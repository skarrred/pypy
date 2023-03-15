from wordcloud import WordCloud
from matplotlib import pyplot as plt

text = "Dobby is a free Elf!. Dobby is from the wizarding world of harry potter"
wc = WordCloud().generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wc)
plt.axis("off")
plt.show()