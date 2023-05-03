# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
if __name__ == '__main__':

    # x1=[5,10,20]
    # y1=[
    #     0.714, 2.118,7.757
    # ]
    # 0.2296287678987679,0.8668281050893551,2.9482863307988314,3.93149940673524,6.1923661328036305]
    # 1.6724007742919998, 4.42540000007, 15.868210526157893, 13.610211111200002, 35.049989584999996]
    x1=[2,4,6,8]

    y1=[18492/30.0, 13178/30.0,12000/30.0, 10618.1/30.0]
    # x2=[]
    num = 1.2
    y2=[12618.1/(30.0*num),12618.1/(30.0*num),12618.1/(30.0*num),12618.1/(30.0*num)]
    # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    y3=[10255/30.0, 6838/30.0, 5825/30.0,5308/30.0]
    y4= [9345/30.0, 6918/30.0+5, 4588/30.0+20, 4555/30.0+5]
    y5= [9457/30.0, 5638/30.0, 4643/30.0, 4186/30.0]
    # (9345-9457)/9345+(6918-5638)/6918+(4588-4643)/4588+(4555-4186)/4555
    y6=[700,700,700,700]
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    width = 10
    l1=plt.plot(x1,y1,'r--',label='Random', linewidth=width)
    l2=plt.plot(x1,y2,'g--',label='LE', linewidth=width)
    l3=plt.plot(x1,y3,'b--',label='DQN+FCFS', linewidth=width)
    l4=plt.plot(x1,y4,'b^-',label='Greedy', linewidth=width)
    l5=plt.plot(x1,y5,'ro-',label='DTTO', linewidth=width)
    l6=plt.plot(x1,y6,'w')
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(width)
    ax.spines['left'].set_linewidth(width)
    ax.spines['right'].set_linewidth(width)

    # plt.plot(x1,y1,'ro-')
    # plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
    # plt.title('Effect of changing bandwidth of network')
    plt.xlabel('f) Bandwidth (Synthetic DAGs)')
    plt.ylabel('Average completion time (ms)')
    plt.xticks(x1)
    plt.legend()
    plt.savefig('rbandwidth.pdf', dpi=120, bbox_inches='tight')
    plt.show()