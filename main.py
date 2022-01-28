import random
import string
import urllib.request
from concurrent.futures import wait, ThreadPoolExecutor
import requests
import os, sys
from random import randint
from bs4 import BeautifulSoup
from cloudscraper import create_scraper

scraper = create_scraper()

try:
    os.mkdir("screenshots")
except:
    pass


def gen_link():
    letters = list(string.ascii_lowercase)
    link_point = random.choice(letters) + random.choice(letters) + str(randint(1000, 9999))
    print(link_point)
    return link_point


def down_rand_img():
    rand_link = "https://prnt.sc/" + gen_link()
    res = scraper.get(rand_link)
    soup = BeautifulSoup(res.text, "html.parser")
    print(res.status_code)
    if res.status_code == 200:
        img_link = soup.find("img", {'class': 'no-click screenshot-image'})['src']
        if img_link[:2] == "//":
            img_link = "http:" + img_link
        with scraper.get(img_link) as data:
            print(data.status_code)
            if data.status_code==200:
                print(data)
                with open(os.path.join("screenshots", f"{randint(1, 1000000)}.png"), "wb") as file:
                    file.write(data.content)
            print(img_link)


futures = []
pool = ThreadPoolExecutor(4)
for i in range(1000):
    futures.append(pool.submit(down_rand_img))
wait(futures)