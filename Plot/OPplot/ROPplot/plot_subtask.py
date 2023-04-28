import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    labels=['25', '50', '75', '100']
    data = pd.DataFrame({'LE': [1.0, 1.0, 1.0,1.0], 'Random': [ 82 / 404.0,   53 / 429.0 ,63 / 454.0, 67 / 479.0], 'DQN': [46 / 404.0, 48 / 429.0 ,  50 / 454.0 ,  51 / 479.0],
                         'Greedy': [51 / 404.0, 55 / 429.0 ,   58 / 454.0,  58 / 479.0], 'ADPRL': [144 / 404.0,169 / 429.0,194 / 454.0, 219 / 479.0],
                         'class1': [0, 0, 0, 0], 'class2': [322/404.0,  376/ 429.0  ,391 / 454.0,412/479.0], 'class3': [358 / 404.0,  381 / 429.0,  404 / 454.0 ,  428 / 479.0],
                         'class4': [ 353 / 404.0, 374 / 429.0,   396 / 454.0,  421 / 479.0], 'class5': [260 / 404.0, 260/ 429.0,260/454.0,260/ 479.0]},
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
    # Add some text for labels, title and custom x-axis tick labels, etc.
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
    # ax.set_title('Scores by group and gender')
    lwidth = 10
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(lwidth)
    ax.spines['left'].set_linewidth(lwidth)
    ax.spines['right'].set_linewidth(lwidth)
    plt.ylim(0.0, 2)
    plt.ylabel('Offloading proportion')
    plt.xlabel('d) Number of subtasks (Synthetic DAGs)')

    plt.yticks()
    plt.legend()
    plt.savefig('rsubtaskOP.pdf', dpi=120, bbox_inches='tight')
    plt.show()
