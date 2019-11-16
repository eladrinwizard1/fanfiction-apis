# Add root of project to path
import sys
sys.path.append("..")

from fanfiction_apis import ffn

PATH = "C:/Users/vijay/Documents/hp_data"


def test_init():
    api = ffn.FFN("book", "Harry Potter", PATH)


def test_search():
    api = ffn.FFN("book", "Harry-Potter", PATH)
    query = ffn.FFNQuery(sort=4)
    stories = api.search(query, 2)
    [print(story.name) for story in stories]


def test_get_story_data():
    api = ffn.FFN("book", "Harry-Potter", PATH)
    query = ffn.FFNQuery(sort=4, rating=10, length=11)
    story = api.search(query, 1)[13]
    api.get_story_data(story)
    print(story)


def test_get_chapter_data():
    api = ffn.FFN("book", "Harry-Potter", PATH)
    query = ffn.FFNQuery(sort=4, rating=10)
    story = api.search(query, 1)[0]
    api.get_story_data(story)
    api.get_chapter_data(story)


test_get_story_data()
