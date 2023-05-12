import math
import sys

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

from AutoEncoder import AutoEncoder
from Environment import MultiHopNetwork
from Task import Task
from DDPG import DDPG
import os
import logging
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
# Define the autoencoder architecture

# Define the training process
def train_autoencoder(model, dataset, epochs, batch_size, learning_rate):
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(epochs):
        for batch_data in dataloader:
            bs_ba, br_bs_ = batch_data
            optimizer.zero_grad()
            output = model(bs_ba)
            loss = criterion(output, br_bs_)
            loss.backward()
            optimizer.step()

        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Return: 下个时刻的奖励（奖励与状态有关）
def unsupervised_learning(t_model, r_model, bs, ba, s_dim):
    bs_array = bs.array[1:].to_numpy()
    bs_array = bs_array.reshape(1, len(bs_array))
    ba = ba.reshape(1, len(ba))
    bs_ba = np.concatenate((bs_array, ba), axis=1)
    bs_ba_float = bs_ba.astype(np.float32)
    # print("bs_ba.dtype:", bs_ba.dtype)
    bs_ba_tensor = torch.tensor(bs_ba_float, dtype=torch.float32)
    bs_ = t_model.forward(bs_ba_tensor)
    bs_ = bs_[:, -s_dim:]
    br = r_model.forward(bs_)
    return br, bs_

# Function:检测对应时刻下的状态s中指定节点node_num是否有task t需要的resource
# Output: 输出需要的waiting time

def check_node_state(device, s, task):
    if device.resource > task.resource:
        wait_time = s["device_"+str(device.deviceId)+"_time"]
        return wait_time
    else:
        return sys.maxsize

def run_network(env, agent, task_num, transaction_model, reward_model, s_dim):
    step = 0
    final_action = 0
    completion_time_dic = {}
    reward_dic = {}

    for episode in range(1):
        # initial observation
        print("episode: ", episode)
        observation = env.reset()
        episode_done = False
        time_step = 1
        max_time = 10
        task_count = 0
        task_time_dic = {}
        subtask_time_dic = {}
        avg_reward_dic = {} # key: task_id value: time
        while not episode_done or time_step < max_time:
            # RL choose action based on observation
            print("-------------------timestep: ", time_step, "-------------------")
            tasks = getTasksByTime(env.taskList, time_step)
            task_count += len(tasks)

            if len(tasks) != 0:
                for i in range(len(tasks)):
                    task = tasks[i]
                    print("task:", task.subId)
                    # 在指定次数（指定概率）内，选择预估reward最高的action
                    max_reward = 0
                    min_wait_time = sys.maxsize - 1
                    # action_count = 1 # 选择2个动作中最优的一个
                    # target_action = None
                    # target_device_index = -1
                    # target_bandwidth = -1
                    # target_waitTime = -1
                    # temp_action = None
                    # while(action_count):
                    #     # Action需要满足resource constraints
                    #     UnavailableFlag = True # True表示 Unavailable
                    #     if episode < 0:
                    #         while(UnavailableFlag):
                    #             device_index, bandwidth, waitTime, temp_action = agent.choose_action(observation)
                    #             temp_device = env.deviceList[device_index-1]
                    #             wait_time = check_node_state(temp_device, observation, task)
                    #             if (wait_time < min_wait_time):
                    #                 target_action = temp_action
                    #                 target_device_index = device_index
                    #                 target_bandwidth = bandwidth
                    #                 target_waitTime = waitTime
                    #                 min_wait_time = wait_time
                    #                 UnavailableFlag = False
                    #     else:
                    #         while(UnavailableFlag):
                    device_index, bandwidth, waitTime, temp_action = agent.choose_action(observation)
                    target_device_index = device_index
                    target_bandwidth = bandwidth
                    target_waitTime = waitTime
                    target_action = temp_action
                    temp_device = env.deviceList[device_index-1]
                    # 这么来看， reward是没有用的，只有wait_time有用，还有bandwidth的waiting time
                    br, bs_ = unsupervised_learning(transaction_model, reward_model, observation, temp_action, s_dim-1)
                    # 将 PyTorch 张量转换为 NumPy 数组，并从 2D 数组中提取第一行
                    bs_values = bs_.detach().numpy().flatten()
                    # 使用 Pandas 的 map 函数将观测值与新的值关联起来
                    bs_keys = observation.keys()[1:]
                    updated_values = dict(zip(bs_keys, bs_values))
                    # 使用更新后的值创建一个新的 Pandas Series
                    predict_ob = pd.Series(updated_values)
                    # 根据 bs_ 创建一个新的 Pandas Series Observation_
                    # array_bs_ = bs_.detach().numpy()
                    # index_length = pd.Index(observation)
                    # array_length = np.repeat(array_bs_, len(index_length))
                    #
                    # predict_ob = pd.Series(array_length, index=index_length)
                    wait_time = check_node_state(temp_device, predict_ob, task)
                    # TODO 如何根据predicted bandwidth去优化target_bandwidth
                    # bandwidth = check_link_state(temp_action, predict_ob, task)
                    target_waitTime = min(wait_time, target_waitTime)
                    # breward = br.item()
                    # if (breward >= max_reward and wait_time <= min_wait_time):
                    #     target_action = temp_action
                    #     target_device_index = device_index
                    #     target_bandwidth = bandwidth
                    #     target_waitTime = waitTime
                    #     min_wait_time = wait_time
                    #     max_reward = br
                    #     UnavailableFlag = False
                    # action_count = action_count-1

                    # 存在问题是max_reward和reward有区别, 如何进行二次模型训练?
                    observation_, reward, done, finishTime = env.step(target_device_index, target_bandwidth, target_waitTime, task, time_step)

                    # average_waitTime, average_ctime
                    if task.taskId in avg_reward_dic.keys():
                        avg_reward_dic[task.taskId] = max(avg_reward_dic[task.taskId], reward)
                    else:
                        avg_reward_dic[task.taskId] = reward

                    subtask_time_dic[task.subId] = finishTime-time_step+1
                    # avg_reward_dic
                    # avg_reward += reward
                    if task.taskId in task_time_dic.keys():
                        task_time_dic[task.taskId] = max(task_time_dic[task.taskId], finishTime-time_step+1)
                    else:
                        task_time_dic[task.taskId] = finishTime-time_step+1
                    # task_time_dic[task] = finishTime-time_step

                    # TODO s, lstm_s,  a, r, s_, lstm_s_
                    agent.store_transition(observation, target_action, reward, observation_)

                    # if (step > 10) and (step % 5 == 0):
                    bs, ba, br, bs_ = agent.learn()
                    bs_ba = np.concatenate((bs[:, 1:], ba), axis=1) # 去除time的一列
                    # Convert the dataset to PyTorch tensors
                    bs_ba_tensor = torch.tensor(bs_ba, dtype=torch.float32)
                    bs_tensor = torch.tensor(bs_[:, 1:], dtype=torch.float32)
                    dataset = TensorDataset(bs_ba_tensor, bs_tensor)
                    # Train the transaction model
                    epochs = 10
                    batch_size = 64
                    learning_rate = 0.001
                    train_autoencoder(transaction_model, dataset, epochs, batch_size, learning_rate)
                    # Train the transaction model
                    epochs = 10
                    batch_size = 64
                    learning_rate = 0.001
                    br_tensor = torch.tensor(br, dtype=torch.float32)
                    dataset = TensorDataset(bs_tensor, br_tensor)
                    train_autoencoder(reward_model, dataset, epochs, batch_size, learning_rate)
                    # # Split the dataset into training and validation sets
                    # bs_ba_train, bs_ba_val, br_bs_train, br_bs_val = train_test_split(bs_ba, br_bs_, test_size=0.2, random_state=42)
                    # lr_schedule = keras.optimizers.schedules.ExponentialDecay(
                    #     initial_learning_rate=1e-2,
                    #     decay_steps=10000,
                    #     decay_rate=0.9)
                    # transaction_model.compile(optimizer=keras.optimizers.SGD(learning_rate=lr_schedule), loss='mse')
                    # epochs = 1
                    # batch_size = 64
                    # transaction_model.fit(bs_ba_train, br_bs_train, epochs=epochs, batch_size=batch_size, validation_data=(bs_ba_val, br_bs_val))

                    observation = observation_

            else:
                env.add_new_state(time_step)
            print(task_count)
            # ToRevise
            if task_count == task_num:
                episode_done = True
                completion_time = 0
                for task, time_value in task_time_dic.items():
                    print(task, time_value)
                    completion_time += time_value
                print("subtask_time_dic")
                print(subtask_time_dic)
                completion_time_dic[episode] = completion_time
                avg_reward = 0
                for task, reward in avg_reward_dic.items():
                    avg_reward += reward
                print("completion_time:", completion_time)
                reward_dic[episode] = avg_reward
                print("reward:", avg_reward)
                break

            time_step += 1
        step += 1
    agent.save_net()
    # agent.save_digital_model()
    now = "DDPGTO"
    auto_name = "DTmodels/"+now+".pth"
    # Save the trained model
    torch.save(transaction_model.state_dict(), auto_name)
    return completion_time_dic, reward_dic

def checkAllocated(taskList):
    res = False
    for task in taskList:
        if not task.isAllocated:
            res = True
    return res

def getTasksByTime(taskList, time_step):
    tasks = []
    for task in taskList:
        if task.release_time == time_step:
            tasks.append(task)
    sorted(tasks, key=lambda task: task.subId)
    return tasks

def destory(destory_path):
    df = pd.read_csv(destory_path)
    df.to_csv("DDPGTO/file/now_schedule.csv", index=0)

def plotCompletionTime(completion_time_dic,name):
    f1 = open("result/"+name+".csv", "w")
    x = []
    y = []
    for key, value in completion_time_dic.items():
        f1.write(str(key)+","+str(value)+"\n")
        x.append(key)
        y.append(value)
    f1.close()
    plt.plot(x, y)
    plt.ylabel(name)
    plt.xlabel('Episodes')
    plt.savefig("result/"+name+'.pdf')
    plt.show()

def run_model(env, agent,task_num, devices):
    final_action = 0
    completion_time_dic = {}
    reward_dic = {}
    observation = env.reset()
    episode_done = False
    time_step = 1
    max_time = 10
    task_count = 0
    task_time_dic = {}
    subtask_time_dic = {}
    avg_reward_dic = {} # key: task_id value: time
    agent.restore_net()
    while not episode_done or time_step < max_time:
        # RL choose action based on observation
        print("-------------------timestep: ", time_step, "-------------------")
        tasks = getTasksByTime(env.taskList, time_step)
        task_count += len(tasks)

        if len(tasks) != 0:
            for i in range(len(tasks)):
                task = tasks[i]
                print("task:", task.subId)
                action = agent.choose_action(observation)

                observation_, reward, done, finishTime = env.step(action, task, time_step)
                # average_waitTime, average_ctime
                if task.taskId in avg_reward_dic.keys():
                    avg_reward_dic[task.taskId] = max(avg_reward_dic[task.taskId], reward)
                else:
                    avg_reward_dic[task.taskId] = reward

                subtask_time_dic[task.subId] = finishTime-time_step+1
                # avg_reward_dic
                # avg_reward += reward
                if task.taskId in task_time_dic.keys():
                    task_time_dic[task.taskId] = max(task_time_dic[task.taskId], finishTime-time_step+1)
                else:
                    task_time_dic[task.taskId] = finishTime-time_step+1
                # task_time_dic[task] = finishTime-time_step

                # agent.store_transition(observation, action, reward, observation_)
                # if (step > 10) and (step % 5 == 0):
                #     agent.learn()

                observation = observation_

        else:
            env.add_new_state(time_step)
        print(task_count)
        # ToRevise
        if task_count == task_num:
            episode_done = True
            completion_time = 0
            for task, time_value in task_time_dic.items():
                print(task, time_value)
                completion_time += time_value
            print("subtask_time_dic")
            print(subtask_time_dic)
            # completion_time_dic[episode] = completion_time
            avg_reward = 0
            for task, reward in avg_reward_dic.items():
                avg_reward += reward
            print("completion_time:", completion_time)
            # reward_dic[episode] = avg_reward
            print("reward:", avg_reward)
            break
        time_step += 1
    return completion_time_dic

if __name__ == "__main__":
    # maze game

    ali_data = "Rfile/Test/Random_test_data/"
    # ali_data = "Rfile/Subtask/subtask100"
    # ali_data = "file/Test/Alibaba_test_data/"
    # ali_data = "Rfile/Bandwidth_test_data"
    task_file_path = ali_data+"task_info_5.csv"
    task_pre_path = ali_data+"task_pre_5.csv"
    # network_node_path = ali_data+"/network_node_info.csv"
    # network_edge_path = ali_data+"/network_edge_info.csv"
    # device_path = ali_data+"/device_info.csv"
    # schedule_path = "now_schedule.csv"
    # destory_path = "file/now_schedule.csv"
    network_node_path = "file/network_node_info.csv"
    network_edge_path = "file/network_edge_info.csv"
    device_path = "file/device_info.csv"
    schedule_path = "file/now_schedule.csv"
    destory_path = "now_schedule.csv"
    edges_devices_num = 16
    devices =[1,2,3,4,5,6,7,8]
    # Device: 50
    # edges_devices_num = 100
    # devices = [i for i in range(1,51)]
    # Device: 75
    # edges_devices_num = 148
    # devices = [i for i in range(1,76)]
    # Device: 100
    # edges_devices_num = 200
    # devices = [i for i in range(1,101)]

    # network_node_path = "file/device25/graph_node.csv"
    # network_edge_path = "file/device25/graph_edge.csv"
    # device_path = "file/device25/device_info.csv"
    # schedule_path = "file/device25/now_schedule.csv"
    # # DQN/file/device25
    # edges_devices_num = 49
    # devices = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    f1 = open(task_file_path, "r")
    lines = f1.readlines()
    task_num = len(lines)

    # destory(destory_path)
    dic_task_time = {}
    env = MultiHopNetwork(devices,edges_devices_num, schedule_path, network_edge_path, network_node_path, device_path, task_file_path, task_pre_path)

    # env.n_actions, env.n_features, n_lstm_features, n_time
    s_dim = env.n_features
    a_dim = 3  # < source, bandwidth, waitTime>
    a_bound = env.n_actions

    # Initialize the autoencoder model
    input_dim = s_dim - 1 + a_dim
    hidden_dim = 128
    output_dim = s_dim - 1
    transaction_model = AutoEncoder(input_dim, hidden_dim, output_dim)
    r_input_dim = s_dim - 1
    r_output_dim = 1
    reward_model = AutoEncoder(r_input_dim, hidden_dim, r_output_dim)

    agent = DDPG(a_dim, s_dim, a_bound, transaction_model)

    import time
    # 记录开始时间
    start_time = time.time()

    # 在这里插入需要计时的代码块
    completion_time_dic, reward_dic = run_network(env, agent,task_num, transaction_model, reward_model, s_dim)

    # 记录结束时间
    end_time = time.time()

    # 计算执行时间，单位为秒
    elapsed_time = end_time - start_time

    # 将执行时间转换为小时和分钟，并打印结果
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    print(f"Execution time: {hours} hours, {minutes} minutes")

    # completion_time_dic, reward_dic = run_model(env, agent, task_num)
    min_sum = sys.maxsize
    plotCompletionTime(completion_time_dic, "completion_time")
    plotCompletionTime(reward_dic, "reward")
    agent.plot_cost()
    # get TF logger