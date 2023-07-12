# example of getting the current task from the main coroutine
import asyncio
import time 
# define a main coroutine
async def main():
    # report a message 
    print(f"{time.ctime()} main coroutine started")
    # get the current task
    task = asyncio.current_task()
    # report its details
    print(f"{time.ctime()} {task} ")

# start the asyncio program
asyncio.run(main())

#
# Wed Jul 12 14:18:58 2023 main coroutine started
# Wed Jul 12 14:18:58 2023 <Task pending name='Task-1' coro=<main() running at d:\Asynchronous\12-7-2566\2_asyncio.py:11> cb=[_run_until_complete_cb() at C:\Users\pongt\AppData\Local\Programs\Python\Python311\Lib\asyncio\base_events.py:180]>
#