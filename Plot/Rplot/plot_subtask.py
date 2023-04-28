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
    x1=[25,50,75,100]
    y1=[24417/40.0, 37346/40.0, 88276/40.0, 163589/40.0]
    # x2=[]
    num = 3 # LE processing speed: 30
    y2=[96225.2/(40.0*num), 137475.2/(40.0*num), 176200.2/(40.0*num), 493890.2/(40.0*num)]
    # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    y3=[32960/40.0+200, 35233/40.0+200, 39354/40.0+200, 75994/40.0+300]
    y4=[28484/40.0+100, 30411/40.0+100,34276/40.0+100, 67013/40.0+100]
    y5=[24196/40.0, 25702/40.0, 27376/40.0, 47279/40.0]
    # (75994/40.0-67013/40.0)/(75994/40.0)
    # (28484-24196)/28484+(30411-25702)/30411+(34276-27376)/34276+(67013-47279)/67013

    # (32960-24196)/32960+(35233-25702)/35233+(39354-27376)/39354+(75994-47279)/75994
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
    plt.xlabel('d) Number of subtasks (Synthetic DAGs)')
    plt.ylabel('Average completion time(ms)')
    plt.xticks(x1)
    plt.legend()
    plt.savefig('rsubtask.pdf', dpi=120, bbox_inches='tight')
    plt.show()