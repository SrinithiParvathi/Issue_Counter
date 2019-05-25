import csv
import requests
from datetime import datetime
from flask import json
import json
x = 0

#GITHUB_USER = 'SrinithiParvathi'
#GITHUB_PASSWORD = 'Welcome12326'
# REPO = 'hunspell/hunspell'  # format is username/repo
# ISSUES_FOR_REPO_URL = 'https://api.github.com/repos/%s/issues' % REPO
#auth = None
#AUTH = (GITHUB_USER, GITHUB_PASSWORD)
BASE_URL = 'https://api.github.com/repos/'
END_POINT = '/issues'

def hit_url(url):
    REQUEST_URL =  BASE_URL + url + END_POINT
    print(REQUEST_URL)
    response = requests.get(REQUEST_URL)
    #csvout.writerow(('id', 'Title', 'Body', 'Created At', 'Updated At'))
    count = write_issues(response)

    if 'link' in response.headers:
        pages = {rel[6:-1]: url[url.index('<') +1 : -1] for url, rel in
                (link.split(';') for link in
                response.headers['link'].split(','))}
        while 'last' in pages and 'next' in pages:
            pages = {rel[6:-1]: url[url.index('<') +1 : -1] for url, rel in
                 (link.split(';') for link in
                  response.headers['link'].split(','))}

            print(response.headers['link'])
            response = requests.get(pages['next'])
            x = write_issues(response)
            count += x
            if pages['next'] == pages['last']:
                break
    return x
    
def write_issues(response):
    count = 0
    Listless_7 = list()
    List2 = list()
    List3 = list()
    count1 = 0
    count2 = 0
    count3 = 0
    """Parses JSON response and writes to CSV."""
    if response.status_code != 200:
        raise Exception(response.status_code)
    for issue in response.json():
        if 'pull_request' not in issue:
            labels = ', '.join([l['name'] for l in issue['labels']])
            #print(issue['url'])
            issue_created_at = issue['created_at']
            issue_time = issue_created_at.split('T')[0]
            someday = datetime.strptime(issue_time, '%Y-%m-%d').date()
            today = datetime.now().date()
            difference = today - someday
            print(difference.days)

            if(difference.days < 1):
                count1 = count1 + 1
                Listless_7.append(issue['url'])
            elif (difference.days < 7 and difference.days > 1) :
                count2 = count2 + 1
                List2.append(issue['url'])
            elif(difference.days > 3200):
                count3 = count3 + 1
                List3.append(issue['url'])
            count += 1

    print(count1)
    print(count2)
    print(count3)

    result = json.dumps({'count_1': count1, 'count_2': count2, 'count_3': count3})
    print(result)
    return result
            # Change the following line to write out additional fields
