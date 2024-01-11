#!/usr/bin/env python3
"""Module thats returns mixed lists"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns their sum as a float."""
    return sum(mxd_lst)
