import torch
from transformers import pipeline


"""
chs = words
for ch1, ch2 in zip(chs, chs[1:]):
    bigram = (ch1, ch2)
    b[bigram] = b.get(bigram, 0) +1

#basic code for the bigram model
"""

#classifier = pipeline("sentiment-analysis")
classifier = pipeline("text-generation", model="sentiment-analysis")
#another example using a specific model

res = classifier(
    "this is some text hopefully to train on",
    max_length=30,
    num_return_sequences=2,
    )
#analyising the given object to preproces the message by tokenizing the text

print(res)



stoi =