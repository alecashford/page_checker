import requests
import json
import time
from bs4 import BeautifulSoup
import re
import sys
from secrets import *

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def check_page(url, keyword):
    page_response = requests.get(url, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    results = page_content.find_all(text=re.compile(r'{}'.format(keyword), re.IGNORECASE), recursive=True)

    keyword_matched = len(results) > 0

    if keyword_matched:
        request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
        request = requests.post(request_url, auth=('api', key), data={
            'from': 'hello@example.com',
            'to': recipient,
            'subject': 'Match found!',
            'text': 'Log on to check for match :)\n\n{}'.format(url)
        })
        print('Status: {0}'.format(request.status_code))
        print('Body:   {0}'.format(request.text))
        sys.exit()

def main():
    url = input("Enter the URL you'd like the check: ")
    keyword = input("Enter the keyword you'd like to check the URL for: ")
    frequency = int(input("How often do you want to check (in minutes): "))

    tries = 0
    while True:
        check_page(url, keyword)
        tries += 1
        if tries % 10 == 0:
            print("Tried {} times so far".format(tries))
        time.sleep(frequency * 60)


if __name__ == '__main__':
    main()
