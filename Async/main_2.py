import asyncio

"""
from requests import Session
from time import sleep

def get_response():
    with Session() as session:
        response = session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"

        )
        
        #print(response.json())
        #print(response.text)
        #print(response.cookies)
        #print(response.url)
        #print(response.status_code)
"""

#for i in  range(10):
 #   get_response()

from aiohttp import ClientRequest, ClientSession


class Alpha:

    @staticmethod
    @create_async_session
    async def get_response():
        async with ClientSession() as session:
        response = await session.get(
            url="https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates"
        )
        await asyncio.sleep(3)
        print(response.status)

async def main():
    loop = asyncio.get_running_loop()
    tasks = [loop.create_task(get_response()) for i in range(10)]
    for task in tasks:
        await task

asyncio.run(main())




"""
from crud import CRUDCategory

async def main():
    res = await CRUDCategory.get.all()
    print(res)




async def foo():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)


async def main():
    loop = asyncio.get_running_loop()
    task = [loop.create_task(foo()) for i in range(10)]
    for task in task:
        await task


if __name__ == '__main__':
    #asyncio.set_event_loop_policy(acyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

"""

