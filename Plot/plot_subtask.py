# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
if __name__ == '__main__':

    # x1=[5,10,20]
    # y1=[
    #     0.714, 2.118,7.757
    # ]
    x1=[25,50,75,100]
    y1=[39002/40.0, 55382/40.0, 64229/40.0, 104229/40.0]
    # x2=[]
    num = 3 # LE processing speed: 30
    y2=[49105.0/(40.0*num), 90355.0/(40.0*num), 129080.0/(40.0*num), 446770.0/(40.0*num)]
    # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    y3=[33800/40.0,34390/40.0, 37710/40.0,64168/40.0]
    y4=[24601/40.0,25897/40.0, 28065/40.0, 56800/40.0]
    y5=[15429/40.0,16935/40.0, 18609/40.0, 38512/40.0]
    # (49105.0/120-15429/40.0)/(49105.0/120)+(90355.0/120-16935/40.0)/(90355.0/120)+(129080.0/120-18609/40.0)/(129080.0/120)+(446770.0/120-38512/40.0)/(446770.0/120)
    1.80400303617+1.64772992908
    # (39002/40.0-15429/40.0)/(39002/40.0)+(55382/40.0-16935/40.0)/(55382/40.0)+(64229/40.0-18609/40.0)/(64229/40.0)+(104229/40.0/120-38512/40.0)/(104229/40.0)

    # (24601-15429)/24601+(25897-16935)/25897+(28065-16935)/28065+(56800-38512)/56800

    # (4162.5-1542.0)/4162.5+(4265.5-1692.6)/4265.5+(4346.9-1860.0)/4346.9+(6833.7-3850.3)/6833.7
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
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(width)
    ax.spines['left'].set_linewidth(width)
    ax.spines['right'].set_linewidth(width)
    # plt.plot(x1,y1,'ro-')
    # plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
    # plt.title('Effect of changing number of subtasks')
    plt.xlabel('c) Number of subtasks (Alibaba cluster-trace-v2018)')
    plt.ylabel('Average completion time(ms)')
    plt.xticks(x1)
    plt.legend()
    plt.savefig('subtask.pdf', dpi=120, bbox_inches='tight')
    plt.show()