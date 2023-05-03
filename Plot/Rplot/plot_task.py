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
    # y1=[329/5.0, 1230/10.0, 5417/20.0, 7186/30.0, 7218/40.0]
    # # x2=[]
    # y2=[403/5.0, 1159/10.0, 5652/20.0, 7213/30.0, 7213/40.0]
    # # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    # y3=[322/5.0, 1064/10.0, 4794/20.0, 6238/30.0, 6332/40.0]
    # y4=[180/5.0, 664/10.0, 2440/20.0, 3206/30.0, 3233/40.0]
    # y5=[290/5.0, 1187/10.0, 6794/20.0, 8718/30.0, 9160/40.0]
    x1=[10,20,30,40]
    num = 1.2 # LE processing speed: 12
    y1=[2902.1/(10.0*num), 7301.3/(20.0*num), 16618.1/(30.0*num), 107983.7/(40.0*num)]
    # 0.42709
    y2=[1902.1/(10.0*num), 6301.3/(20.0*num), 12618.1/(30.0*num), 97983.7/(40.0*num)]
    # x3=[30,50,70,90,105,114,128,137,147,159,170,180,190,200,210,230,243,259,284,297,311]
    y3=[814/10.0+50, 2102/20.0+50, 5013/30.0 + 150,33322/40.0 + 100]
    y4=[874/10.0, 2377/20.0 + 100, 4555/30.0+ 100, 28645/40.0+ 100]
    y5=[856/10.0, 2345/20.0, 4164/30.0, 24510/40.0]
    # (874-856)/874+(2377-2345)/2377+(4555-4164)/4555+(28645-24510)/28645
    # (1902.1-814)/1902.1
    # (6301.3-2102)/6301.3 = 0.66
    # (12618.1-5013)/12618.1 = 0.6027
    # (1902.1-856)/1902.1 = 0.54997
    # (6301.3-2345)/6301.3 = 0.62785456969
    # (12618.1-4164)/12618.1 = 0.66999
    # (97983.7-24510)/97983.7 = 0.74985635365

    # x=np.arange(20,350)
    plt.figure(figsize=(32,29))
    plt.rc('font',family='Times New Roman')
    matplotlib.rcParams.update({'font.size': 100})
    width = 10
    l1=plt.plot(x1,y1,'r--',label='Random', linewidth=width)
    l2=plt.plot(x1,y2,'g--',label='LE', linewidth=width)
    l3=plt.plot(x1,y3,'b--',label='DQN+FCFS', linewidth=width)
    l4=plt.plot(x1,y4,'b^-',label='Greedy', linewidth=width)
    l5=plt.plot(x1,y5,'ro-',label='DTTO', linewidth=width)
    ax=plt.gca()
    ax.spines['bottom'].set_linewidth(width)
    ax.spines['left'].set_linewidth(width)
    ax.spines['right'].set_linewidth(width)
    plt.xticks(x1)
    # plt.plot(x1,y1,'ro-')
    # plt.plot(x1,y1,'ro-',x2,y2,'g+-',x3,y3,'b^-')
    # plt.title('Effect of changing number of tasks')
    plt.xlabel('b) Number of tasks (Synthetic DAGs)')
    plt.ylabel('Average completion time (ms)')
    plt.legend()
    plt.savefig('rtask.pdf', dpi=120, bbox_inches='tight')
    plt.show()