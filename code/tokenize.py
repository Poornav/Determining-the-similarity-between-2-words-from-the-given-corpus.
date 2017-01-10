#import gensim





import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
#from gensim.models import Word2Vec

fp = open("tweets_filtered.txt",'r')
f = fp.read()
sentences =(sent_tokenize(f))
ans=list(map(lambda x:x.lower().strip(),sentences))
'''
tokens=[]
for sen in ans:
	words=word_tokenize(sen)
	tokens.append(words)
model = gensim.models.Word2Vec(tokens,size=32)
print "Hi",model.similarity("to","buy")
'''

words = ["modi","dubai","uae","india","aap","bjp","speech","people","delhi","pm","bjp","speech","people"]
#words=[]
for i in ans:
	words.append(i)
triples = []
unigramWordCount = {}
for i in range(len(words)):
	temp = ()
	if(unigramWordCount.has_key(words[i])):
		unigramWordCount[words[i]] += 1
	else:
		unigramWordCount[words[i]] = 1
	if(i==0):
		temp = temp + (" ",)
		temp = temp + (words[i],)
		temp = temp + (words[i+1],)
		triples.append(temp)
		continue
	if(i == len(words) - 1):
		temp = temp + (words[i-1],)
		temp = temp + (words[i],)
		temp = temp + (" ",)
		triples.append(temp)
		continue

	temp = temp + (words[i-1],)
	temp = temp + (words[i],)
	temp = temp + (words[i+1],)
	triples.append(temp)
'''
print triples
print "-------------------"
print unigramWordCount
print "-------------------"
'''
triplesCount = {}

similarityWords = ["modi","dubai","uae","india","aap","bjp","speech","people","delhi","pm"]

for i in range(len(triples)):
	if(triplesCount.has_key(triples[i][1])):
		triplesCount[triples[i][1]] += 1
	else:
		triplesCount[triples[i][1]] = 1

print triplesCount

wordPairs = {}
D = 0
for i in range(len(similarityWords)):

	for j in range(i+1,len(similarityWords)-1):
		wordpair = similarityWords[i] + " - " + similarityWords[j]
		Z = triplesCount[similarityWords[i]] + triplesCount[similarityWords[j]]
		delta = abs(triplesCount[similarityWords[i]] - triplesCount[similarityWords[j]])
		tup = [delta,Z]
		wordPairs[wordpair] = tup
		D += delta
'''
print "-------------------"
print wordPairs
'''
for key in wordPairs:
	wordPairs[key] = 1 - float(wordPairs[key][0])/wordPairs[key][1]
	#wordPairs[key] = float(wordPairs[key][0])/wordPairs[key][1]
'''
print "-------------------"
print "D = " + str(D)
'''
print wordPairs
fo=open("tok_output.txt",'w')
fo.write(str(wordPairs))
