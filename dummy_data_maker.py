import csv
import argparse
import psutil
from datetime import datetime

parser = argparse.ArgumentParser(description="profile")
parser.add_argument("--name", "-n", type=str, default="None", help="pc_name")
parser.add_argument("--directory", "-d", type=str, default="None", help="output file directory")
args = parser.parse_args()
print(args.name, args.directory)

with open(args.directory + "{0}.csv".format(args.name), "a") as f:
    csv_writer = csv.writer(f)

    for num in range(50):
        now_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                psutil.cpu_percent(interval=1),
                psutil.virtual_memory().percent
                ]
        csv_writer.writerow(line)
