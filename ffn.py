# Custom-built fanfiction.net API

from .api import API


class FFN(API):

    def __init__(self, source: str):
        self.host = "https://www.fanfiction.net/"  # + whatever the rest of the url for the source is
        # TODO: Iterate over types of fanfiction source and find source
        # TODO: Convert source string into hyphenated string (helper fn in separate or same lib?)
