import requests
import argparse

parser = argparse.ArgumentParser(description="profile")
parser.add_argument("--filepath", "-fp", type=str, default="None", help="output file directory")
args = parser.parse_args()

accessToken = ""
channelId = ""
files = {"file": open(args.filepath, "rb")}

param = {'token': accessToken, 'channels': channelId}
res = requests.post(url="https://slack.com/api/files.upload", params=param, files=files)
