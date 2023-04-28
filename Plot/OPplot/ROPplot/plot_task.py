import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    labels=['10', '20', '30', '40']
    x1=[10,20,30,40]
    data = pd.DataFrame({'LE': [1.0, 1.0, 1.0,1.0], 'Random': [10 / 52.0,30 / 180.0, 46 / 280.0, 67 / 400.0], 'DQN': [7 / 52.0, 21 / 180.0,  31 / 280.0, 44 / 400.0],
                         'Greedy': [6 / 52.0, 21 / 180.0, 33 / 280.0, 51 / 400.0], 'ADPRL': [24 / 52.0,   24 / 180.0,   65 / 280.0  ,  119 / 400.0],
                         'class1': [0, 0, 0, 0], 'class2': [42 / 52.0,150 / 180.0, 234 / 280.0, 333 / 400.0], 'class3': [45 / 52.0, 159 / 180.0,  249 / 280.0, 356 / 400.0],
                         'class4': [46 / 52.0, 159 / 180.0, 247 / 280.0, 349 / 400.0], 'class5': [28 / 52.0,   156 / 180.0,   215 / 280.0  ,  281 / 400.0]},
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

    lwidth = 10
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(lwidth)
    ax.spines['left'].set_linewidth(lwidth)
    ax.spines['right'].set_linewidth(lwidth)
    plt.ylim(0.0, 2)
    plt.ylabel('Offloading proportion')
    plt.xlabel('b) Number of tasks (Synthetic DAGs)')
    plt.xticks(x1)
    plt.yticks()
    plt.legend()
    plt.savefig('rtaskOP.pdf', dpi=120, bbox_inches='tight')
    plt.show()
