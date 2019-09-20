""" API path handling """

from typing import List, Tuple


def join(first: str, *others: str) -> str:
    """
    Join one or more path components intelligently.

    Rules:
    - If any component starts with "http", all previous parts will be discarded.
    - The returned path will always start with "/", except if it starts with "http".
    - The returned path will never end with "/", except when ending in a protocol
      notation ("://") or enforced (see below)
    - A trailing slash can be enforced with a final component "/"
    - Empty strings are skipped

    Examples:
    - join("https://")                           ->  "https://
    - join("web", "rest", "2.0")                 ->  "/web/rest/2.0"
    - join("http://example.com/", "/api/", "/")  ->  "http://example.com/api/"
    """

    all_components: List[str] = [first, *others]

    if any(type(x) not in {str, bytes} for x in all_components):
        raise TypeError("expected str or bytes objects")

    sep = "/"
    final_sep_enforced: bool = all_components[-1] == sep

    final_path: str = sep

    for comp in all_components:
        if comp == "":
            continue

        assert final_path.endswith(sep)

        remove_start_sep: bool = comp[0] == sep and final_path.endswith(sep)
        append_end_sep: bool = comp[-1] != sep

        # Absolute path: Reset path
        if comp.startswith("http"):
            final_path = ""
            remove_start_sep = False

        if remove_start_sep:
            comp = comp[1:]

        if append_end_sep:
            comp += sep

        final_path += comp

    is_protocol: bool = final_path.endswith("://")
    if not final_sep_enforced and not is_protocol:
        final_path = final_path[:-1]

    return final_path
