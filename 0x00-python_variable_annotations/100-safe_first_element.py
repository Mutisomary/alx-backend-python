#!/usr/bin/env python3
"""Duck typing"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Get the first element of an iterable safely."""
    if lst:
        return lst[0]
    else:
        return None
