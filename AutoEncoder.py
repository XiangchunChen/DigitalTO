from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Input


# Define the autoencoder architecture
class AutoEncoder(Model):
    def __init__(self, input_dim, hidden_dim):
        super(AutoEncoder, self).__init__()
        self.encoder = Dense(hidden_dim, activation='relu')
        self.decoder = Dense(input_dim, activation='relu')

    def call(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
