"""
Duration formatting utilities
Equivalent to lib/DurationFromSeconds.ahk
"""

import datetime


def duration_from_seconds(secs: float, format_str: str = "hh:mm:ss", capacity: int = 64) -> str:
    """
    Format seconds into a duration string
    Equivalent to DurationFromSeconds()

    Args:
        secs: Number of seconds
        format_str: Format string (Python datetime format)
        capacity: Maximum string length (ignored in Python)

    Returns:
        Formatted duration string
    """
    # Convert seconds to timedelta
    duration = datetime.timedelta(seconds=secs)

    # Handle custom format strings
    if format_str == "hh:mm:ss":
        hours, remainder = divmod(int(duration.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    elif format_str.startswith("h'h' m") or format_str.startswith("m'm' s"):
        # Custom format for hmsFromSeconds
        parts = []
        total_seconds = int(secs)

        if total_seconds >= 3600:
            hours = total_seconds // 3600
            parts.append(f"{hours}h")
            total_seconds %= 3600

        if total_seconds >= 60 or (not parts and total_seconds > 0):
            minutes = total_seconds // 60
            parts.append(f"{minutes}m")
            total_seconds %= 60

        if total_seconds > 0 or not parts:
            parts.append(f"{total_seconds}s")

        return " ".join(parts)
    else:
        # For other formats, use Python's strftime
        return str(duration)


def hms_from_seconds(secs: float) -> str:
    """
    Format seconds into human-readable format (e.g., "1h 30m 45s")
    Equivalent to hmsFromSeconds()

    Args:
        secs: Number of seconds

    Returns:
        Human-readable duration string
    """
    return duration_from_seconds(secs, ((secs >= 3600) and "h'h' m" or "") + ((secs >= 60) and "m'm' s" or "") + "s's'")
