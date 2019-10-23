# Custom-built fanfiction.net API
import re
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup

from api import API, Query, Story, User


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
    title: str = ""  # Note: this is the actual title, not the url-formatted title
    author: FFNUser = None
    chapter_count: int = 0
    word_count: int = 0
    review_count: int = 0
    update_time: int = 0
    publication_time: int = 0

    def set_from_url(self, url) -> None:
        # Takes in relative url string and sets id and name
        (self.id, _, self.name) = url.split('/')[2:5]

    def generate_url(self) -> str:
        # Returns relative url string for story
        return f"/s/{self.id}/1/{self.name}"


@dataclass
class FFNQuery(Query):
    # Class for a set of FFN search parameters. Data is stored as ints and converted to strings for human readability

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


class FFN(API):

    def __init__(self, category: str, source: str):
        super().__init__(f"https://www.fanfiction.net/{category}/{source}/")
        # TODO: Convert source string into hyphenated string (helper fn in separate or same lib?)

    def _set_categories(self) -> None:
        # Retrieves and constructs dictionary of categories with labels
        pass

    # Query methods

    def print_query(self, query: FFNQuery) -> None:
        # Pretty printing of a Query dataclass with human-readable string values
        pass

    def _generate_query_string(self, query: FFNQuery) -> str:
        # Generates the URL string for the search query. Internal method for use in search
        return """?
                  &srt={query.sort}\
                  &t={query.time}\
                  &g1={query.genre_1}\
                  &g2={query.genre_2}\
                  &r={query.rating}\
                  &lan={query.language}\
                  &len={query.length}\
                  &s={query.status}\
                  &v1={query.world}\
                  &c1={query.char_1}\
                  &c2={query.char_2}\
                  &c3={query.char_3}\
                  &c4={query.char_4}\
                  &pm={query.pairing}\
                  &_g1={query.no_genre_1}\
                  &_c1={query.no_char_1}\
                  &_c2={query.no_char_2}\
                  &_v1={query.no_world}\
                  &_pm={query.no_pairing}
               """

    def search(self, query: FFNQuery, pages: int = 1) -> List[FFNStory]:
        # Returns a list of Story objects with only urls that are results from the query
        # Note that a page by default has 25 stories
        stories = []
        for i in range(1, pages + 1):
            src = requests.get(self.host + self._generate_query_string(query) + "&p={i}")
            soup = BeautifulSoup(src.content, 'html.parser')
            story_urls = [a["href"] for a in soup.find_all("a", class_="stitle")]
            if len(story_urls) == 0:
                break
            for url in story_urls:
                story = FFNStory()
                story.set_from_url(url)
                stories.append(story)
        return stories

    # Story methods

    def get_story_data(self, story: FFNStory) -> None:
        # Adds story metadata to a story
        src = requests.get(self.host + story.generate_url())
        soup = BeautifulSoup(src.content, 'html.parser')
        metadata_elt = soup.find(string=re.compile("Favs")).parent
        # TODO: process metadata_elt
        pass

    def get_chapter_data(self, story: FFNStory) -> None:
        # Adds chapter metadata to a story
        pass

    def download_chapters(self, story: FFNStory) -> None:
        # Downloads chapters of a story to disk
        pass

    # User methods

    def get_stories(self, user: FFNUser) -> List[FFNStory]:
        # Gets stories from a particular author
        pass
