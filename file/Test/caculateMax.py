import random
import re

if __name__ == '__main__':
    fl = "Alibaba_test_data6"
    f1 = open("ali_task_info.csv", "r")
    lines = f1.readlines()
    list = []
    # TODO revise
    lastId = 1
    num = 0
    max_num = 0
    totalnum = 0
    for line in lines:
        info = line.split(",")
        taskId = (int)(info[1])
        if taskId not in list:
            list.append(taskId)
        if taskId == lastId:
            num = num + 1
        else:
            if num > max_num:
                max_num = num
            if num >= 100:
                print("task",lastId, "num", num)
                # break
            # totalnum = totalnum+num
            # print("task",lastId,"num",num)
            lastId = taskId
            num = 1
    # print("max_num",max_num)
    # print("avg_num",totalnum/40)
    f1.close()
