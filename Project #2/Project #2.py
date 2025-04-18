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

def highest_prime_calc():
    highest_prime = 0
    n = 0
    start_time = time.time()
    while time.time() - start_time <= 180:
        if is_prime(n):
            highest_prime = n
        n += 1
    return highest_prime

def fibonacci_calc(n):
    a, b = 0, 1
    nth_term = 0
    while a <= n:
        if a == n:
            return nth_term
        a, b = b, a + b
        nth_term += 1
    if abs(n - (b - a)) <= abs(n - a):
        return nth_term - 1
    else:
        return nth_term
    
async def async_calc():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, highest_prime_calc)

async def main():
    async_prime = await async_calc()
    print(f"Async Highest Prime: {async_prime}")
    nth_term = fibonacci_calc(async_prime)
    print(f"Closest Fibonacci Number is {nth_term}")

if __name__ == "__main__":
    asyncio.run(main())