import asyncio
import multiprocessing
import threading
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def highest_prime_calculation():
    highest_prime = 0
    n = 0
    start_time = time.time()
    while time.time() - start_time() <= 180:
        if is_prime(n):
            highest_prime = n
        n += 1
    return highest_prime

async def asynchronous_calc():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None,highest_prime_calculation)

async def main():
    async_prime = await asynchronous_calc()
    print(f"Async Highest Prime: {async_prime}")

if __name__ == "__main__":
    asyncio.run(main())