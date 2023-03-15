from nltk.tokenize import *

para = "this is a sentence. do you know"

print("tokenizing sentence:")
sent = sent_tokenize(para)
print(sent)

print("tokeinizing words:")
for i in range(len(sent)):
    words = word_tokenize(sent[i])
    print(words)