import matplotlib.pyplot as plt
import os, re, math
def clearData(line):
    line = re.sub('.*Range: ', '', line)
    line = re.sub(' m.*', '', line)
    return line

def get_old_mbe_plotable(get_rmsy=False):

    dalmierze = []
    mbry = []
    rmsy = []

    files = os.listdir(os.getcwd() + "\\pomiary_mbe_stare")

    for filename in files: #dla każdego pomiaru dalmirzowego
        if "txt" in filename:
            sigma = 0
            sigmaKwadrat = 0
            wartOczekiwana = float(re.sub('.txt', '', filename))
            dalmierze.append(wartOczekiwana)
            with open(os.path.join(os.getcwd() + "\\pomiary_mbe_stare", filename), 'r') as f:
                n = 0
                print(f)
                for line in f.readlines(): #pomiary z uwb
                    print(line)
                    if line != '':
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
    if get_rmsy:
        return(dalmierze, rmsy)
    return (dalmierze, mbry)

if __name__ == '__main__':
    plotable = get_old_mbe_plotable()
    plt.ylabel('mean bias error')
    plt.ylabel('mbe')
    plt.xlabel('odległość')
    plt.plot(plotable[0], plotable[1])
    plt.show()

    plotable = get_old_mbe_plotable(get_rmsy=True)
    plt.ylabel('root mean square error')
    plt.xlabel('odległość')
    plt.plot(plotable[0], plotable[1])
    plt.show()