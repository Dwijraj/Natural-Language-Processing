file=open('dummytext.txt','rt')
text=file.read()
file.close()
#print(text)
from nltk import sent_tokenize
Sentences=sent_tokenize(text)
print(Sentences[0])
Sentences[0]=Sentences[0][3:]
print(Sentences[0])
from nltk import word_tokenize
lines=[]
for sent in Sentences:
    Words=word_tokenize(sent)
    lines.append(Words)  
print(lines[0])
from nltk import SnowballStemmer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
Stemmer=SnowballStemmer('english')
Sentences=[]
for l in lines:
    stemmedW=[]
    for w in l:
        if w not in stop_words and w.isalpha():
            stemmedW.append(Stemmer.stem(w))
    Sentences.append(stemmedW)
print(Sentences[0])
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import pyplot
sentences=Sentences
# train model
model = Word2Vec(sentences, min_count=1)
# fit a 2D t-SNE model to the vectors
X = model[model.wv.vocab]
tsne = TSNE(n_components=2)
result = tsne.fit_transform(X)
# create a scatter plot of the projection
pyplot.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
    pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
pyplot.show()
