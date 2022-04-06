import asyncio
# import time

from multitrhreading.decorators import async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


@async_measure_time
async def main():
    await asyncio.gather(tick(), tick(), tick())
    # for _ in range(3):
    #     tick()


if __name__ == '__main__':
    asyncio.run(main())
