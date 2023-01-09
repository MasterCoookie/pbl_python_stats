import matplotlib.pyplot as plt
import os, re, math

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

    for filename in files: #dla każdego pomiaru dalmirzowego
        if "txt" in filename:
            delay= float(re.sub('ms.txt', '', filename)[len(dist) + 1:])
            dealys.append(delay)
            path = os.path.join(os.getcwd() + mesurements_path_dist, filename)
            with open(path, 'r') as f:
                # n = 
                timeout_count = 0
                print(f)
                for line in f.readlines(): #pomiary z uwb
                    print(line)
                    if line != '':
                        # n += 1
                        # pomiar = float(clearData(line).strip())
                        # pomiar = line[10:]
                        # delta=pomiar-wartOcekiwana
                        # deltaKwadrat = delta * delta
                        if line.strip() == "Timed out!":
                            timeout_count += 1

                timeouts.append(timeout_count)
            

    #     sigma += delta
    #     sigmaKwadrat += deltaKwadrat
    # mbr = sigma / n
    # rmse = math.sqrt(sigmaKwadrat / n)
    # dalmierze.sort()
    # mbry.insert(dalmierze.index(wartOczekiwana), mbr)
    # rmsy.insert(dalmierze.index(wartOczekiwana), rmse)

# plt.ylabel('min bias error')
# plt.ylabel('mbr')
# plt.xlabel('odległość')    
# plt.plot(dalmierze, mbry)

    plt.plot(dealys, timeouts, label=("Distance " + dist))

plt.legend()
plt.show()

#with open(os.path.join(os.getcwd(), "3.978.txt"), 'r') as f:
#   wyniki = []
#   for line in f.readlines():
#      wyniki.append(float(clearData(line).strip()))

#plt.plot(wyniki)
#plt.show()
