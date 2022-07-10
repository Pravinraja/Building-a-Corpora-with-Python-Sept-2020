#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Problem 1
#1	C:\Users\Prav\AppData\Roaming\nltk_data is the download directory
#2	 I chose the movie reviews corpus. In there are 2 folders with 2,001 files
#3	The point of this corpus is to categorize 
#movies as positive or negative in two subfolders, each text 
#file in the folder contain a review of the movie along with the sample plot. 
#This falls under the NLP category text classification. 
import nltk


# In[14]:


# Problem 2
# How many categories are in your corpus?
from nltk.corpus import movie_reviews
movie_reviews.categories()
# Answer was 2
# ['neg', 'pos']


# In[15]:


# Problem 2
# How many sentences are in the corpus?
movie_text = movie_reviews.raw()
tokens = nltk.sent_tokenize(movie_text)
count=0
for t in tokens:
    print (t, "\n")
    count = count + 1 
print(f'the number of sentences in the movie_reviews corpus is {count}')
#the total sentence count was 71360


# In[16]:


#Problem 2
#How many sentences are in each category?
from nltk.corpus import movie_reviews as mr
poslearn1 = mr.sents(categories="pos")
poslearn2 = mr.sents(categories="neg")
print(poslearn1)
print(poslearn2)
count1=0
for t in poslearn1:
    #print ("positive review", "\n")
    count1 = count1 + 1 
print(f'sentences for positive category is {count1}')
count2=0
for t in poslearn2:
    #print ("negative review", "\n")
    count2 = count2 + 1 
print(f'sentences for negative category is {count2}')
#sentences for positive category is 36037
#sentences for negative category is 35495


# In[18]:


#Problem 3
from nltk.corpus import movie_reviews
word1='fight' 
word2='crime' 
cfd = nltk.ConditionalFreqDist((target, fileid[:4])for fileid in movie_reviews.fileids()for w in movie_reviews.words(fileid)for target in [word1, word2] if w.lower().startswith(target))
cfd.plot()


# In[ ]:




