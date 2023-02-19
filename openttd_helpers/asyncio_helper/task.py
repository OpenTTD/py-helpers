import asyncio


TASKS = set()


def _create_task_factory(parent_factory):
    def task_factory_impl(loop, coro):
        if parent_factory is None:
            task = asyncio.tasks.Task(coro, loop=loop)
        else:
            task = parent_factory(loop, coro)

        task.add_done_callback(TASKS.discard)
        TASKS.add(task)

        return task

    return task_factory_impl


def enable_strong_referenced_tasks(loop=None):
    """
    Ensures that all tasks created have a strong reference, so the GC doesn't
    clean them up unexpectedly.

    This is a design choice of asyncio; just one that is rather annoying to
    deal with.
    """

    if loop is None:
        loop = asyncio.get_event_loop()

    task_factory = loop.get_task_factory()
    new_task_factory = _create_task_factory(task_factory)
    loop.set_task_factory(new_task_factory)
