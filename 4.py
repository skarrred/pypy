import re
from nltk.tokenize import *

#using nltk
sentence1 = "this is a dummy sentence"
print(RegexpTokenizer('\s',gaps=True).tokenize(sentence1))

#using RE
sentence2 = "sentences have a lot of ees in them"
print(re.split('e', sentence2))
print(re.split('[s,n]', sentence2))