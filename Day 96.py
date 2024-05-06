import time, asyncio

async def function1():
    await asyncio.sleep(3)
    print("func 1")

async def function2():
    await asyncio.sleep(3)
    print("func 2")

async def function3():
    await asyncio.sleep(3)
    print("func 3")

async def main():
    L = await asyncio.gather(function1(), function2(), function3())
    print(L)

asyncio.run(main())