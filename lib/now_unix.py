"""
Unix timestamp utilities
Equivalent to lib/nowUnix.ahk
"""

import time
from datetime import datetime


def now_unix() -> int:
    """
    Get current Unix timestamp (seconds since epoch)
    Equivalent to nowUnix()

    Returns:
        Current Unix timestamp as integer
    """
    return int(time.time())


def now_unix_ms() -> int:
    """
    Get current Unix timestamp in milliseconds

    Returns:
        Current Unix timestamp in milliseconds as integer
    """
    return int(time.time() * 1000)


def unix_to_datetime(unix_time: int) -> datetime:
    """
    Convert Unix timestamp to datetime object

    Args:
        unix_time: Unix timestamp

    Returns:
        datetime object
    """
    return datetime.fromtimestamp(unix_time)


def datetime_to_unix(dt: datetime) -> int:
    """
    Convert datetime object to Unix timestamp

    Args:
        dt: datetime object

    Returns:
        Unix timestamp
    """
    return int(dt.timestamp())
