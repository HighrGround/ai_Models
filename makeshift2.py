import torch
import torch.nn as nn
import torch.optim as optim


import numpy as np
import pandas as pd

#model parameter
input_size = 64
ouput_size = 1
file_path = 'Songs.csv'
data = pd.read_csv(file_path)
X = data.drop('Type', axis=1).values 
y = data['key'].values  

class DenseLayer:
    def __init__(self, input_size, output_size, activation_function):
        self.weights = np.random.randn(input_size, output_size)
        self.bias = np.zeros((1, output_size))
        self.activation_function = nn.relu()
        self.input_data = None
        self.output_data = None
        


    def forward(self, input_data):
        self.input_data = input_data
        self.output_data = np.dot(input_data, self.weights) + self.bias
        if self.activation_function is not None:
            self.output_data = self.activation_function(self.output_data)
        return self.output_data

class SequentialNeuralNetwork:
    def __init__(self):
        self.layers = []

    def add_layer(self, layer):
        self.layers.append(layer)

    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X

    def get_parameters(self):
        params = []
        for layer in self.layers:
            params.append(layer.weights)
            params.append(layer.bias)
            print(f"Layer {layer.__class__.__name__} parameters: {params[-2].shape}, {params[-1].shape}")
        return params










class loss_function:
    def calculate(self, ouput, y ):
        sample_loses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss

'''
class loss_categorical(loss_function):
    def forward(self, y_pred, y_true):
        samples =len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)
        if len(y_true.shape) == 1:
            correct_confidences - y_pred_clipped[range(samples), y_true]
        #this deals with one hot encoded vectos as apposed to the
        elif len(y_true.shape) == 2:
            correct_confidences = np.sum(y_pred_clipped*y_true, axis=1)
        negative_log_liklihoods = -np.log(correct_confidences)
        return negative_log_liklihoods
    
'''
model = SequentialNeuralNetwork()




#defining the loss function and optimiser
loss_function1 = loss_function()


optimizer = optim.SGD(model.get_parameters(), lr=0.01)  



epochs = 1000
for epoch in range(epochs):
    optimizer.zero_grad()
    predictions = model(torch.FloatTensor(X))
    loss = loss_function1.calculate_loss(predictions, y)  
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')
