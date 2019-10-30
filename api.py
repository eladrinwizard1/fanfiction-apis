# TODO: Fix this after finishing ffn.py
# Abstract API class
import os
from dataclasses import dataclass

HEADERS = {  # TODO: Figure out which of these are unneeded
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; "
                  "x64) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Chrome/77.0.3865.120 "
                  "Safari/537.36",
    "Accept": "text/html"
              "application/signed-exchange;v=b3",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "__gads=Test; cookies=yes",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
}


@dataclass
class User:
    # Dataclass for handling users
    pass


@dataclass
class Story:
    # Dataclass for handling individual stories

    def set_from_url(self, url):
        # Takes in relative url string and sets id and name
        raise NotImplementedError("Abstract method")

    def generate_url(self, chapter):
        # Returns relative url string for story
        raise NotImplementedError("Abstract method")


@dataclass
class Query:
    # Abstract class for a set of search parameters

    def generate_query_string(self):
        # Generates the URL string for the search query.
        # Internal method for use in search
        raise NotImplementedError("Abstract method for specific APIs")


class API:

    def __init__(self, host, path):
        self.host = host
        self.path = path
        if not os.path.exists(path):
            os.makedirs(path)
        self.headers = HEADERS

    # Query methods

    def _set_categories(self):
        # Retrieves and constructs dictionary of categories with labels
        raise NotImplementedError("Abstract method for specific APIs")

    def print_query(self, query: Query):
        # Pretty printing of a Query dataclass with human-readable string values
        raise NotImplementedError("Abstract method for specific APIs")

    def search(self, query: Query):
        # Returns a list of Story objects that are results from the query
        raise NotImplementedError("Abstract method for specific APIs")

    # Story methods

    def get_story_data(self, story: Story):
        # Adds story metadata to a story
        raise NotImplementedError("Abstract method for specific APIs")

    def get_chapter_data(self, story: Story):
        # Downloads chapters of a story
        raise NotImplementedError("Abstract method for specific APIs")

    # User methods

    def get_stories(self, user: User):
        # Gets stories from a particular author
        pass
