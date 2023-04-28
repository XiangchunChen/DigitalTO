import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    labels=[2,4,6,8]
    data = pd.DataFrame({'LE': [1.0, 1.0, 1.0,1.0], 'Random': [   59 / 280.0,54 / 280.0 ,48 / 280.0, 44 / 280.0], 'DQN': [31 / 280.0, 31 / 280.0, 31 / 280.0, 31 / 280.0],
                         'Greedy': [34 / 280.0, 35 / 280.0, 34 / 280.0, 33 / 280.0], 'ADPRL': [65 / 280.0,65 / 280.0, 65 / 280.0, 65 / 280.0],
                         'class1': [0, 0, 0, 0], 'class2': [221 / 280.0,226 / 280.0 ,232 / 280.0, 236 / 280.0], 'class3': [249 / 280.0, 249 / 280.0, 249 / 280.0, 249 / 280.0],
                         'class4': [246 / 280.0, 245 / 280.0, 246 / 280.0, 247 / 280.0], 'class5': [215 / 280.0,215 / 280.0, 215 / 280.0, 215 / 280.0]},
                        index=labels)
    menStd = (2, 30, 40)
    womenStd = (30, 50, 20)
    x = np.arange(2,10,2, dtype=int)  # the label locations
    width = 0.4  # the width of the bars
    # plt.figure(figsize=(50,40))
    lwidth = 10
    rects1 = plt.bar(x - width*2, data['class1'], width, alpha=0.8,color="w",edgecolor="k",
                     bottom=data['LE'], label='LE')

    rects2 = plt.bar(x - width, data['class2'],  width,  alpha=0.8,color="w",edgecolor="k",hatch=".....",
                     bottom=data['Random'], label='Random')
    rects3 = plt.bar(x, data['class3'], width, alpha=0.8,color="w",edgecolor="k",hatch="o",
                     bottom=data['DQN'], label='DQN+FCFS')
    rects4 = plt.bar(x + width, data['class4'],  width,  alpha=0.8,color="w",edgecolor="k",hatch="/",
                     bottom=data['Greedy'], label='Greedy')
    rects5 = plt.bar(x + width*2,data['class5'],  width,  alpha=0.8,color="w",edgecolor="k",hatch="//",
                     bottom=data['ADPRL'], label='ADPRL')
    # Add some text for labels, title and custom x-pltis tick labels, etc.
    print('LE')
    print(data['class1'])
    print('Random')
    print(data['class2'])
    print('DQN')
    print(data['class3'])
    print('Greedy')
    print(data['class4'])
    print('ADPRL')
    print(data['class5'])

    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(lwidth)
    ax.spines['left'].set_linewidth(lwidth)
    ax.spines['right'].set_linewidth(lwidth)
    plt.ylim(0.0, 2)
    plt.ylabel('Offloading proportion')
    plt.xlabel('f) Bandwidth (Synthetic DAGs)')
    plt.yticks()
    plt.legend()
    plt.savefig('rbandwidthOP.pdf', dpi=120, bbox_inches='tight')
    plt.show()
