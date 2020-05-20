#!/usr/bin/env python
# coding: utf-8

# # Sentiment

# ### MNB
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import pickle
# print('loading transformer....')
# # load the tfidf_vectorizer from disk
# filename = 'models/MNB_vect.sav'
# MNB_vect = pickle.load(open(filename, 'rb'))
# print('loading transformer....done!')

# print('loading MNB model (86% acuracy rate)....')
# # load the selector from disk 86% accuracy
# filename = 'models/MNB_model.sav' 
# MNB_model = pickle.load(open(filename, 'rb'))
# print('loading MNB model (86% acuracy rate)....done!')

# def MNB_predict_sentiment(text):
#     """
#     expect: a string of text
#     modify: vectorize the string with 'tfidf_vectorizer' and 'selector' transformers
#     return: an int (1:'postive' ; 0:'negative')
#     """
#     text_list=[]
#     text_list.append(text)
#     raw_dtm = MNB_vect.transform(text_list)
#     pred_class = int(MNB_model.predict(raw_dtm))    
#     return pred_class

# ### SVM
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.svm import LinearSVC
# import pickle

# print('loading transformer....')
# # load the transformer from disk
# filename = 'models/SVM_vect.sav'
# SVM_vect = pickle.load(open(filename, 'rb'))
# print('loading transformer....done!')

# print('loading SVM model (89% accuracy rate)....')
# # load the model from disk  89%
# filename = 'models/SVM_model.sav'
# SVM_model = pickle.load(open(filename, 'rb'))
# print('loading SVM model (89% accuracy rate)....done!')


# def SVM_predict_sentiment(text):
#     """
#     expect: a string of text
#     modify: vectorize the string with 'tfidf_vectorizer' and 'selector' transformers
#     return: an int (1:'postive' ; 0:'negative')
#     """
#     text_list=[]
#     text_list.append(text)
#     raw_dtm = SVM_vect.transform(text_list)
#     pred_class = int(SVM_model.predict(raw_dtm))    
#     return pred_class


# ### Keras

# pip install h5py
# pip install keras
# pip install PyYAML
# pip install anvil-uplink


import keras # for sentitment model
import tensorflow as tf  # to resolve the loading issue with different version of keras
from nltk.tokenize import RegexpTokenizer
import pickle # load transformers: 'tfidf_vectorizer' and 'selector'
import dill # load language model
from collections import defaultdict # to make language model work


# load model 92%
print('loading keras model (92% accuracy)...')
model = tf.keras.models.load_model('models/kera_model_dropout_nn.h5')
print('loading keras model (92% accuracy)...done!')
# summarize model.
model.summary()


# load the tfidf_vectorizer from disk
print('loading transformers...')
filename = 'models/tfidf_vectorizer.sav'
tfidf_vectorizer = pickle.load(open(filename, 'rb'))

# load the selector from disk
filename = 'models/selector.sav'
selector = pickle.load(open(filename, 'rb'))
print('loading transformers...done!')


def keras_predict_sentiment(text):
    """
    expect: a string of text
    modify: vectorize the string with 'tfidf_vectorizer' and 'selector' transformers
    return: an int (1:'postive' ; 0:'negative')
    """
    text_list=[]
    text_list.append(text)
    raw_dtm = tfidf_vectorizer.transform(text_list)
    selected_dtm = selector.transform(raw_dtm).astype('float32')  
    pred_class = int(model.predict_classes(selected_dtm.toarray()))    
    return pred_class

   

# # Text Prediction

print('loading language model....')
# %%time
# Load models
with open('models/bigram_model.p', 'rb') as file:
   bigram_model = dill.load(file)
with open('models/trigram_model.p', 'rb') as file:
   trigram_model = dill.load(file)
# with open('models/fourgram_model.p', 'rb') as file:
#    fourgram_model = dill.load(file)
# with open('models/fivegram_model.p', 'rb') as file:
#    fivegram_model = dill.load(file)

# define tokenizer to get words
tokenizer = RegexpTokenizer(r'\w+')
print('loading language model....done!')


# function to predict the next word based on bigram model
def bigram_predict_next_word(word):
    '''
    word: a list of token
    '''
    if len(bigram_model[word[0]]) == 0:
        return None
    else:
        prob_list = bigram_model[word[0]].values()
        # find the max prob
        most_likely = max(prob_list)
        #print(most_likely)
        # predicted words
        pred_words = [word for word, prob in bigram_model[word[0]].items() if prob == most_likely]
#         pred_word = random.choice(pred_words)
    return pred_words[0]


# function to predict next word with trigram model
def trigram_predict_next_word(words):
    '''
    words: a list of token
    '''
    if len(trigram_model[words[0], words[1]]) == 0:
        last_word = words[-1]
        return bigram_predict_next_word(last_word)
    else:
        # get probabilities of next word
        prob_list = trigram_model[words[0], words[1]].values()
        # find the max prob
        most_likely = max(prob_list)
        # predicted words
        pred_words = [word for word, prob in trigram_model[words[0], words[1]].items() if prob == most_likely]
    return pred_words[0]


# def fourgram_predict_next_word(words):
#     '''
#     words: a list of token
#     '''
#     if len(fourgram_model[words[0], words[1], words[2]]) == 0:
#         last_two_words = words[-2:] 
#         return trigram_predict_next_word(last_two_words)
#     else:
#         # get probabilities of next word
#         prob_list = fourgram_model[words[0], words[1], words[2]].values()
#         # find max prob
#         most_likely = max(prob_list)
#         # get the predicted word(s)
#         pred_words = [word for word, prob in fourgram_model[words[0], words[1], words[2]].items() if prob == most_likely]
# #         pred_word = random.choice(pred_words)
#     return pred_words[0]


# # function to predict next word with 5-gram model
# def fivegram_predict_next_word(words):
#     '''
#     words: a list of token
#     '''
#     if len(fivegram_model[words[0], words[1], words[2], words[3]]) == 0:
#         last_three_words = words[-3:]
#         return fourgram_predict_next_word(last_three_words)
#     else:
#         # get probabilities of next word
#         prob_list = fivegram_model[words[0], words[1], words[2], words[3]].values()
#         # find max prob
#         most_likely = max(prob_list)
#         # predicted words
#         pred_words = [w for w, p in fivegram_model[words[0], words[1], words[2], words[3]].items() if p == most_likely]
# #         pred_word = random.choice(pred_words)
#     return pred_words[0]


# def ngram_prediction(text):
#     """
#     expect: a raw string of text
#     modify: tokenize the string and # check the length to decide to start with which model.
#                 1. if the string has 4 tokens or above, take the last four tokens as input to fivegram_model
#                 2. if the string has 3 tokens, take the list of tokens as input to fourgram_model
#                 3. if the string has 2 tokens, take the list of tokens as input to trigram_model
#                 4. if the string has 1 tokens, take the token as input to trigram_model
#     return: predicted word
#     """
#     # tokenize the words
#     user_tokens = tokenizer.tokenize(text)
#     if len(user_tokens) >= 4:
#         try:
#             return fivegram_predict_next_word(user_tokens[-4:]) # take the last four tokens
#         except:    
#             return fivegram_predict_next_word(user_tokens) # take the last four tokens
#     elif len(user_tokens) == 3:
#         return fourgram_predict_next_word(user_tokens)
#     elif len(user_tokens) == 2:
#         return trigram_predict_next_word(user_tokens)
#     elif len(user_tokens) == 1:
#         return bigram_predict_next_word(user_tokens) 
   


# for remote server AWS EC2 / Droplet
def make_prediction(text):
    """
    expect: a raw string of text
    modify: tokenize the string and # check the length to decide to start with which model.
            1. if the string has 2 tokens or above, take the last four tokens as input to trigram_model
            2. if the string has 1 token, take the list of tokens as input to bigram_model
    return: predicted word
    """
    # tokenize the words
    user_tokens = tokenizer.tokenize(text)
    if len(user_tokens) >= 2:
        try:
            return trigram_predict_next_word(user_tokens[-2:]) # take the last four tokens
        except:    
            return trigram_predict_next_word(user_tokens) # take the last four tokens
    elif len(user_tokens) == 1:
        return bigram_predict_next_word(user_tokens) 


# # Anvil
import anvil.server

anvil.server.connect("KDO33RPUPH27AGMVCZBAHU2U-PDHT24SNT663M2H7")
print('final step is running')



@anvil.server.callable
# Put the function that will be used in anvil client server (web)
# This block of code should be running forever
# The @anvil.server.callable decorator can only take one function

def app_prediction(text):
    """
    expect: a string of text
    modify: send the string to two functions:
                1. ngram_prediction
                2. keras_predict_sentiment
    return: a tuple that contains a predicted word and a predicted class
    """
    ## Sentiment Prediction
    pred_word = make_prediction(text)
    
    ## Text Prediction
    pred_class = keras_predict_sentiment(text)
        
    return pred_word, pred_class

anvil.server.wait_forever()





