import time

_MICROPYTHON_EPOCH_OFFSET = 946684800


async def sync() -> None:
    """Sync the device RTC from an NTP time server. Requires an active network connection."""
    try:
        import ntptime
        ntptime.settime()
        print("Time synced via NTP")
    except OSError as e:
        print("NTP sync failed:", e)


def unix_time() -> int:
    """Return the current time as a Unix timestamp (seconds since 1970-01-01).

    MicroPython's time.time() counts from 2000-01-01; this corrects for that offset.
    Call clock.sync() first to ensure the RTC has been set via NTP.
    """
    return time.time() + _MICROPYTHON_EPOCH_OFFSET
