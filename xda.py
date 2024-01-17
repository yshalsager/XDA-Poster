"""
Copyright © 2019 Maestro Creativescape
SPDX-License-Identifier: GPL-3.0
authors: @baalajimaestro, @yshalsager
"""

from httpx import AsyncClient, Client, Response


class XDA:
    """XDA API client"""

    def __init__(self, api_key: str):
        self.url = "https://xdaforums.com/api"
        self.api_key = api_key
        self.headers = {
            'XF-Api-Key': self.api_key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self._timeout = 10
        self._client = Client(http2=True, timeout=self._timeout)
        self._async_client = lambda: AsyncClient(http2=True, timeout=self._timeout)

    def post(self, thread_id: int, message: str):
        """
        Post XDA post to a thread
        :param message: reply text
        :param thread_id: XDA thread id
        """
        xda_req = self._client.post(f'{self.url}/posts', data={"thread_id": thread_id, "message": message},
                                    headers=self.headers)
        if not xda_req.status_code == 200:
            print(f"XDA Error: {xda_req.reason_phrase}\nResponse: {xda_req.text}")

    def update_post(self, post_id: int, message: str):
        """
        Update an XDA post
        :param message: post text
        :param post_id: XDA post id
        """
        xda_req = self._client.post(f'{self.url}/posts/{post_id}', data={"message": message}, headers=self.headers)
        if not xda_req.status_code == 200:
            print(f"XDA Error: {xda_req.reason_phrase}\nResponse: {xda_req.text}")

    async def post_async(self, thread_id: int, message: str):
        """
        Post XDA post to a thread asynchronously
        :param message: reply text
        :param thread_id: XDA thread id
        """
        async with self._async_client() as client:
            resp: Response = await client.post(
                f'{self.url}/posts', data={"thread_id": thread_id, "message": message},
                headers=self.headers)
            if not resp.status_code == 200:
                print(f"XDA Error: {resp.reason_phrase}\nResponse: {resp.text}")

    async def update_post_async(self, post_id: int, message: str):
        """
        Update an XDA post asynchronously
        :param message: post text
        :param post_id: XDA thread id
        """
        async with self._async_client() as client:
            resp: Response = await client.post(
                f'{self.url}/posts/{post_id}', data={"message": message},
                headers=self.headers)
            if not resp.status_code == 200:
                print(f"XDA Error: {resp.reason_phrase}\nResponse: {resp.text}")
