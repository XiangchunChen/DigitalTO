import tensorflow as tf

def save2DQN(loss,name):
    cost_writer = tf.summary.create_file_writer('graph')
    for batch_index in range(len(loss)):
        with cost_writer.as_default():
            tf.summary.scalar(name, loss[batch_index], step=batch_index)

if __name__ == '__main__':
    f1 = open("file/device25/result/completion_time.csv")
    f2 = open("file/device25/result/reward.csv")
    # f3 = open("result/result5/cost.csv")
    completion_list = []
    reward_list = []
    cost_list = []
    lines1 = f1.readlines()
    for line in lines1:
        info = line.strip("\n").split(",")
        completion_list.append(float(info[1]))

    lines2 = f2.readlines()
    for line in lines2:
        info = line.strip("\n").split(",")
        reward_list.append(float(info[1]))

    # lines3 = f3.readlines()
    # for line in lines3:
    #     info = line.strip("\n").split(",")
    #     cost_list.append(float(info[1]))

    save2DQN(completion_list, "completion_time")
    # save2DQN(cost_list, "cost")
    save2DQN(reward_list, "reward")