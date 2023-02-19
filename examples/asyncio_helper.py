import asyncio

from openttd_helpers import asyncio_helper


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    asyncio_helper.enable_strong_referenced_tasks(loop)

    loop.create_task(asyncio.sleep(1))
    loop.close()


if __name__ == "__main__":
    main()
