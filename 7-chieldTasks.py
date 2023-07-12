# example of getting the current task from the main coroutine
import asyncio
import time 
import random

# define a simple asynchronous
async def simple_task(number):
    # block for a moment
    await asyncio.sleep(1)
    # return the argument
    return number

async def cancel_task(task):
    # block fir a moment
    await asyncio.sleep(0.2)
    # cancel the task
    was_canceled = task.cancel()
    print(f"{time.ctime()} canceled {was_canceled}")


# define a main coroutine
async def main():
    # report a message 
    print(f"{time.ctime()} main starting.")
    # create the coroutine
    coro = simple_task(1)
    # create a task 
    task = asyncio.create_task(coro)
    # create the chielded task
    shielded = asyncio.shield(task)
    # create the task to cancel the previous task
    asyncio.create_task(cancel_task(shielded))
    # asyncio.create_task(cancel_task(task))
    # handle cancellation
    try:
        result = await shielded
        print(f"{time.ctime()} > got {result}")
    except asyncio.CancelledError:
        print(f"{time.ctime()} shielded was cancle.")

    # wait a moment 
    await asyncio.sleep(1)

    print(f"{time.ctime()} shielded: {shielded}")
    print(f"{time.ctime()} task: {task}")
    
# start the asyncio program
asyncio.run(main())

