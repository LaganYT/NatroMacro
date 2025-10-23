"""
High-precision sleep function
Equivalent to lib/HyperSleep.ahk
"""

import time


def hyper_sleep(ms: float):
    """
    High-precision sleep function
    Equivalent to HyperSleep()

    Args:
        ms: Milliseconds to sleep
    """
    start_time = time.perf_counter()
    end_time = start_time + (ms / 1000.0)

    while time.perf_counter() < end_time:
        remaining = end_time - time.perf_counter()
        if remaining > 0.03:  # 30ms threshold
            time.sleep(0.001)  # Sleep for 1ms
        # Busy wait for remaining time for higher precision


def sleep_ms(ms: float):
    """
    Convenience function for sleeping in milliseconds
    """
    hyper_sleep(ms)


def sleep_us(us: float):
    """
    Convenience function for sleeping in microseconds
    """
    hyper_sleep(us / 1000.0)
