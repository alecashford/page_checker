import csv
# import urllib2, sys
import requests
import json
import time
import re
from functools import wraps
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/FairAndBalanced/"
keyword = "testpostpleaseignore"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

key = 'key-2yysjtw83re60djtlw22w4flfnyl8wt1'
sandbox = 'sandboxfac2f1ef29a84995bb38573a3c2b060d.mailgun.org'
recipient = 'ashford91@gmail.com'

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
else:
    print('Not found')

# def make_http_request(url):
#     hdr = {'User-Agent': 'Mozilla/5.0'}
#     req = urllib2.Request(url, headers=hdr)
#     page = urllib2.urlopen(req)
#     return page

# def get_soup_from_url(url):
#     page = make_http_request(url)
#     return BeautifulSoup(page)

# def true_if_keyword_on_page(url, keyword):
#     soup = get_soup_from_url(url)
#     soup.html.find_all(text=re.compile(r'testpostpleaseignore', re.IGNORECASE), recursive=True)

# def main():
#     # iterate_through_every_gd_page()
#     # DO STUFF
#     print(true_if_keyword_on_page(url, keyword))

# if __name__== "__main__":
#   main()
