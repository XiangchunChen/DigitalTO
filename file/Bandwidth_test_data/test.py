if __name__ == '__main__':
    f1 = open("test.csv", "r")
    f2 = open("task.csv", "w")
    lines = f1.readlines()
    for line in lines:
        info = line.strip("\n").split(",")
        num1 = int(info[0][0:3])
        line = str(num1)+"\n"
        f2.write(line)