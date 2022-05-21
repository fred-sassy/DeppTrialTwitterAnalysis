import requests 
import csv
import datetime as dt

BEARER_TOKEN = '<mytoken>'

url = 'https://api.twitter.com/2/tweets/counts/recent'  # use twitter's 'recent' endpoint to avoid paying for this stuff
headers = {'Authorization': f'Bearer {BEARER_TOKEN}'}   # replace <mytoken> with bearer token

start_date = (dt.date.today() - dt.timedelta(days=6)).isoformat()
params = {
    'start_time': f'{start_date}T00:00:00.00Z',     # start 6 days ago to stay within free 'recent' date limits
    'end_time': f'{dt.date.today()}T00:00:00.00Z',  # end at midnight today
    'granularity': 'hour'                           # pull hourly instead of daily because we can only get 6 days of data
}

def pull_totals(hashtag):
    """ Get hourly totals for one hashtag for the last 6 days """
    # Update parameters to search for specific hashtag and 
    params['query'] = f'#{hashtag}'
    response = requests.get(url, headers=headers, params=params)
    json = response.json()
    
    # Take necessary info from each row, add date/hour fields, and add to result list
    data = []
    for row in json['data']:
        data.append({
            'hashtag': hashtag,
            'start_time': row['start'],
            'tweets': row['tweet_count'],
            'date': row['start'][:10],
            'hour': row['start'][11:13]
        })
    return data

# Pull hourly tweet counts for each hashtag and put them in one list
all_data = []
for hashtag in ['AmberTurd', 'JusticeforJohnnyDepp', 'AmberHeardIsAnAbuser', 'AmberHeardIsALiar', 'JohnnyDeppIsInnocent']:
    all_data.extend(pull_totals(hashtag))

# Write results to csv to copy/paste into spreadsheet
with open('tweet_counts2.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, all_data[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(all_data)
