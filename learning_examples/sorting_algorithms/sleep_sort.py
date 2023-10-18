import asyncio

results = []
DELAY_DIVISION = 25000


async def say_after(delay, what):
    await asyncio.sleep(delay / DELAY_DIVISION)
    results.append(delay)
    print(what)


async def sleep_sort(x: list[int]):
    for i in x:
        asyncio.create_task(say_after(i, f"{i} ({i} wakes up so print it)"))

    await asyncio.sleep((max(x) + 2) / DELAY_DIVISION)

if __name__ == "__main__":
    asyncio.run(sleep_sort([1, 8, 2, 92, 5, 4, 9, 3, 6, 75]))
    print(results)
