import tinygrad as tg
import numpy as np
import torch



class Layer_dense:
    def __init__(self, n_inputs, n_neurons): 
        self.weigths =0.10 * np.random.randn(1, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, X):
        self.z = np.dot(X, self.weigths) + self.biases


class activation_ReLU:
    def forward(self, X):
        self.output = np.maximum(X, 0)

    