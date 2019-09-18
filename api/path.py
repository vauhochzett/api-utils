# encoding=utf-8
""" API path handling """

from typing import List, Tuple


def join(first: str, *others: str) -> str:
    """
	Join one or more path components intelligently.
	Contrary to `os.path`, "absolute paths" are not denoted by a starting slash, but by a protocol.
	Rules:
	- The returned path will always start with "/", except if the first component starts with "http"
	- The returned path will never end with "/", except when enforced (see below)
	- A trailing slash can be enforced with a final component "/"
	- Empty components will be discarded
	"""

    # Remove all whitespace components
    all_components: List[str] = [p for p in [first, *others] if p.strip() != ""]

    if not all_components:
        return ""

    sep = "/"
    # Empty components have been removed above
    end_sep: bool = all_components[-1] == sep

    path_comps: List[str] = [""]  # Always start with a sep

    # Strip seps and...
    for comp in [p.strip(sep) for p in all_components]:
        # ...filter empty strings again to ensure that "/" and "//" do not result in double slashes
        if comp == "" or comp.isspace():
            continue
        # Reset when it's an absolute path
        elif comp.startswith("http"):
            path_comps = [comp]
        else:
            path_comps.append(comp)

    if end_sep:
        path_comps.append("")

    result = sep.join(path_comps)
    return result
