# Helper functions for string processing
from typing import List


def num_from_meta(meta_tags: List[str], label: str) -> int:
    matches = [x for x in meta_tags if label in x]
    if len(matches) == 0:
        return 0
    else:
        meta_tag = matches[0]
    return int(meta_tag.split(": ")[1].replace(',', ''))
