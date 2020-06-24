"""
Copyright © 2019 Maestro Creativescape
SPDX-License-Identifier: GPL-3.0
authors: @baalajimaestro, @yshalsager
"""

import json
import re
from os import environ

from requests import get, post
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

XDA_USERNAME = environ['XDA_USERNAME']
XDA_PASSWORD = environ['XDA_PASSWORD']


class XDA:
    """XDA API client"""

    def __init__(self):
        self.api_key = self.get_api_key()

    @staticmethod
    def get_api_key():
        """Get XDA API key using selenium"""
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Firefox(options=firefox_options)
        wait = WebDriverWait(driver, 60)
        # Grab the current window
        main_window_handle = None
        while not main_window_handle:
            main_window_handle = driver.current_window_handle
        driver.get("http://api.xda-developers.com/explorer/")
        wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="login_btn"]'))).click()
        # Swap to signin window
        signin_window_handle = None
        while not signin_window_handle:
            signin_window_handle = [handle for handle in driver.window_handles
                                    if handle != main_window_handle][0]
            break
        driver.switch_to.window(signin_window_handle)
        wait.until(ec.presence_of_element_located((By.XPATH, '//form[@id="login"]')))
        username = driver.find_element_by_name("username")
        password = driver.find_element_by_name("password")
        username.send_keys(XDA_USERNAME)
        password.send_keys(XDA_PASSWORD)
        driver.find_element_by_id("signin-submit").click()
        wait.until(ec.presence_of_element_located((By.XPATH, '//input[@id="authorize"]'))).click()
        # Come back to main window
        driver.switch_to.window(main_window_handle)
        api_key_text = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="message-bar"]'))).text
        # Scrape out the API Key
        try:
            api_key = re.search(r'Access token: ([a-z0-9]+)', api_key_text).group(1)
        except IndexError:
            raise Exception("Could not get the API key!")
        driver.quit()
        return api_key

    @staticmethod
    def get_post_id(thread_id):
        """Get post ID from xda thread"""
        return get("https://api.xda-developers.com/v3/posts",
                   params={"threadid": thread_id}
                   ).json()["results"][0]["postid"]

    def post(self, xda_post_id, xda_post):
        """Post XDA post to a thread"""
        data = {"postid": xda_post_id, "message": xda_post}
        headers = {
            'origin': 'https://api.xda-developers.com',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer ' + self.api_key,
            'x-requested-with': 'XMLHttpRequest',
            'content-type': 'application/json',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'referer': 'https://api.xda-developers.com/explorer/',
            'authority': 'api.xda-developers.com',
            'sec-fetch-site': 'same-origin',
        }
        xda_req = post('https://api.xda-developers.com/v3/posts/new',
                       data=json.dumps(data), headers=headers)
        if not xda_req.status_code == 200:
            print("XDA Error")
            print(xda_req.reason)
