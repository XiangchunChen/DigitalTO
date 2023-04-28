import numpy as np

from AutoEncoder import AutoEncoder


def unsupervised_learning(model, bs, ba,  bs_dim=8):
    bs_ba = np.concatenate((bs, ba), axis=1)
    br_bs_ = model.predict(bs_ba)
    br = br_bs_[:, -bs_dim - 1: -bs_dim]
    bs_ = br_bs_[:, -bs_dim:]


    return br, bs_
if __name__ == '__main__':

    s_dim = 8
    a_dim = 3
    input_dim = 3 + 8
    hidden_dim = 128
    loaded_model = AutoEncoder(input_dim, hidden_dim)
    loaded_model.load_weights('DDPGTO.h5')
    MEMORY_CAPACITY = 10000
    BATCH_SIZE = 64
    # Example usage
    memory = np.zeros((MEMORY_CAPACITY, s_dim * 2 + a_dim + 1), dtype=np.float32)  # memory里存放当前和下一个state，动作和奖励
    indices = np.random.choice(MEMORY_CAPACITY, size=BATCH_SIZE)
    bt = memory[indices, :]
    bs = bt[:, :s_dim]
    ba = bt[:, s_dim: s_dim + a_dim]
    # new_bs = np.zeros(s_dim, dtype=np.float32)  # Load new bs data here
    # new_ba = np.zeros(a_dim, dtype=np.float32) # Load new ba data here

    predicted_br, predicted_bs_ = unsupervised_learning(loaded_model, bs, ba)
    print(predicted_br, predicted_bs_)