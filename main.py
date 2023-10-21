import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json
import datetime

username = 'MrQui3'
session = HTMLSession()

begin = datetime.datetime.now()

user_json = json.load(open('users.json'))
users = {}

def get_user_info(username, number):
    global users
    if number == 4 or username in users:
        return 0
    else:
        page = session.get('https://github.com/' + username + '?tab=followers')
        soup = BeautifulSoup(page.content, 'html.parser')

        follower_number = 0
        following_number = 0

        follower_N_following = soup.find_all(class_="text-bold color-fg-default")

        if len(follower_N_following) != 0:
            follower_number = follower_N_following[0].text
            if 'k' in follower_number:
                follower_number = float(follower_number[:-1]) * 1000
            follower_number = int(follower_number)

            following_number = follower_N_following[1].text
            if 'k' in following_number:
                following_number = float(following_number[:-1]) * 1000
            following_number = int(following_number)


        users[username] = {'follower': follower_number, 'following':  following_number}

        followers = []
        if follower_number > 50:
            follower_number = 49
        for i in range(follower_number):
            try:
                follower_name = soup.find_all(class_="Link--secondary")[-(i + 1)].text
                followers.append(follower_name)
                get_user_info(follower_name, number + 1)
            except:
                print(username)
                print([-(i + 1)])
                follower_name = soup.find_all(class_="Link--secondary")[-(i + 1)].text

        return followers





result = get_user_info(username, 0)



json.dump(users, open('users.json', 'w'))
print('finished')
print(len(users))

print("Time taken: ", datetime.datetime.now() - begin)
