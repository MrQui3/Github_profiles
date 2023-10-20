import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = 'https://github.com/test'

session = HTMLSession()
page1 = session.get(url)

soup1 = BeautifulSoup(page1.content, 'html.parser')


follower = soup1.find_all(class_="text-bold color-fg-default")[0].text
following = soup1.find_all(class_="text-bold color-fg-default")[1].text

print(f'Follower: {follower}, Following: {following}')