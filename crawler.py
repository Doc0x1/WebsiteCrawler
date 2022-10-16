import os
from bs4 import BeautifulSoup
import aiohttp
import asyncio
import pandas as pd
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque

class SiteDirectoryCrawler(object):
    def __init__(self, urls):
        self.all_crawled_urls = []
        self.master_dict = {}
        self.urls = urls
        asyncio.run(self.main())

    async def fetch(self, session, url):
        try:
            async with session.get(url) as resp:
                text = await resp.text()
                return text, url
        except Exception as e:
            print(str(e))

        if("Request timed out." or "unreachable") in resp:
            print(f"{resp} is down")
            f = open("ip_down_links.txt", "a")
            f.write(str(resp) + "\n")
            f.close()
        else:
            print(f"{resp} is up")
            f = open("ip_up_links.txt", "a")
            f.write(str(resp) + "\n")
            f.close()


    def crawl_site(self, url):
        self.urls_processed = set()  # set of urls that we have already crawled
        self.urls_local = set()
        self.urls_foreign = set()
        self.urls_broken = set()


    async def main():
        tasks = []
