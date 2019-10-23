# Add root of project to path
import sys
sys.path.append("..")

import ffn


def test_search():
    api = ffn.FFN("book", "Harry-Potter")
    query = ffn.FFNQuery()
    stories = api.search(query, 2)
    print(len(stories))
    print(stories[0].name)


def test_get_story_data():
    api = ffn.FFN("book", "Harry-Potter")
    query = ffn.FFNQuery()
    story = api.search(query, 1)[0]
    api.get_story_data(story)


test_search()
test_get_story_data()
