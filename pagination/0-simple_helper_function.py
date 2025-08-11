#!/usr/bin/env python3
"""return the start and end index for pagination
"""


def index_range(page, page_size):
    """return tuple start and end
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
