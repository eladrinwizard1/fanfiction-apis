# Custom-built fanfiction.net API
from api import API, Query, Story


class FFNStory(Story):
    # Class for FFN story data.
    pass


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

    def print_query(self, query: Query):
        # Pretty printing of a Query dataclass with human-readable string values
        pass

    def _generate_query_string(self, query: Query):
        # Generates the URL string for the search query. Internal method for use in search
        return """?
                  &srt={query.sort}\
                  &g1={query.genre_1}\
                  &g2={query.genre_2}\
                  &lan={query.language}\
                  &r={query.rating}\
                  &len={query.length}\
                  &t={query.time}\
                  &s={query.status}\
                  &c1={query.char_1}\
                  &c2={query.char_2}\
                  &c3={query.char_3}\
                  &c4={query.char_4}\
                  &v1={query.world}\
                  &pm={query.pairing}\
                  &_g1={query.no_genre_1}\
                  &_c1={query.no_char_1}\
                  &_c2={query.no_char_2}\
                  &_v1={query.no_world}\
                  &_pm={query.no_pairing}
               """

    def search(self, query: Query):
        # Returns a list of Story objects that are results from the query
        pass

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
