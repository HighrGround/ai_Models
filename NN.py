import numpy as np
import torch 
import torch.nn as nn
from torchvision import datasets, transforms
from matplotlib import pyplot

transform = transforms.Compose([
    transforms.ToTensor(),  # Convert to tensor format
    transforms.Normalize((0.1307,), (0.3081,))  # Normalize pixel values
])

kernal_size = 
number_of_filters = 




train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)


device = "rocm"



for i in range(9):  
    pyplot.subplot(330 + 1 + i)
    pyplot.imshow(train_X[i], cmap=pyplot.get_cmap('gray'))
    pyplot.show()


image_size = 224* 224


class ConvUnit(nn.Module):
  def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
    super(ConvUnit, self).__init__()
    self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
    self.relu = nn.ReLU()

  def forward(self, x):
    x = self.conv(x)
    x = self.relu(x)
    return x
class Layer_dense:
    def __init__(self, n_inputs, n_neurons): 
        self.weigths =0.10 * np.random.randn(1, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, X):
        self.z = np.dot(X, self.weigths) + self.biases


layer1 = layer_dense(4,5)
layer2 = layer_dense(5,2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)


#an activation function is a graph function that goes from -x to +x gong up to one somewhere in the middle this can be done in a few ways 
# with either step sigmoid relu and more , step is almost never used sigmoid provides good granular results relu is simple if x < 0 x == 0 
# then has about a 35% gradient relu is very good is also very granular relaible and quick especially useful for inputs above 0 

#no linear diagonal line function is used as this produces a sin wave which is hard to fit a line of best fit too (which represnts a model trying to find patterns)
#in short makes less lines wavy lines in graph makes non linear easier to fit to






class loss:
    def __init__:
        