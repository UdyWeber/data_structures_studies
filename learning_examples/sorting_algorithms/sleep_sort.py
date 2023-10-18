import asyncio

results = []


async def say_after(delay, what):
    await asyncio.sleep(delay)
    results.append(delay)
    print(what)


async def sleep_sort(x: list[int]):
    for i in x:
        asyncio.create_task(say_after(i, f"{i} ({i} wakes up so print it)"))

    await asyncio.sleep(max(x) + 2)

if __name__ == "__main__":
    asyncio.run(sleep_sort([1, 8, 2, 5, 4]))
    print(results)
