#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:23:47 2020

@author: jasonmaloney
"""
import os

def stopword_remover(document):
    nltkstopwords = stopwords.words('english')
    #addl_stopwords = ['subject', '']
    #all_stopwords = nltkstopwords + addl_stopwords
    cleaned_list = []
    for word in document:
        if word not in nltkstopwords:
            cleaned_list.append(word)
    return cleaned_list 

# function to read  files, training data
def readtrain(dirPath,limitStr):
  # convert the limit argument from a string to an int
  limit = int(limitStr)
  
  # start lists for positive and negativetraining reviews
  train_pos = []
  train_neg = []
  os.chdir(dirPath)
  # process all files in directory that end in .txt up to the limit
  #    assuming that the emails are sufficiently randomized
  for file in os.listdir("./pos"):
    if (file.endswith(".txt")) and (len(train_pos) < limit):
      # open file for reading and read entire file into a string
      f = open("./pos/"+file, 'r', encoding = "utf-8")
      train_pos.append (f.read())
      f.close()
  for file in os.listdir("./neg"):
    if (file.endswith(".txt")) and (len(train_neg) < limit):
      # open file for reading and read entire file into a string
      f = open("./neg/"+file, 'r', encoding = "utf-8")
      train_neg.append (f.read())
      f.close() 
  return train_pos, train_neg
  print ("Number of positive reviews files:",len(train_pos))
  print ("Number of negative files:",len(train_neg))
  
  
# function to read  files, test data
def readtest(dirPath,limitStr):
  # convert the limit argument from a string to an int
  limit = int(limitStr)
  # start lists for positive and negative test reviews
  test_pos = []
  test_neg = []
  os.chdir(dirPath)
  # process all files in directory that end in .txt up to the limit
  #    assuming that the emails are sufficiently randomized
  for file in os.listdir("./pos"):
    if (file.endswith(".txt")) and (len(test_pos) < limit):
      # open file for reading and read entire file into a string
      f = open("./pos/"+file, 'r', encoding = "utf-8")
      test_pos.append (f.read())
      f.close()
  for file in os.listdir("./neg"):
    if (file.endswith(".txt")) and (len(test_neg) < limit):
      # open file for reading and read entire file into a string
      f = open("./neg/"+file, 'r', encoding = "utf-8")
      test_neg.append (f.read())
      f.close()
  return test_pos, test_neg
  print ("Number of positive review test files:",len(test_pos))
  print ("Number of negative review test files:",len(test_neg))

# read in training data
train_pos, train_neg = readtrain("/Users/jasonmaloney/Documents/Syracuse/IST 736 Text Mining/Text Mining Project/aclImdb/train", 20)

# read in test data
test_pos, test_neg = readtest("/Users/jasonmaloney/Documents/Syracuse/IST 736 Text Mining/Text Mining Project/aclImdb/test", 20)

# view the data
for i in range(len(train_pos)):
    train_pos[i] = re.sub(r"<br\s/><br\s/>", ' ', train_pos[i])
    print(i, ":-----", train_pos[i])

# clean the data
import re # regular expressions
# need to get rid of  <br /><br />
for i in range(len(train_pos)):
    train_pos[i] = re.sub(r"<br\s/><br\s/>", ' ', train_pos[i])
    print(i, ":-----", train_pos[i])

def cleantext(lst):
    for i in range(len(lst)):
        lst[i] = re.sub(r"<br\s/><br\s/>", " ", lst[i])
    return lst

# clean the sets
clean_train_neg = cleantext(train_neg)
clean_train_pos = cleantext(train_pos)
clean_test_neg = cleantext(test_neg)
clean_test_pos = cleantext(test_pos)

for i in range(len(clean_train_pos)):
    print(clean_train_pos[i])

# attach negative sentiment to reviews
def negsent(neglist): 
    neg_doc = []
    for review in neglist:
        neg_doc.append((review, "neg"))
    return(neg_doc)

# attach positive sentiemnt to reviews
def possent(poslist):
    pos_doc = []
    for review in poslist:
        pos_doc.append((review, "pos"))
    return(pos_doc)

# get the lists with the sentiments
train_neg_docs = negsent(clean_train_neg)
train_pos_docs = possent(clean_train_pos)        
test_neg_docs = negsent(clean_test_neg)
test_pos_docs = possent(clean_test_pos)

# combine train and test sets
train_set = train_neg_docs + train_pos_docs
test_set = test_neg_docs + test_pos_docs

# combine pos and neg sets
pos_rev = clean_train_pos + clean_test_pos
neg_rev = clean_train_neg + clean_test_neg

# Count Vectorizer
from sklearn.feature_extraction.text import CountVectorizer as CV
import numpy as np
import pandas as pd 

# get frequency counts
word_frequency_vectorizer = CV(binary = False)

# apply it to positive reviews
pos_freq_dtm = word_frequency_vectorizer.fit_transform(pos_rev)

# convert dtm to df
pos_freq_df = pd.DataFrame(pos_freq_dtm.toarray(), columns = word_frequency_vectorizer.get_feature_names())
pos_freq_df.shape


# get the most frequent words in pos and neg reviews
from nltk import FreqDist
from nltk.corpus import stopwords

all_pos_words = []
filt_pos_words = []
for review in pos_rev:
    tokens = nltk.word_tokenize(review)
    words = stopword_remover(tokens)
    for word in words:
        filt_pos_words.append(word)
    for word in tokens:
        all_pos_words.append(word)

# all positive words
pos_word_counts = nltk.FreqDist(all_pos_words)    
pos_most_common = pos_word_counts.most_common(50)    
pos_most_common

# stop words filtered
pos_filt_counts = nltk.FreqDist(filt_pos_words)
pos_filt_common = pos_filt_counts.most_common(50)
pos_filt_common

all_neg_words = []
filt_neg_words = []
for review in neg_rev:
    tokens = nltk.word_tokenize(review)
    words = stopword_remover(tokens)
    for word in words:
        filt_neg_words.append(word)
    for word in tokens:
        all_neg_words.append(word)

# all positive words
neg_word_counts = nltk.FreqDist(all_neg_words)    
neg_most_common = neg_word_counts.most_common(50)    
neg_most_common

# stop words filtered
neg_filt_counts = nltk.FreqDist(filt_neg_words)
neg_filt_common = neg_filt_counts.most_common(50)
neg_filt_common

# create a data frame columns - pos words and counts
pos_words = []
pos_count = []
for word, count in pos_filt_common:
    pos_words.append(word)
    pos_count.append(count)
neg_words = []
neg_count = []
for word, count in neg_filt_common:
    neg_words.append(word)
    neg_count.append(count)

most_common_df = pd.DataFrame({'pos_word':pos_words, 'pos_count':pos_count, 'neg_word':neg_words, 'neg_count':neg_count})
most_common_df

# bar plot of the most common words in pos and neg reviews
import matplotlib.pyplot as plt
plt.bar(x = 'pos_word', height = pos_count, data = most_common_df)
plt.xticks(rotation = 'vertical')
plt.title("Most Common Words in Positive Reviews")
plt.show()

plt.bar(x = 'neg_word', height = neg_count, data = most_common_df)
plt.xticks(rotation = 'vertical')
plt.title("Most Common Words in Negative Reviews")
plt.show()








# this is just a reference --- unused!
  # create list of mixed spam and ham email documents as (list of words, label)
  emaildocs = []
  hamdocs = []
  spamdocs = []
  
  # add all the spam
  for spam in spamtexts:
    tokens = nltk.word_tokenize(spam)
    # filter stop words
    #word = stopword_remover(tokens)
    emaildocs.append((tokens, 'spam'))
    #emaildocs.append((tokens, 'spam'))
    spamdocs.append(tokens)
  
  # add all the regular emails
  for ham in hamtexts:
    tokens = nltk.word_tokenize(ham)
    # filter stop words
    #word = stopword_remover(word)
    #emaildocs.append((tokens, 'ham'))
    emaildocs.append((tokens, 'ham'))
    hamdocs.append(tokens)
  
  # randomize the list
  random.shuffle(emaildocs)

  # create a list that has the labels  
  lab = [lab for email, lab in emaildocs]
  labels = list(set(lab))