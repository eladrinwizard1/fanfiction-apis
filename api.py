# TODO: Fix this after finishing ffn.py
# Abstract API class
from dataclasses import dataclass


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

    def generate_url(self):
        # Returns relative url string for story
        raise NotImplementedError("Abstract method")


@dataclass
class Query:
    # Abstract class for a set of search parameters
    pass


class API:

    def __init__(self, host):
        self.host = host

    # Query methods

    def _set_categories(self):
        # Retrieves and constructs dictionary of categories with labels
        raise NotImplementedError("Abstract method for specific APIs")

    def print_query(self, query: Query):
        # Pretty printing of a Query dataclass with human-readable string values
        raise NotImplementedError("Abstract method for specific APIs")

    def _generate_query_string(self, query: Query):
        # Generates the URL string for the search query. Internal method for use in search
        raise NotImplementedError("Abstract method for specific APIs")

    def search(self, query: Query):
        # Returns a list of Story objects that are results from the query
        raise NotImplementedError("Abstract method for specific APIs")

    # Story methods

    def get_story_data(self, story: Story):
        # Adds story metadata to a story
        raise NotImplementedError("Abstract method for specific APIs")

    def get_chapter_data(self, story: Story):
        # Adds chapter metadata to a story
        raise NotImplementedError("Abstract method for specific APIs")

    def download_chapters(self, story: Story):
        # Downloads chapters of a story to disk
        raise NotImplementedError("Abstract method for specific APIs")

    # User methods

    def get_stories(self, user: User):
        # Gets stories from a particular author
        pass
