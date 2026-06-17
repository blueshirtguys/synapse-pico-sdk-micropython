import network
import asyncio


async def connect(ssid: str, password: str, timeout_ms: int = 10_000) -> None:
    """Connect to a WiFi network. Raises OSError if the connection times out."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    for _ in range(timeout_ms // 100):
        if wlan.isconnected():
            print("WiFi connected:", wlan.ifconfig()[0])
            return
        await asyncio.sleep(0.1)

    raise OSError("WiFi connection timed out")


async def disconnect(timeout_ms: int = 5_000) -> None:
    """Disconnect from WiFi and deactivate the interface. Raises OSError if it times out."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)

    for _ in range(timeout_ms // 100):
        if not wlan.active():
            print("WiFi disconnected")
            return
        await asyncio.sleep(0.1)

    raise OSError("WiFi disconnect timed out")
