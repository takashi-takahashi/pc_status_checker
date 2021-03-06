import csv
import argparse
from datetime import datetime
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="profile")
parser.add_argument("--directory", "-d", type=str, default="None", help="output file directory")
args = parser.parse_args()

calculator_name_list = ["calc01",
                        "calc02",
                        "calc03",
                        "calc04",
                        "calc05",
                        "calc06"
                        ]

# read data
data_dictionary = {}
for calculator_name in calculator_name_list:
    with open(args.directory + calculator_name + ".csv", "r") as f:
        csv_reader = csv.reader(f)
        data_dictionary[calculator_name] = []
        for index, line in enumerate(csv_reader):
            data_dictionary[calculator_name].append(line)
        data_dictionary[calculator_name] = data_dictionary[calculator_name][-50:]

# plot data
fig = plt.figure(figsize=(9, 5))
ax_cpu = fig.add_subplot(2, 1, 1)
ax_memory = fig.add_subplot(2, 1, 2)
for key in data_dictionary.keys():
    time_list = []
    cpu_percent_list = []
    memory_percent_list = []
    for line in data_dictionary[key]:
        time_list.append(datetime.strptime(line[0], "%Y-%m-%d %H:%M:%S"))
        cpu_percent_list.append(float(line[1]))
        memory_percent_list.append(float(line[2]))

    # cpu usage
    ax_cpu.plot(time_list, cpu_percent_list, "-o", ms=5, label=key, alpha=0.75)

    # memory usage
    ax_memory.plot(time_list, memory_percent_list, "-d", ms=5, label=key, alpha=0.75)

now = datetime.now()

ax_cpu.set_xlabel("time")
ax_cpu.set_ylabel("cpu[%]")
ax_cpu.set_title("cpu usage[%]")
ax_cpu.grid()
ax_cpu.legend(loc="right")
ax_cpu.set_ylim(0, 100)
diff = max(time_list) - min(time_list)
ax_cpu.set_xlim(xmin=min(time_list), xmax=max(time_list) + diff * 0.2)

ax_memory.grid()
ax_memory.legend(loc="right")
ax_memory.set_xlabel("time")
ax_memory.set_ylabel("memory[%]")
ax_memory.set_title("memory usage[%]")
ax_memory.set_ylim(0, 100)
diff = max(time_list) - min(time_list)
ax_memory.set_xlim(xmin=min(time_list), xmax=max(time_list) + diff * 0.2)

fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(args.directory + "latest.png", format="png", dpi=150)
# plt.show()
