# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 19:17:16 2020

@author: Maya
"""

# Gates code for FP 

## Textmining Naive Bayes Example
import nltk
import pandas as pd
import sklearn
import re  
from sklearn.feature_extraction.text import CountVectorizer

#Convert a collection of raw documents to a matrix of TF-IDF features.
#Equivalent to CountVectorizer but with tf-idf norm
from sklearn.feature_extraction.text import TfidfVectorizer


from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
## For Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import os
import os.path

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import string
import numpy as np

df =  pd.read_csv("C:/Users/aivii/programsmm/FP736/corpus/combined_csv1.csv")
print(df.head)
df = df.drop(df.columns[[0]], axis=1) # remove the first column 
print(df.head)


## Generating one row  
rows = df.sample(frac =.25) 
  
## Checking if sample is 0.25 times data or not 
  
if (0.25*(len(df))== len(rows)): 
    print( "Cool") 
    print(len(df), len(rows)) 
  
## Display 
print(rows)


rows.to_csv(r'C:\Users/aivii\programsmm\FP736\COMBINED_TEST_TR.csv', index = False)

RawfileName0="C:/Users/aivii/programsmm/FP736/COMBINED_TEST_TR.csv"

## This file has a header. 
## It has "setinment" and "review" on the first row.

## We will create a list of labels and a list of reviews
AllReviewsList=[]
AllLabelsList=[]

with open(RawfileName0,'r', encoding="utf8") as FILE:
    FILE.readline() # skip header line - skip row 1
    ## This reads the line and so does nothing with it
    for row in FILE:
        NextLabel,NextReview=row.split(",", 1)
        #print(Label)
        #print(Review)
        AllReviewsList.append(NextReview)
        AllLabelsList.append(NextLabel)

#print(AllReviewsList)
#print(AllLabelsList) # all the labels 

## CountVectorizer
My_CV1=CountVectorizer(input='content',
                        stop_words='english',
                        max_features=100
                        
                        )
## Tfidf Vectorizer
My_TF1=TfidfVectorizer(input='content',
                        stop_words='english',
                        max_features=100
                        
                        )


## NOw I can vectorize using my list of complete paths to my files
X_CV1=My_CV1.fit_transform(AllReviewsList)
X_TF1=My_TF1.fit_transform(AllReviewsList)

print(My_CV1.vocabulary_)
print(My_TF1.vocabulary_)


ColNames=My_TF1.get_feature_names()


## OK good - but we want a document topic model A DTM (matrix of counts)
DataFrame_CV=pd.DataFrame(X_CV1.toarray(), columns=ColNames)
DataFrame_TF=pd.DataFrame(X_TF1.toarray(), columns=ColNames)

# Update row names with file names
MyDict = {}
for i in range(0, len(AllLabelsList)):
    MyDict[i] = AllLabelsList[i]

print("MY DICT", MyDict)

DataFrame_CV = DataFrame_CV.rename(MyDict, axis = "index")
DataFrame_TF = DataFrame_TF.rename(MyDict, axis = "index")
DataFrame_CV.index.name = 'LABEL'
DataFrame_TF.index.name = 'LABEL'

## Drop/remove columns not wanted
print(DataFrame_CV.columns)

def Logical_Numbers_Present(anyString):
    return any(char.isdigit() for char in anyString)


for nextcol in DataFrame_CV.columns:
    
    Result=str.isdigit(nextcol) ## Fast way to check numbers
    
    LogResult=Logical_Numbers_Present(nextcol)
    ## The above returns a logical of True or False
    
    ## The following will remove all columns that contains numbers
    if(LogResult==True):
        #print(LogResult)
        #print(nextcol)
        DataFrame_CV=DataFrame_CV.drop([nextcol], axis=1)
        DataFrame_TF=DataFrame_TF.drop([nextcol], axis=1)

   
    elif(len(str(nextcol))<=3):
        print(nextcol)
        DataFrame_CV=DataFrame_CV.drop([nextcol], axis=1)
        DataFrame_TF=DataFrame_TF.drop([nextcol], axis=1)
    
DataFrame_CV1 = DataFrame_CV.reset_index()
DataFrame_TF1 = DataFrame_TF.reset_index()

print(DataFrame_CV1)
print(DataFrame_TF1)

#DataFrame_CV1.to_csv(r'C:\Users/aivii\programsmm\HW3_736\combined_tst_tr_clean_cv.csv', index = False)
#DataFrame_TF1.to_csv(r'C:\Users/aivii\programsmm\HW3_736\combined_test_tr_clean_tf.csv', index = False)

## Train, Test split
from sklearn.model_selection import train_test_split

TrainDF, TestDF = train_test_split(DataFrame_CV1, test_size=0.3)

## Now we have a training set and a testing set. 
print("\nThe training set is:")
print(TrainDF)
print("\nThe testing set is:")
print(TestDF)

## IMPORTANT - YOU CANNOT LEAVE LABELS ON THE TEST SET

## Save labels
TestLabels=TestDF["LABEL"]
#print(TestLabels)

## remove labels
## Make a copy of TestDF
CopyTestDF=TestDF.copy()
TestDF = TestDF.drop(["LABEL"], axis=1)
print(TestDF)

## DF seperate TRAIN SET from the labels
TrainDF_nolabels=TrainDF.drop(["LABEL"], axis=1)
#print(TrainDF_nolabels)
TrainLabels=TrainDF["LABEL"]
#print(TrainLabels)

#####################################################################
# Naive Bayes
#####################################################################
from sklearn.naive_bayes import MultinomialNB

MyModelNB= MultinomialNB()

MyModelNB.fit(TrainDF_nolabels, TrainLabels)
Prediction = MyModelNB.predict(TestDF)
print("\nThe prediction from NB is:")
print(Prediction)
print("\nThe actual labels are:")
print(TestLabels)


## confusion matrix
from sklearn.metrics import confusion_matrix

cnf_matrix = confusion_matrix(TestLabels, Prediction)
print("\nThe confusion matrix is:")
print(cnf_matrix)

print(np.round(MyModelNB.predict_proba(TestDF),2))

from sklearn import metrics

print(metrics.classification_report(TestLabels, Prediction))
print(metrics.confusion_matrix(TestLabels, Prediction))

#####################################################################
# SVM
#####################################################################

from sklearn.svm import LinearSVC

SVM_Model1=LinearSVC(C=600, multi_class="crammer_singer")
SVM_Model1.fit(TrainDF_nolabels, TrainLabels)

print("SVM prediction:\n", SVM_Model1.predict(TestDF))
print("Actual:")
print(TestLabels)

SVM_matrix = confusion_matrix(TestLabels, SVM_Model1.predict(TestDF))
print("\nThe confusion matrix is:")
print(SVM_matrix)
print("\n\n")


#--------------other kernels

## RBF-----------------------------------------------------------------------
SVM_Model2=sklearn.svm.SVC(C=10, kernel='rbf', degree=3, gamma="scale")
SVM_Model2.fit(TrainDF_nolabels, TrainLabels)

print("SVM prediction:\n", SVM_Model2.predict(TestDF))
print("Actual:")
print(TestLabels)

SVM_matrix = confusion_matrix(TestLabels, SVM_Model2.predict(TestDF))
print("\nThe confusion matrix is:")
print(SVM_matrix)
print("\n\n")

## POLY---------------------------------------------------------------------
SVM_Model3=sklearn.svm.SVC(C=1.0, kernel='poly', degree=3, gamma="scale")
SVM_Model3.fit(TrainDF_nolabels, TrainLabels)

print("SVM prediction:\n", SVM_Model3.predict(TestDF))
print("Actual:")
print(TestLabels)

SVM_matrix = confusion_matrix(TestLabels, SVM_Model3.predict(TestDF))
print("\nThe confusion matrix is:")
print(SVM_matrix)
print("\n\n")


##################################################################
# Decision Tree
##################################################################

from sklearn import tree

## Recall:
print(TestLabels.head())
print(TestDF.head())
print(TrainDF_nolabels.head())
print(TrainLabels.head())


MyTreeModel= tree.DecisionTreeClassifier().fit(TrainDF_nolabels,TrainLabels)
Tree_Predictions=MyTreeModel.predict(TestDF)
print(MyTreeModel)
print("Predicted results: \n",Tree_Predictions)
print("Actual labels: \n", list(TestLabels))

###Confusion Matrix
Tree_conf_Mat = confusion_matrix(TestLabels, Tree_Predictions)
print("\nThe confusion matrix is:")
print(Tree_conf_Mat)
print("\n\n")


##### Plot the tree
tree.plot_tree(MyTreeModel.fit(TestDF, TestLabels),
               class_names=["n","p"]) 

import graphviz 
TreeDetails = tree.export_graphviz(
                    MyTreeModel, 
                    out_file=None, 
                    #feature_names=,  
                    class_names=["n","p"],
                    filled=True,
                    rounded=True, 
                    special_characters=True 
                    )

graph = graphviz.Source(TreeDetails) 
#graph
graph.render("MyTree") ## This creates a pdf file 
## that contains the tree plot. 
