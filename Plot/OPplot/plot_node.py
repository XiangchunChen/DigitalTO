import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    labels=[25,50,75,100]
    data = pd.DataFrame({'LE': [1.0, 1.0, 1.0,1.0], 'Random': [   13 / 68.0, 11 / 68.0 ,9 / 68.0, 9 / 68.0], 'DQN': [7 / 68.0, 7 / 68.0, 7 / 68.0, 7 / 68.0],
                         'Greedy': [5 / 68.0, 4 / 68.0, 1 / 68.0, 0 / 68.0], 'ADPRL': [3 / 68.0,2 / 68.0, 1 / 68.0, 1 / 68.0],
                         'class1': [0, 0, 0, 0], 'class2': [55 / 68.0,57 / 68.0 ,59 / 68.0, 59 / 68.0], 'class3': [61 / 68.0, 61 / 68.0, 61 / 68.0, 61 / 68.0],
                         'class4': [63/68, 64/68, 67/68, 68/68], 'class5': [65 / 68.0,66 / 68.0, 67 / 68.0, 67 / 68.0]},
                        index=labels)
    menStd = (2, 30, 40)
    womenStd = (30, 50, 20)
    x = np.arange(10,50,10, dtype=int)  # the label locations
    width = 2  # the width of the bars
    ls = ['LE','Random','DQN','Greedy','ADPRL']


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
    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_title('Scores by group and gender')
    # print('LE')
    # print(data['class1'])
    # print('Random')
    # print(data['class2'])
    # print('DQN')
    # print(data['class3'])
    # print('Greedy')
    # print(data['class4'])
    # print('ADPRL')
    # print(data['class5'])

    lwidth = 10
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(lwidth)
    ax.spines['left'].set_linewidth(lwidth)
    ax.spines['right'].set_linewidth(lwidth)
    plt.ylim(0.0, 2)
    plt.ylabel('Offloading proportion')
    plt.xlabel('g) Number of edge nodes (Alibaba cluster-trace-v2018)')
    plt.yticks()
    plt.legend()
    plt.savefig('nodeOP.pdf', dpi=120, bbox_inches='tight')
    plt.show()
