import asyncio
import multiprocessing
import threading
import time
import math

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
    
def factorial_calc(n):
    num = 0
    factorial = 1
    while factorial <= n:
        if factorial == n:
            return num
        num += 1
        factorial = math.factorial(num)
    if abs(n - math.factorial(num - 1)) <= abs(n - factorial):
        return num - 1
    else:
        return num

async def main():
    loop = asyncio.get_event_loop()
    async_prime = await loop.run_in_executor(None, highest_prime_calc)
    print(f"Async Highest Prime: {async_prime}")
    loop = asyncio.get_event_loop()
    fibonacci = loop.run_in_executor(None, fibonacci_calc, async_prime)
    factorial = loop.run_in_executor(None, factorial_calc, async_prime)
    nth_term, num = await asyncio.gather(fibonacci, factorial)
    print(f"Closest Fibonacci Number is {nth_term}")
    print(f"Closest Factorial is {num}")

def thread_main():
    prime = None
    def worker():
        nonlocal prime
        prime = highest_prime_calc()
    thread_prime = threading.Thread(target = worker)
    thread_prime.start()
    thread_prime.join()
    print(f"Thread Highest Prime: {prime}")

if __name__ == "__main__":
    asyncio.run(main())
    print()
    thread_main()