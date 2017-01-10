__author__ = 'ghazanfar'

import re

lst = []

with open('tweets.txt', 'r') as f:
    for l in f:
        l = l.replace('RT', '').strip() #removes RT s
        l = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', l) # removes urls
        l = ' '.join([i  for i in l.split() if not i.startswith('#')]) #remove #
        l = ' '.join([i  for i in l.split() if not i.startswith('@')]) # remove @
        l = re.sub(r'[:;8B=Xx][>cCoO-]?[0O)(>D3PpdXx|/\\\]]', '', l) # removes emoticons [eyes][nose][mouth]
        l = l.lower()
        lst.append(l)
        if len(lst) > 10000:    #write in batches for better performance
            with open('tweets_out.txt', 'w') as outF:
                outF.write('\n'.join(lst))
            lst = []
with open('tweets_out.txt', 'w') as outF:
    outF.write('\n'.join(lst))
