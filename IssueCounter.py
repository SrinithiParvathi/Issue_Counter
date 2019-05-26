import csv
import requests
from datetime import datetime
from flask import json
import json
result = 0
BASE_URL = 'https://api.github.com/repos/'                                                      #its a base url to fetch open issuses from github 
END_POINT = '/issues'
total = 0




# Function to fetch result based on input url

def hit_url(url):
    REQUEST_URL = BASE_URL + url + END_POINT                                                     #url is the input link from which issues has to be fetched
    print(REQUEST_URL)
    response = requests.get(REQUEST_URL)
    count = write_issues(response)

    if 'link' in response.headers:                                                              #if there are more than one page
        pages = {rel[6:-1]: url[url.index('<') + 1: -1] for url, rel in
                 (link.split(';') for link in
                  response.headers['link'].split(','))}
        while 'last' in pages and 'next' in pages:
            pages = {rel[6:-1]: url[url.index('<') + 1: -1] for url, rel in
                     (link.split(';') for link in
                      response.headers['link'].split(','))}

            response = requests.get(pages['next'])
            result = write_issues(response)                                                      #call write_issues - the response for the request 
            count += result
            if pages['next'] == pages['last']:
                break
    return result
	
	

# Function to process the response object parse it and counts the open issuses based on different filter

def write_issues(response):
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    global total
    if response.status_code != 200:
        raise Exception(response.status_code)                                                  #if status code is not 200 exception is raised else response for issues is processed
    for issue in response.json():
        if 'pull_request' not in issue:
            labels = ', '.join([l['name'] for l in issue['labels']])
            issue_created_at = issue['created_at']
            issue_time = issue_created_at.split('T')[0]
            someday = datetime.strptime(issue_time, '%Y-%m-%d').date()
            today = datetime.now().date()
            difference = today - someday                                                        #we calculate the open issues based one the filter (less tahn 24 hrs more tham  a week etc)

            if(difference.days < 1):
                count1 = count1 + 1
            elif (difference.days < 7 and difference.days > 1):
                count2 = count2 + 1
            elif(difference.days > 7):
                count3 = count3 + 1
            count += 1
    total += count
    result = json.dumps({'Less than 24hrs': count1, 'More than 24hrs Less than week': count2,      # here we return an json object wih the counts to hit_url_url
                         'More than 7 days': count3, 'Total count': total})
    return result
