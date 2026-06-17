async def sync() -> None:
    """Sync the device RTC from an NTP time server. Requires an active network connection."""
    try:
        import ntptime
        ntptime.settime()
        print("Time synced via NTP")
    except OSError as e:
        print("NTP sync failed:", e)
