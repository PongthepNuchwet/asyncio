# example of getting the current task from the main coroutine
import asyncio
import time 
import random

# coroutine for a task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = 1+random.random()
    # report message
    print(f"{time.ctime()} > task got {value}")
    # block for a  moment
    await asyncio.sleep(value)
    # report the value
    print(f"{time.ctime()} > task done ")
   

# define a main coroutine
async def main():
    # report a message 
    print(f"{time.ctime()} main starting.")
    # create a rask
    task = task_coro(1)
    try:
        await asyncio.wait_for(task, timeout=0.2)
    except asyncio.TimeoutError:
        print(f"{time.ctime()} Gave up waiting, task canceled.")
    

# start the asyncio program
asyncio.run(main())

