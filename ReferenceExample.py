import torch
import torch.nn as nn
import torch.optim as optim

# Define the neural network architecture
class TransportationPredictionModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(TransportationPredictionModel, self).__init__()
        self.hidden = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.output = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        hidden = self.relu(self.hidden(x))
        output = self.output(hidden)
        return output

# Prepare the training data
train_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
train_labels = torch.tensor([[10.0], [20.0], [30.0]])

# Initialize the model with
input_size = 3
hidden_size = 10
output_size = 1
model = TransportationPredictionModel(input_size, hidden_size, output_size)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Train the model
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(train_data)
    loss = criterion(outputs, train_labels)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Test the model
test_data = torch.tensor([[2.0, 3.0, 4.0]])
predicted_labels = model(test_data)
print(f'Predicted Labels: {predicted_labels.item()}')
