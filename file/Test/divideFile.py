import random
import re

if __name__ == '__main__':
    f1 = open("ali_task_info.csv", "r")
    lines = f1.readlines()
    list = []
    num = 1
    for line in lines:
        f2.write(line)
        info = line.split(",")
        taskId = (int)(info[1])
        if taskId not in list:
            list.append(taskId)
        if len(list) == 10:
            f2 = open("task_info"+".csv", "w")
            f2.write("file"+str(num)+"\n\n\n")
            num = num + 1
            list = []
    f1.close()
    f2.close()