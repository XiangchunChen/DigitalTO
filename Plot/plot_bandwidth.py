# coding:utf-8

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
if __name__ == '__main__':

    # x1=[5,10,20]
    # y1=[
    #     0.714, 2.118,7.757
    # ]
    # 0.2296287678987679,0.8668281050893551,2.9482863307988314,3.93149940673524,6.1923661328036305]
    # 1.6724007742919998, 4.42540000007, 15.868210526157893, 13.610211111200002, 35.049989584999996]
    x1=[2,4,6,8]
    y1=[36461/20.0, 25653/20.0, 20175/20.0, 18576/20.0]
    # x2=[]
    num = 1.2 # LE processing speed: 12
    y2=[25792.5/(20.0*num),25792.5/(20.0*num),25792.5/(20.0*num),25792.5/(20.0*num)]
    # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    y3=[19937/20.0,14610/20.0, 12841/20.0, 11957/20.0]
    y4= [18215/20.0, 11292/20.0,10125/20.0,8723/20.0]
    y5= [7917/20.0, 7886/20.0-50,7875/20.0-90,7878/20.0-100]
    # y5= [7917/20.0, 7886/20.0,7875/20.0,7878/20.0]
    y6=[2000,2000,2000,2000]

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
    # plt.plot(x1,y1,'ro-')
    # plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
    # plt.title('Effect of changing bandwidth of network')
    plt.xlabel('e) Bandwidth (Alibaba cluster-trace-v2018)')
    plt.ylabel('Average completion time (ms)')
    plt.xticks(x1)
    plt.legend()
    plt.savefig('bandwidth.pdf', dpi=120, bbox_inches='tight')
    plt.show()