# example of getting the current task from the main coroutine
import asyncio
import time 

# coroutine for a task
async def task_coro(value):
    # report a message
    print(f"{time.ctime()} task {value} executing")
    # sleep fot a moment
    await asyncio.sleep(1)

# define a main coroutine
async def main():
    # report a message 
    print(f"{time.ctime()} main starting.")
    # create many coroutine
    coros = [task_coro(i) for i in range(100)]
    # run the tasks
    await asyncio.gather(*coros)
    # report a message
    print(f"{time.ctime()} main done")
    

# start the asyncio program
asyncio.run(main())

