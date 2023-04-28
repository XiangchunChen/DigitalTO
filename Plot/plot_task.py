# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
if __name__ == '__main__':


    x1=[10,20,30,40]
    num = 1.2 # LE processing speed: 12
    y1=[1513/(10.0*num), 32923/(20.0*num), 60799/(30.0*num),85508/(40.0*num)]
    # x2=[]
    y2=[1385.0/(10.0*num),25792.5/(20.0*num), 45125.0/(30.0*num), 64487.0/(40.0*num)]
    # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    y3=[673/10.0, 11431/20.0, 29279/30.0, 39823/40.0+100]
    y4=[736/10.0, 8398/20.0, 16832/30.0, 32107/40.0]
    y5=[450/10.0,7879/20.0, 14218/30.0, 21206/40.0]
    # (1385.0/(12)-450/10.0)/(1385.0/(12))
    # (25792.5/24-7879/20.0)/(25792.5/24)=0.6334
    # (64487.0/48-21206/40.0)/(64487.0/48)=6053
    y6=[3000,3000,3000,3000]
    # x=np.arange(20,350)
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    width = 10
    l1=plt.plot(x1,y1,'r--',label='Random', linewidth=width)
    l2=plt.plot(x1,y2,'g--',label='LE', linewidth=width)
    l3=plt.plot(x1,y3,'b--',label='DQN+FCFS', linewidth=width)
    l4=plt.plot(x1,y4,'b^-',label='Greedy', linewidth=width)
    l5=plt.plot(x1,y5,'ro-',label='ADPRL', linewidth=width)
    l6=plt.plot(x1,y6,'w')
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
    plt.xlabel('a) Number of tasks (Alibaba cluster-trace-v2018)')
    plt.ylabel('Average completion time (ms)')
    plt.legend()
    plt.savefig('task.pdf', dpi=120, bbox_inches='tight')
    plt.show()