import numpy as np
import torch
import nnfs as nf

#showcased in this video expontialization using eulers number nomralization to put all numbers to positive values while retaining information.
#  on the whole this process can be defined as a softmax function.



inputs = [[4.8,1.21, 2.385],
          [4.8,1.21, 2.385],
          [4.8,1.21, 2.385]]

for output in layer_outputs:
    #by exponentiating the sum we can retain the information of the values while also converting the numbers to a positive value
    exp_values.append(e**output) 

class Layer_dense:
    def __init__(self, n_inputs, n_neurons): 
        self.weigths =0.10 * np.random.randn(1, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, X):
        self.z = np.dot(X, self.weigths) + self.biases

class activation_Softmax:
    def forward(self, X):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(inputs, axis=1, keepdims=True))
        self.output = probabilities

class activation_ReLU: 
    def forward(self, X):
        self.output = np.maximum(X, 0)

X, y = spiral_data(samples = 100, classes = 3)

dense1 = Layer_dense(2,3)
activation2 = activation_ReLU()

dense2 = Layer_dense(3,3)
activation2 = activation_Softmax()