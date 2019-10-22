# Add root of project to path
import sys
sys.path.append("..")

import ffn


def test_search():
    api = ffn.FFN("book", "Harry-Potter")
    query = ffn.FFNQuery()
    stories = api.search(query)
    print(len(stories))
    print(stories[0].name)


test_search()
