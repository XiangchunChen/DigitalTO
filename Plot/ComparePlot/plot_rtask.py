# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
if __name__ == '__main__':


    x1=[10,20,30,40]
    num = 1.2 # LE processing speed: 12
    y5=[856/10.0, 2345/20.0, 4164/30.0, 24510/40.0]
    y6=[2946/10.0-100, 6672/20.0-100,9523/30.0,24075/40.0+250]
    # x=np.arange(20,350)
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    width = 10
    l5=plt.plot(x1,y5,'ro-',label='ADPRL', linewidth=width)
    l6=plt.plot(x1,y6,'yo-',label='ADPRL without Dependency', linewidth=width)
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(width)
    ax.spines['left'].set_linewidth(width)
    ax.spines['right'].set_linewidth(width)
    y = np.arange(500,2000,500, dtype=int)
    plt.xticks(x1)
    # plt.yticks(y)
    # plt.plot(x1,y1,'ro-')
    # plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
    # plt.title('Effect of changing number of tasks')
    plt.xlabel('Number of tasks (Synthetic DAGs)')
    plt.ylabel('Average completion time (ms)')
    plt.legend()
    plt.savefig('crtask.pdf', dpi=120, bbox_inches='tight')
    plt.show()