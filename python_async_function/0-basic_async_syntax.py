#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay betweeen 0 and max_delay (inclusive) seconds.
    Returns the delay as a float
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# Example usage:


async def main():
    random_delay = await wait_random()
    print(f"Random delay: {random_delay:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
