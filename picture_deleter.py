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
max_count = 1000
data_list = {'token': access_token, 'channels': channel_id, "ts_to": ts_to, 'ts_from': ts_from, 'count': max_count}

counter = 0
while True:
    try:
        print("counter", counter)

        file_list_response = requests.post(url=files_list_url, data=data_list)
        files = file_list_response.json()['files']
        # if len(files) == 0:
        #     print("nothing")
        if len(files) < 50:
            print("not enough: ", len(files))
            time.sleep(20)

        else:
            print("file length / count  : {0} / {1}".format(len(files), max_count))
            for file_index, f in tqdm(enumerate(files), total=len(files)):
                if f['name'] == "latest.png":
                    data_delete = {'token': access_token, 'file': f['id']}
                    delete_request_response = requests.post(url=delete_url, data=data_delete)
                    if not delete_request_response.json()['ok']:
                        print("delete request failed")
                        print(delete_request_response.json())
                        print(f['name'])
                        print()
                    time.sleep(0.8)
                if file_index > 300:
                    break
            counter += 1
            # print("sleeping...", datetime.now())
            # time.sleep(150)
    except Exception as e:
        print(e)
