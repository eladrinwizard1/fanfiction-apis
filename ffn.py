# Custom-built fanfiction.net API
import requests
from bs4 import BeautifulSoup

from api import API, Query, Story


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
    chapter_count: int = 0
    word_count: int = 0
    review_count: int = 0
    update_time: int = 0
    publication_time: int = 0
    pass

    def set_from_url(self, url):
        # Takes in relative url string and sets id and name
        (self.id, self.name) = url.split('/')[2:4]

    def generate_url(self):
        # Returns relative url string for story
        return f"/s/{self.id}/{self.name}"


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
        # TODO: Iterate over types of fanfiction source and find source
        # TODO: Convert source string into hyphenated string (helper fn in separate or same lib?)

    # Query methods

    def get_categories(self):
        # Retrieves and constructs dictionary of categories with labels
        pass

    def print_query(self, query: Query):
        # Pretty printing of a Query dataclass with human-readable string values
        pass

    def _generate_query_string(self, query: Query):
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

    def search(self, query: Query):
        # Returns a list of Story objects with only urls that are results from the query
        src = requests.get(self.host + self._generate_query_string(query))
        soup = BeautifulSoup(src.content, 'html.parser')
        story_urls = [a["href"] for a in soup.find_all("a", class_="stitle")]
        stories = []
        for url in story_urls:
            story = FFNStory()
            story.set_from_url(url)
            stories.append(story)
        return stories

    # Story methods

    def get_story_data(self, story: Story):
        # Adds story metadata to a story
        pass

    def get_chapter_data(self, story: Story):
        # Adds chapter metadata to a story
        pass

    def download_chapters(self, story: Story):
        # Downloads chapters of a story to disk
        pass
