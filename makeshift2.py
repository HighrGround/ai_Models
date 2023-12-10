import torch
import numpy as np




#model parameters
input_size = 64


#f ind avacado 
#find what is macholibre 
#implement loss function


file_path = 'reales.csv'
data = pd.read_csv(file_path)

# Split the data into features (X) and target variable (y)
X = data.drop('target_column_name', axis=1)  # Replace 'target_column_name' with the actual name of your target variable
y = data['target_column_name']


class DenseLayer:
    def __init__(self, input_size, output_size, activation_function):
        self.weights = np.random.randn(input_size, output_size)
        self.bias = np.zeros((1, output_size))
        self.activation_function = activation_function
        self.input_data = None
        self.output_data = None

    def forward(self, input_data):
        self.input_data = input_data
        self.output_data = np.dot(input_data, self.weights) + self.bias
        if self.activation_function is not None:
            self.output_data = self.activation_function(self.output_data)
        return self.output_data



layer1 = DenseLayer(input_size)


class loss_fucntion:
    def __init__(self,):
        






'''
class RNNCell(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.xh_to_h = nn.Linear(config.n_embd + config.n_embd2, config.n_embd2)

    def forward(self, xt, hprev):
        xh = torch.cat([xt, hprev], dim=1)
        ht = F.tanh(self.xh_to_h(xh))
        return ht

'''