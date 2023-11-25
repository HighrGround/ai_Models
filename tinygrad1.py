import tinygrad as tg
import numpy as np
import torch


layer_outputs = [4.8,1.21, 2.385]
e = 2.7182818


#showcased in this video expontialization using eulers number nomralization to put all numbers to positive values while retaining information.
#  on the whole this process can be defined as a softmax function.


exp_values = np.exp(layer_outputs)

for output in layer_outputs:
    #by exponentiating the sum we can retain the information of the values while also converting the numbers to a positive value
    exp_values.append(e**output) 

#to do normalization

norm_base  = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)
    print(norm_values)







class Layer_dense:
    def __init__(self, n_inputs, n_neurons): 
        self.weigths =0.10 * np.random.randn(1, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, X):
        self.z = np.dot(X, self.weigths) + self.biases


class activation_ReLU: 
    def forward(self, X):
        self.output = np.maximum(X, 0)


 