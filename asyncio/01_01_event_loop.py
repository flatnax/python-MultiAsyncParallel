import asyncio
# import time

# from multitrhreading.decorators import async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print('loop is still running')


async def main():
    awaitable_obj = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable_obj


if __name__ == '__main__':
    # coroutine = main()
    # print(coroutine)

    # asyncio.run(main())

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.create_task(main())
        loop.run_forever()
        # loop.run_until_complete(main())
        print('coroutines have finished')
    except KeyboardInterrupt:
        print('Manually closed app')
    finally:
        loop.close()
        print('loop is closed')
        print(f'loop is closed = {loop.is_closed()}')
