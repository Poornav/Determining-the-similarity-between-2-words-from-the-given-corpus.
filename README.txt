Determining-the-similarity-between-2-words-from-the-given-corpus.


We have built a system based on the principles of Language model and
Continuous Bag of Words (CBOW) to determine the similarity between 2 words from the
given corpus. We then evaluate the performance by comparing this with the scores
produced by word2vec.


How to run?
tokenize.py and wordtovec.py are run in a terminal.
Then the output could be analysed be seeing the output files "wordtovec_output.txt" and "tok_output.txt"


Dataset -  A corpus of tweets 


Algorithm :


1. Clean the tweets: Replace hashtags, screen names, urls, RT, emoticons with

suitable words (token type)

2. Convert the tweets to lowercase

3. Apply preprocessing like lemmatization or stemming

4. Construct a vocabulary

5. Build unigram counts

6. Choose a subset of V based on a minimum threshold count for the unigrams.

Replace the words that have less than the threshold counts with a special

symbol.

7. From the preprocessed corpus, select a minimum of 10 word pairs for evaluating

similarity between them

8. Extract all triples from the preprocessed corpus – let us call this a set T. For each t

in T measure the counts c.

9. For each word pair in the list chosen in step 7, wi and wj, for each triple in T:

a. Assign count(wi,, t) = c if wi is the center word of t

b. Assign count(wj,, t) = c if wj is the center word of t

c. Compute delta(t) = abs(count(wi,, t) - count(wj,, t))

10. Compute the sum of all deltas generated in step 9 and let this be D

11. Add up all the counts obtained from steps 9(a) and 9(b) and let this be Z

12. Compute and return the score (1 – D/Z)

13. Train the word2vec with the preprocessed corpus

14. For the same word pairs wi and wj compute similarity using word2vec

15. Normalize the similarity score obtained in step 14 to have the range (0, 1)

16. Prepare a table and tabulate for each word pairs chosen in step 7 the scores

produced by the counting algorithm and the word2vec