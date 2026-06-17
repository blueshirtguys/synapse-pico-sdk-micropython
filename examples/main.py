import asyncio
from pico import ble, clock, power, wifi

WIFI_SSID = "your-ssid"
WIFI_PASSWORD = "your-password"


async def main():
    await ble.disable()
    await wifi.connect(WIFI_SSID, WIFI_PASSWORD)
    await clock.sync()
    await wifi.disconnect()

    power.sleep()


if __name__ == "__main__":
    asyncio.run(main())
