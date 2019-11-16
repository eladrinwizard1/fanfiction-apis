# Helper functions for string processing in get_story_data
from datetime import date
from typing import List, Tuple, Dict


def num_from_meta(meta_tags: List[str], label: str) -> int:
    matches = [x for x in meta_tags if label in x]
    return "" if len(matches) == 0 \
        else int(matches[0].split(": ")[1].replace(',', ''))


def str_from_meta(meta_tags: List[str], label: str) -> str:
    matches = [x for x in meta_tags if label in x]
    return "" if len(matches) == 0 else matches[0]


def date_from_meta(meta_tags: List[str], label: str) -> date:
    tag_array = str_from_meta(meta_tags, label).split(": ")[1].split("/")
    return date.today() if len(tag_array) == 1 \
        else date(int(tag_array[2]), int(tag_array[0]), int(tag_array[1]))


def get_int_rating(meta_tags: List[str]) -> int:
    rating = str_from_meta(meta_tags, "Rated").replace("Fiction  ", "")
    ratings = {"K": 1, "K+": 2, "T": 3, "M": 4}
    return ratings.get(rating, 0)


def get_genres(label: str, genres: Dict[str, str]) -> Tuple[int, int]:
    tag_array = label.strip().split("/", 1)
    genre_list = [int(genres.get(tag_array[i], 0)) if len(tag_array) > i else 0
                  for i in range(2)]
    return genre_list[0], genre_list[1]


def get_chars(label: str, names: Dict[str, str]) \
        -> Tuple[int, int, int, int]:
    tag_array = label.strip().split(", ")
    name_list = [int(names.get(tag_array[i], 0)) if len(tag_array) > i else 0
                 for i in range(4)]
    return name_list[0], name_list[1], name_list[2], name_list[3]


# JSON encoder for stories
def encode_story(o):
    if type(o) == date:
        return o.strftime("%Y-%m-%d")
    return vars(o)
