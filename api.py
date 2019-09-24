# Abstract API class
from dataclasses import dataclass


@dataclass
class Story:
    # Dataclass for handling individual stories
    id: int
    name: str
    chapter_count: int


class SearchParams:
    # Class for a set of search parameters

    def __init__(self):
        # Set search properties
        pass


class API:

    def __init__(self):
        self.host = None
        raise NotImplementedError("Abstract method for specific APIs")

    # Story processing methods

    def get_story_data(self, story: Story):
        # Adds story metadata to a story
        raise NotImplementedError("Abstract method for specific APIs")

    def get_chapter_data(self, story: Story):
        # Adds chapter metadata to a story
        raise NotImplementedError("Abstract method for specific APIs")

    def download_chapters(self, story: Story):
        # Downloads chapters of a story to disk
        raise NotImplementedError("Abstract method for specific APIs")
