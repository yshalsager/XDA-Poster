"""
Copyright © 2019 Maestro Creativescape
SPDX-License-Identifier: GPL-3.0
authors: @baalajimaestro, @yshalsager
"""

from requests import post
from aiohttp import ClientSession


class XDA:
    """XDA API client"""

    def __init__(self, api_key):
        self.url = "https://forum.xda-developers.com/api"
        self.api_key = api_key
        self.headers = {
            'XF-Api-Key': self.api_key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def post(self, thread_id, message):
        """
        Post XDA post to a thread
        :param message: reply text
        :type message: str
        :param thread_id: XDA thread id
        :type thread_id: int
        """
        xda_req = post(f'{self.url}/posts', data={"thread_id": thread_id, "message": message}, headers=self.headers)
        if not xda_req.status_code == 200:
            print(f"XDA Error: {xda_req.reason}")

    async def post_async(self, thread_id, message):
        """
        Post XDA post to a thread asynchronously
        :param message: reply text
        :type message: str
        :param thread_id: XDA thread id
        :type thread_id: int
        """
        async with ClientSession() as session:
            async with session.post(
                    f'{self.url}/posts', data={"thread_id": thread_id, "message": message},
                    headers=self.headers) as resp:
                if not resp.status == 200:
                    print(f"XDA Error: {resp.reason}")
