import nltk
#import word2vec
from gensim.models import Word2Vec
import gensim
import string
import os

def callfile(path):
	ls=[]
	for dirpath,dirnames,filenames in os.walk(path):
		for filename in filenames:
			#print(filename)
			fp=open(path+filename,"r")		
			fp=fp.read()
			ans=nltk.sent_tokenize(fp)
			ans=list(map(lambda x:x.lower().strip(),ans))
			ls=ls+ans
			#print(ls)
	tokens=[]
	for sentences in ls:
		words=nltk.word_tokenize(sentences)
		tokens.append(words)
	
	return tokens



tok=callfile("datasets/")
#print(tok)
#word2vec.word2vec(tok, size=8)
model = gensim.models.Word2Vec(tok,size=32)
pairs = []
similarityWords = ["modi","dubai","uae","india","aap","bjp","speech","people","delhi","pm"]

for i in range(len(similarityWords)):

	for j in range(i+1,len(similarityWords)-1):
		t = (similarityWords[i],similarityWords[j])
		pairs.append(t)
#pairs=[('modi','dubai'),('modi','india'),('modi','aap'),('modi','delhi'),('aap','dubai'),('modi','speech'),('modi','people'),('aap','speech')]
fo=open("wordtovec_output.txt",'w')
for val in pairs:
	print val[0],val[1],model.similarity(val[0],val[1])
	fo.write(str(val[0])+", "+str(val[1])+","+str(model.similarity(val[0],val[1])))

#print model["concerned"]
