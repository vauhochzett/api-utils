""" Test module for apiu.path """

from typing import List, Tuple

import apiu.path


def test_join():
    test_cases: List[Tuple[List[str], str]] = [
        # Always starts with "/", never ends with "/" for normal inputs
        (["abc"], "/abc"),
        (["a/", "b/", "c/"], "/a/b/c"),
        (["/a", "/b", "/c"], "/a/b/c"),
        (["/abc/"], "/abc"),
        (["/a", "b/"], "/a/b"),
        (["/a/", "/b/", "/c/"], "/a/b/c"),
        (["a", "b", "c", "d"], "/a/b/c/d"),
        # Last component "/" -> trailing slash
        (["l", "b", "c", "/"], "/l/b/c/"),
        (["l", "", "/"], "/l/"),
        (["/", "l", "b", "c"], "/l/b/c"),
        (["/", "", "l"], "/l"),
        (["/", "", "l", "/"], "/l/"),
        # Last component "" -> no trailing slash
        (["a", ""], "/a"),
        # Absolute paths starting with "http" -> no starting slash
        (["https://"], "https://"),
        (["https://", "/a"], "https://a"),
        (["http://", "abc.de/", "/g", "/"], "http://abc.de/g/"),
        (["https://", "abc.de", "g", ""], "https://abc.de/g"),
        (["a", "b", "", "https://", "bc.de"], "https://bc.de"),
        (["http://r.a/w/", "x"], "http://r.a/w/x"),
        (["http://xyz", "x", "/"], "http://xyz/x/"),
        # Spaces are preserved
        (["  ", "", "/e /", ""], "/  /e "),
        (["", "  ", "  e  ", "", "/"], "/  /  e  /"),
        # Ensure robustness
        ([""], ""),
        (["", "", ""], ""),
        (["", "r", "", "/b/", "/c", "/", ""], "/r/b/c"),
        (["", "", "r"], "/r"),
        (["", "", "/r"], "/r"),
        (["/r/", ""], "/r"),
    ]

    for inputs, expected_result in test_cases:
        actual_result = apiu.path.join(*inputs)
        assert expected_result == actual_result
