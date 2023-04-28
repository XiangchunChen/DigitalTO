import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    labels=['25', '50', '75', '100']
    data = pd.DataFrame({'LE': [1.0, 1.0, 1.0,1.0], 'Random': [23/143.0, 164/168.0,  32/193.0, 28/218.0], 'DQN': [6/143.0, 17/168.0, 18/193.0,   22/218.0],
                         'Greedy': [18/143.0, 22/168.0,   25/193.0, 28/218.0], 'ADPRL': [139/143.0,164/168.0,  189/193.0,  214/218.0 ],
                         'class1': [0, 0, 0, 0], 'class2': [120/143.0,  4/168.0,   161.0/193.0,190/218.0], 'class3': [137/143.0,  151/168.0,  175/193.0,196/218.0],
                         'class4': [125/143.0, 146/168.0, 168/193.0, 190/218.0], 'class5': [4/143.0,4/168.0, 4/193.0, 4/218.0]},
                        index=labels)
    menStd = (2, 30, 40)
    womenStd = (30, 50, 20)
    x = np.arange(25,125,25, dtype=int)  # the label locations
    width = 5  # the width of the bars
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
    # rects2 = ax.bar(x - width, data['Random'],  width,  alpha=0.8,color="w",edgecolor="k",hatch=".....",
    #                 bottom=data['class2'], label='Random')
    # rects3 = ax.bar(x, data['DQN'], width, alpha=0.8,color="w",edgecolor="k",hatch="\\\\\\\\\\",
    #                 bottom=data['class3'], label='DQN+FCFS')
    # rects4 = ax.bar(x + width, data['Greedy'],  width,  alpha=0.8,color="w",edgecolor="k",hatch="/",
    #                 bottom=data['class4'], label='Greedy')
    # rects5 = ax.bar(x + width*2, data['ADPRL'],  width,  alpha=0.8,color="w",edgecolor="k",hatch="//",
    #                 bottom=data['class5'], label='ADPRL')
    # Add some text for labels, title and custom x-axis tick labels, etc.

    # ax.set_title('Scores by group and gender')
    lwidth = 10
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(lwidth)
    ax.spines['left'].set_linewidth(lwidth)
    ax.spines['right'].set_linewidth(lwidth)
    plt.ylim(0.0, 2)
    plt.ylabel('Offloading proportion')
    plt.xlabel('c) Number of subtasks (Alibaba cluster-trace-v2018)')

    plt.yticks()
    plt.legend()
    plt.savefig('subtaskOP.pdf', dpi=120, bbox_inches='tight')
    plt.show()
