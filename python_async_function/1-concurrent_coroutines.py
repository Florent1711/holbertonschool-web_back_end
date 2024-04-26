#!/usr/bin/env python3
"""asynchrone routine"""

import asyncio
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Returns a list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    # Gather the result in the order they complete
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

# Exemple usage:


async def main():
    n = 5  # Number of times to spawn wait_random
    max_delay = 5  # Maximum delay in seconds
    delays = await wait_n(n, max_delay)
    print(f"Delays (ascending order): {delays}")


if __name__ == "__main__":
    asyncio.run(main())
