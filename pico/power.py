import machine


def deepsleep(ms: int) -> None:
    """Put the device into deep sleep for the given duration in milliseconds.
    Powers down all peripherals. The device resets and runs main.py on wakeup."""
    machine.deepsleep(ms)
