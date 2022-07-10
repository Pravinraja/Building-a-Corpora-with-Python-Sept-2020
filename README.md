# Building-a-Corpora-with-Python-Sept-2020
A corpus is a giant database of text (literature, tweets, newspapers, rss feeds, etc). There are many different corpora, and all of them have different texts. "Corpus linguistics" is the study of the rules/patterns/etc. of language using text from these databases.

Tasks Completed: 
Problem 1)

import nltk

nltk.download()

Scroll through the list and find a corpus to download (do not use brown or inaugural) 
https://www.nltk.org/book/ch02.html

Answer the following:

What directory does the corpus download to?
How many Files are there for that Corpus?
In 3-4 sentences, what is the purpose of that corpus and what genres does it cover?

Problem 2)

Below are examples of how to access your corpus

Example	Description
fileids()	the files of the corpus
fileids([categories])	the files of the corpus corresponding to these categories
categories()	the categories of the corpus
categories([fileids])	the categories of the corpus corresponding to these files
raw()	the raw content of the corpus
raw(fileids=[f1,f2,f3])	the raw content of the specified files
raw(categories=[c1,c2])	the raw content of the specified categories
words()	the words of the whole corpus
words(fileids=[f1,f2,f3])	the words of the specified fileids
words(categories=[c1,c2])	the words of the specified categories
sents()	the sentences of the whole corpus
sents(fileids=[f1,f2,f3])	the sentences of the specified fileids
sents(categories=[c1,c2])	the sentences of the specified categories
abspath(fileid)	the location of the given file on disk
encoding(fileid)	the encoding of the file (if known)
open(fileid)	open a stream for reading the given corpus file
root	if the path to the root of locally installed corpus
readme()	the contents of the README file of the corpus

Answer the following:

How many categories are in your corpus?
How many sentences are in the corpus?
How many sentences are in each category?
For instance for brown you can import it by

from nltk.corpus import brown
brown.[function] 
brown.raw()

Problem 3)

first: pip install matplotlib

import nltk
from nltk.corpus import inaugural
word1='country'
word2='city'
cfd = nltk.ConditionalFreqDist((target, fileid[:4])for fileid in inaugural.fileids()for w in inaugural.words(fileid)for target in [word1, word2] if w.lower().startswith(target))
cfd.plot()

Try finding two words to replace country and city. Find one word that is becoming more popular in recent years (2009) and one that was popular but is not longer.
