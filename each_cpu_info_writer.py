import csv
import argparse
import psutil
from datetime import datetime

parser = argparse.ArgumentParser(description="profile")
parser.add_argument("--name", "-n", type=str, default="None", help="pc_name")
args = parser.parse_args()
print(args.name)

# this should be appropriately modified
directory_name = ""

with open(directory_name + "{0}.csv".format(args.name), "a") as f:
    csv_writer = csv.writer(f)
    now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            psutil.cpu_percent(interval=0.5),
            psutil.virtual_memory().percent
    ]
    csv_writer.writerow(line)
    print(now_string, psutil.cpu_percent(interval=0.5), psutil.virtual_memory().percent)
