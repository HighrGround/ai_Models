import transformers
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from datasets import load_dataset


#this aims to make or take a pretrained model adding more relevant raining data
# collected from a target using the converted amass. software see documentation for futher comments

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=2)
dataset = load_dataset("glue", "mrpc")
def tokenize(batch):
  return tokenizer(batch["sentence1"], batch["sentence2"], padding=True, truncation=True)

dataset = dataset.map(tokenize, batched=True)
#dataset.rename_column("label", "labels")
dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])


train_dataset = dataset["train"]
val_dataset = dataset["validation"]
test_dataset = dataset["test"]


#all this is taken from the maskeshift document if want notes they exist there
'''
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.embedding = nn.Embedding(input_vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=5, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.relu = nn.ReLU()
        self.tanh = nn.tanh()
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


        


#def data_gathering():
    '''