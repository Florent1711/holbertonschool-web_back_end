#!/usr/bin/env python3
"""Takes two integer arguments page and page_size"""


def index_page(page, page_size):
    start_index = page(- 1) * page_size
    end_index = page * page_size
    return start_index, end_index
