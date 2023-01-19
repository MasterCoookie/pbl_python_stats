import matplotlib.pyplot as plt
import os, re, math

def clearData(line):
    # line = re.sub('.*Range: ', '', line)
    # line = re.sub(' m.*', '', line)
    return line[10:]

dalmierze = []
mbry = []
rmsy = []

files = os.listdir(os.getcwd() + "\\pomiary_range")

for filename in files: #dla każdego pomiaru dalmirzowego
   if "txt" in filename:
    sigma = 0
    sigmaKwadrat = 0
    wartOczekiwana = float(re.sub('m.txt', '', filename))
    dalmierze.append(wartOczekiwana)
    with open(os.path.join(os.getcwd() + "\\pomiary_range", filename), 'r') as f:
        n = 0
        print(f)
        for line in f.readlines(): #pomiary z uwb
            print(line)
            if line != '' and line != "Timed out!\n":
                n += 1
                pomiar = float(clearData(line).strip())
                delta=pomiar-wartOczekiwana
                deltaKwadrat = delta * delta
        sigma += delta
        sigmaKwadrat += deltaKwadrat
    mbr = sigma / n
    rmse = math.sqrt(sigmaKwadrat / n)
    dalmierze.sort()
    mbry.insert(dalmierze.index(wartOczekiwana), mbr)
    rmsy.insert(dalmierze.index(wartOczekiwana), rmse)

plt.ylabel('min bias error')
plt.ylabel('mbr')
plt.xlabel('odległość')    
plt.plot(dalmierze, mbry)
plt.show()