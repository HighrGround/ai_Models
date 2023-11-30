import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence
from transformers import AutoTokenizer
import torch.optim as optim



# Initialize an empty list to store tokenized sentences
tokenized_text = []

# Open the file and read it line by line
with open('testdata.txt') as fp:
    for line in fp:
        # Split the line into words and remove leading/trailing whitespaces
        words = line.strip().split()
        if words:
            tokenized_text.append(words)

learning_rate =0.001
batch_size = 6


'''this finds all the words used in the provided text along with inputting all  the words into '''


unique_words = list(set(word for sentence in tokenized_text for word in sentence))
input_vocab_size = len(unique_words)
numerical_text = [[unique_words.index(word) for word in sentence] for sentence in tokenized_text]
numerical_text_tensors = [torch.LongTensor(sentence) for sentence in numerical_text]
tokenized_text_tensor = torch.LongTensor(numerical_text)
padded_text = pad_sequence(numerical_text_tensors, batch_first=True, padding_value=0)


#change these values if want to
embedding_dim = 100
hidden_dim = 140
dropout = 0.2
output_dim =1


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.embedding = nn.Embedding(input_vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=5, batch_first=True)
        #Embedding Layer: You'll likely start with an embedding layer to convert words into dense vector representations.
        # You'll need to specify the input vocabulary size (number of unique words) and the embedding dimension.
        self.fc = nn.Linear(hidden_dim, output_dim)
        # relu layer to add non lineartiry to the model
        self.relu = nn.ReLU()
        self.tanh = nn.tanh()
        '''Dropout and Batch Normalization are techniques used in neural networks to improve training and generalization
        Purpose: Dropout is a regularization technique that helps prevent overfitting in neural networks.
        It randomly "drops out" (sets to zero) a fraction of neurons during each forward and backward pass,
        effectively making the network more robust by preventing it from relying too heavily on any single neuron.
        Dropout Rate: The dropout rate is a hyperparameter that determines the fraction of neurons to drop during training.
        Common values range from 0.2 to 0.5, but you should experiment with different rates to find the one that works best for your model and dataset.
        see notes for batch normalization 
        obsidian://open?vault=Mapped-notes&file=Natrual-Language(nlp)
        '''
        self.dropout = nn.Dropout(dropout)

        def forward(self, x):
            # text: [batch size, max sequence length]

            # Embedding layer
            embedded = self.embedding(x)
            # embedded: [batch size, max sequence length, embedding_dim]

            # LSTM layer
            lstm_out, (hidden, cell) = self.lstm(embedded)
            # lstm_out: [batch size, max sequence length, hidden_dim]

            # Apply dropout
            output = self.dropout(lstm_out)

            # Fully connected layer
            output = self.fc(output[:, -1, :])
            # output: [batch size, output_dim]

            return output


        







