# Custom-built Archive of Our Own API

from .api import API


class AO3(API):

    def __init__(self):
        self.host = "https://archiveofourown.org/"
