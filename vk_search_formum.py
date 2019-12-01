# http://www.cyberforum.ru/python-network/thread2230824.html
import csv

import requests


def take_posts():
    token = 'cc43febfcc43febfcc43febf6fcc2903e6ccc43cc43febf90bafff932fd3f1f213bddc8'
    version = 5.95
    domain = 'vershkoff_ru'
    count = 100
    offset = 0
    all_posts = []

    while offset < 150:
        response = requests.search('https://api.vk.com/method/wall.search',
                                   params={
                                       'access_token': token,
                                       'v': version,
                                       'domain': domain,
                                       'count': count,
                                       'offset': offset,
                                       'query': 'студия акция',
                                   })
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    with open('vk_parsing.csv', 'w') as file:
        a_pen = csv.writer(file, delimiter=';')
        a_pen.writerow(('likes', 'body', 'url'))
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'

            except:
                pass
        a_pen.writerow((post['likes']['count'], post['text'], img_url))


all_posts = take_posts()
file_writer(all_posts)