# example of getting the current task from the main coroutine
import asyncio
import time 
import random

# coroutine for a task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # block for a  moment
    await asyncio.sleep(value)
    # report the value
    print(f"{time.ctime()} > task {arg} done with {value} ")
   

# define a main coroutine
async def main():
    # report a message 
    print(f"{time.ctime()} main starting.")
    # create many coroutine
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete 
    # ALL_COMPLETED, FIRST_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED)
    print(f"{time.ctime()} all done")
    

# start the asyncio program
asyncio.run(main())

