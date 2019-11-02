# Custom-built fanfiction.net API
import concurrent.futures
import os
import threading
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

from api import API, Query, Story, User
from lib.string_lib import num_from_meta


@dataclass
class FFNUser(User):
    # Class for FFN user data.
    id: int = 0
    username: str = ""


@dataclass
class FFNStory(Story):
    # Class for FFN story data.

    # Identifying properties
    id: int = 0
    name: str = ""

    # Search parameter properties
    rating: int = 0
    language: int = 0
    genre_1: int = 0
    genre_2: int = 0

    # Other properties
    title: str = ""  # This is the actual title, not the url-formatted title
    author: FFNUser = None
    chapter_count: int = 0
    word_count: int = 0
    review_count: int = 0
    favorites_count: int = 0
    follows_count: int = 0
    update_time: int = 0
    publication_time: int = 0

    def set_from_url(self, url) -> None:
        # Takes in relative url string and sets id and name
        (self.id, _, self.name) = url.split('/')[2:5]

    def generate_url(self, chapter: int = 1) -> str:
        # Returns relative url string for story
        return f"https://www.fanfiction.net/s/{self.id}/{chapter}"


@dataclass
class FFNQuery(Query):
    # Class for a set of FFN search parameters. Data is stored as ints and
    # converted to strings for human readability

    # "With" filters
    sort: int = 0
    time: int = 0
    genre_1: int = 0
    genre_2: int = 0
    rating: int = 0
    language: int = 0
    length: int = 0
    status: int = 0
    world: int = 0
    char_1: int = 0
    char_2: int = 0
    char_3: int = 0
    char_4: int = 0
    pairing: int = 0

    # "Without" filters
    no_genre_1: int = 0
    no_char_1: int = 0
    no_char_2: int = 0
    no_world: int = 0
    no_pairing: int = 0

    def generate_query_string(self) -> str:
        # Generates URL string for search query
        return f"?srt={self.sort}" + \
               f"&t={self.time}" + \
               f"&g1={self.genre_1}" + \
               f"&g2={self.genre_2}" + \
               f"&r={self.rating}" + \
               f"&lan={self.language}" + \
               f"&len={self.length}" + \
               f"&s={self.status}" + \
               f"&v1={self.world}" + \
               f"&c1={self.char_1}" + \
               f"&c2={self.char_2}" + \
               f"&c3={self.char_3}" + \
               f"&c4={self.char_4}" + \
               f"&pm={self.pairing}" + \
               f"&_g1={self.no_genre_1}" + \
               f"&_c1={self.no_char_1}" + \
               f"&_c2={self.no_char_2}" + \
               f"&_v1={self.no_world}" + \
               f"&_pm={self.no_pairing}"


class FFN(API):

    def __init__(self, category: str, source: str, path: str):
        source = source.replace(" ", "-")
        super().__init__(f"https://www.fanfiction.net/{category}/{source}/",
                         path)
        self._set_categories()

    def _set_categories(self) -> None:
        # Retrieves and constructs dictionary of categories with labels
        categories = {}
        src = requests.get(self.host)
        soup = BeautifulSoup(src.content, 'lxml')
        selectors = soup.find(id="myform").find_all("select")
        labels = ["sort", "time", "genre_1", "genre_2", "rating", "language",
                  "length", "status", "world", "char_1", "char_2", "char_3",
                  "char_4", "no_genre_1", "no_char_1", "no_char_2", "no_world"]
        for selector, label in zip(selectors, labels):
            categories[label] = {}
            for opt in selector.find_all("option"):
                categories[label][str(opt["value"])] = opt.string
        pairings = {"0": "False", "1": "True"}
        categories["pairing"] = pairings
        categories["no_pairing"] = pairings
        self.categories = categories

    # Query methods

    def print_query(self, query: FFNQuery) -> None:
        # Pretty printing of a Query dataclass with human-readable string values
        pass

    def search(self, query: FFNQuery, pages: int = 1) -> List[FFNStory]:
        # Returns a list of Story objects with only urls that are results from
        # the query. Note that a page by default has 25 stories
        stories = []
        for i in range(1, pages + 1):
            src = requests.get(self.host + query.generate_query_string() +
                               f"&p={i}", headers=self.headers)
            soup = BeautifulSoup(src.content, 'lxml')
            story_urls = [a["href"] for a in
                          soup.find_all("a", class_="stitle")]
            if len(story_urls) == 0:
                break
            for url in story_urls:
                story = FFNStory()
                story.set_from_url(url)
                stories.append(story)
        return stories

    # Story methods

    def _make_story_folder(self, story: FFNStory) -> str:
        # Creates directory for storing story information
        abs_path = self.path + f"/{story.name}/"
        if not os.path.exists(abs_path):
            os.makedirs(abs_path)
        return abs_path

    def get_story_data(self, story: FFNStory) -> None:
        # Adds story metadata to a story object and saves output to txt file
        abs_path = self._make_story_folder(story)
        src = requests.get(story.generate_url(), headers=self.headers)
        soup = BeautifulSoup(src.content, 'lxml')
        metadata_elt = soup.find("a",
                                 href="https://www.fictionratings.com/").parent
        raw_text_array = metadata_elt.text.split(" - ")

        # TODO: Fix case where no reviews
        story.chapter_count = num_from_meta(raw_text_array, "Chapters")
        story.word_count = num_from_meta(raw_text_array, "Words")
        story.review_count = num_from_meta(raw_text_array, "Reviews")
        story.favorites_count = num_from_meta(raw_text_array, "Favs")
        story.follows_count = num_from_meta(raw_text_array, "Follows")
        story.title = story.name.replace("-", " ")  # TODO: Make less hackish

        # TODO: Finish processing these parameters
        story.rating = 0
        story.language = 0
        story.genre_1 = 0
        story.genre_2 = 0
        story.author = None
        story.update_time = 0
        story.publication_time = 0

    # TODO: test threading and learn how it works
    def get_chapter_data(self, story: FFNStory) -> None:
        # Downloads chapters of a story
        thread_local = threading.local()

        def get_session():
            if not hasattr(thread_local, "session"):
                thread_local.session = requests.Session()
            return thread_local.session

        def download_chapter(url_tuple):
            url, i = url_tuple
            session = get_session()
            with session.get(url) as src:
                src = session.get(url, headers=self.headers)
            soup = BeautifulSoup(src.content, 'lxml')
            p_arr = soup.find("div", id="storytext").find_all("p")
            with open(f"{abs_path}chapter-{i}.txt", "w+", encoding="utf8") as f:
                for p in p_arr:
                    f.write(f"{p.get_text()}\n")

        abs_path = self._make_story_folder(story)
        urls = [(story.generate_url(i), i) for i in range(story.chapter_count)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_chapter, urls)

    # User methods

    def get_stories(self, user: FFNUser) -> List[FFNStory]:
        # Gets stories from a particular author
        pass
