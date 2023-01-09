import matplotlib.pyplot as plt
import os, re

def clearData(line):
    line = re.sub('.*Range: ', '', line)
    line = re.sub(' m.*', '', line)
    return line


distances = ["20", "55", "100"]

plt.ylabel("Number of timeouts per 100 frames")
plt.xlabel("Delay (ms)")

mesurements_path = "\\pomiary\\pomiary"

for dist in distances:
    dealys = []
    timeouts = []
    mesurements_path_dist = mesurements_path + dist

    files = sorted(os.listdir(os.getcwd() + mesurements_path_dist))
    files.append(files.pop(0))

    for filename in files:
        if "txt" in filename:
            delay= float(re.sub('ms.txt', '', filename)[len(dist) + 1:])
            dealys.append(delay)
            path = os.path.join(os.getcwd() + mesurements_path_dist, filename)
            with open(path, 'r') as f:
                timeout_count = 0
                print(f)
                for line in f.readlines():
                    print(line)
                    if line != '':
                        if line.strip() == "Timed out!":
                            timeout_count += 1

                timeouts.append(timeout_count)


    plt.plot(dealys, timeouts, label=("Distance " + dist))

plt.legend()
plt.show()
