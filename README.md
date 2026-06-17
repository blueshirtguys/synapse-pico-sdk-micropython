# synapse-pico-sdk-micropython

MicroPython helpers for Raspberry Pi Pico W — WiFi, BLE, clock sync, and deep sleep.

## Install

Copy the `pico/` directory onto your device's filesystem (e.g. via `mpremote cp -r pico :`),
or install with `mip`:

```python
import mip
mip.install("github:blueshirtguys/synapse-pico-sdk-micropython")
```

## Usage

See [examples/main.py](examples/main.py) for a complete runnable script. Minimal version:

```python
import asyncio
from pico import ble, clock, power, wifi

async def main():
    await ble.disable()
    await wifi.connect("your-ssid", "your-password")
    await clock.sync()
    await wifi.disconnect()
    power.deepsleep(60_000)

asyncio.run(main())
```

## API

### `pico.wifi`

| Function | Description |
|---|---|
| `await wifi.connect(ssid, password, timeout_ms=10_000)` | Connect to a WiFi network. Raises `OSError` if the connection times out. |
| `await wifi.disconnect(timeout_ms=5_000)` | Disconnect and deactivate the WiFi interface. Raises `OSError` if it times out. |

### `pico.ble`

| Function | Description |
|---|---|
| `await ble.enable(timeout_ms=5_000)` | Activate the BLE radio. Raises `OSError` if it times out. |
| `await ble.disable(timeout_ms=5_000)` | Deactivate the BLE radio. Raises `OSError` if it times out. |

### `pico.clock`

| Function | Description |
|---|---|
| `await clock.sync()` | Sync the device RTC from an NTP time server. Requires an active WiFi connection. Silently swallows `OSError` on failure. |
| `clock.unix_time()` | Return the current time as a Unix timestamp (seconds since 1970-01-01). MicroPython's `time.time()` counts from 2000-01-01; this corrects for that offset. Call `clock.sync()` first. |

### `pico.power`

| Function | Description |
|---|---|
| `power.deepsleep(ms)` | Put the device into deep sleep for the given duration in milliseconds. All peripherals are powered down; the device resets and runs `main.py` on wakeup. |

## Local secrets

Never commit your WiFi credentials. Keep them in a `secrets.py` on the device's filesystem —
add it to `.gitignore` so it stays off version control.

## License

[MIT](LICENSE)
