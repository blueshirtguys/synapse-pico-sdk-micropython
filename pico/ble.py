import asyncio
import bluetooth


async def enable(timeout_ms: int = 5_000) -> None:
    """Activate the BLE radio. Raises OSError if it times out."""
    ble = bluetooth.BLE()
    ble.active(True)

    for _ in range(timeout_ms // 100):
        if ble.active():
            print("Bluetooth enabled")
            return
        await asyncio.sleep(0.1)

    raise OSError("BLE enable timed out")


async def disable(timeout_ms: int = 5_000) -> None:
    """Deactivate the BLE radio. Raises OSError if it times out."""
    ble = bluetooth.BLE()
    ble.active(False)

    for _ in range(timeout_ms // 100):
        if not ble.active():
            print("Bluetooth disabled")
            return
        await asyncio.sleep(0.1)

    raise OSError("BLE disable timed out")
