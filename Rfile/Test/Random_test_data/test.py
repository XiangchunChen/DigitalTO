if __name__ == '__main__':
    f1 = open("info.csv", "r")
    f2 = open("task.csv", "w")
    lines = f1.readlines()
    for line in lines:
        info = line.strip("\n").split(",")
        num1 = int(info[0])
        line = str(num1)+"\n"
        if num1 < 400:
            line = str(num1)+"0\n"
        f2.write(line)
