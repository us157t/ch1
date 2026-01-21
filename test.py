import asyncio

async def say(n):
    await asyncio.sleep(1)
    print(n)

c = [say(i) for i in range(10)]
loop = asyncio.get_event_loop()
loop.run_util_complete(asyncio.wait(c))
loop.close()