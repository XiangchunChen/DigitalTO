import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    labels=['10', '20', '30', '40']
    data = pd.DataFrame({'ADPRL without Dependency': [0,0,0,0],  'ADPRL': [0,0,0,0],
                         'class2': [2/43,2/68,2/93,1/120], 'class5': [4/43.0,4/68.0, 4/93.0, 1/120.0]},
                        index=labels)
    menStd = (2, 30, 40)
    womenStd = (30, 50, 20)
    x = np.arange(10,50,10, dtype=int)  # the label locations
    width = 2  # the width of the bars
    ls = ['ADPRL without Dependency','ADPRL']


    rects2 = plt.bar(x, data['class2'],  width,  alpha=0.8,color="w",edgecolor="k",hatch=".....",
                     bottom=data['ADPRL without Dependency'], label='ADPRL without Dependency')

    rects5 = plt.bar(x + width,data['class5'],  width,  alpha=0.8,color="w",edgecolor="k",hatch="//",
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
    plt.xlabel('a) Number of tasks (Alibaba cluster-trace-v2018)')
    plt.yticks()
    plt.legend()
    plt.savefig('ctaskOP.pdf', dpi=120, bbox_inches='tight')
    plt.show()
