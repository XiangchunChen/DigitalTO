import random
import re

if __name__ == '__main__':
    # fl = "Alibaba_test_data6"
    f1 = open("task_info_40.csv", "r")
    lines = f1.readlines()
    # TODO revise
    lastId = 80
    num = 0
    max_num = 0
    totalnum = 0
    for line in lines:
        info = line.split(",")
        taskId = (int)(info[1])
        if taskId == lastId:
            num = num + 1
        else:
            if num > max_num:
                max_num = num
            if taskId == lastId:
                print("task",lastId, "num", num)
                # break
            # totalnum = totalnum+num
            print("task",lastId,"num",num)
            lastId = taskId
            num = 1
    # print("max_num",max_num)
    # print("avg_num",totalnum/40)
    f1.close()
