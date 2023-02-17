import matplotlib.pyplot as plt
import os, re, math
from mbe_old import get_old_mbe_plotable

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

plt.ylabel('mean bias error')
plt.xlabel('distance [m]')    
plt.plot(dalmierze, mbry, 'g' , label="DW1000 SPGH")
plotable = get_old_mbe_plotable()
plt.plot(plotable[0], plotable[1], 'r', label="DW1000")
plt.legend()
plt.show()


plt.ylabel('root mean square error')
plt.xlabel('distance [m]')    
plt.plot(dalmierze, rmsy, 'g' , label="DW1000 SPGH")
plotable = get_old_mbe_plotable(get_rmsy=True)
plt.plot(plotable[0], plotable[1], 'r', label="DW1000")
plt.legend()
plt.show()

rmsy_avg_dw1000 = (sum(plotable[1]) / len(plotable[1]))
print(f"AVG RMSY DW1000: {rmsy_avg_dw1000}")

rmsy_avg_dw1000SPGH = (sum(rmsy) / len(rmsy))
print(f"AVG RMSY DW1000SPGH: {rmsy_avg_dw1000SPGH}")