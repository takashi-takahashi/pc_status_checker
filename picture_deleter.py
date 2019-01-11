import time
import requests
import calendar
from datetime import datetime, timedelta
from tqdm import tqdm

access_token = ""
channel_id = ""

files_list_url = 'https://slack.com/api/files.list'
delete_url = 'https://slack.com/api/files.delete'
ts_from = str(calendar.timegm((datetime.now() + timedelta(days=-365)).utctimetuple()))
ts_to = str(calendar.timegm((datetime.now() + timedelta(days=-1)).utctimetuple()))
count = 100
data_list = {'token': access_token, 'channels': channel_id, "ts_to": ts_to, 'ts_from': ts_from, 'count': count}

counter = 0
while True:
    print("counter", counter)
    counter += 1

    file_list_response = requests.post(url=files_list_url, data=data_list)
    files = file_list_response.json()['files']
    if len(files) == 0:
        print("nothing")
        break

    else:
        print("file length / count  : {0} / {1}".format(len(files), count))
        for file_index, f in tqdm(enumerate(files), total=len(files)):
            if f['name'] == "latest.png":
                data_delete = {'token': access_token, 'file': f['id']}
                delete_request_response = requests.post(url=delete_url, data=data_delete)
                if not delete_request_response.json()['ok']:
                    print("delete request failed")
                    print(delete_request_response.json())
                    print(f['name'])
                    print()
                time.sleep(1)
    print("sleeping...", datetime.now())
    time.sleep(60)
_