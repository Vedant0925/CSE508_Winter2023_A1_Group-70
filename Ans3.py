
import os
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import numpy as np


# Load the inverted index from the file
with open('Positional_index.pkl', 'rb') as f:
    loaded_index = pickle.load(f)


def pre_process(text):
   
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [token for token in tokens if token not in string.punctuation] 
    tokens = [token for token in tokens if token.strip()]
    processed=""
    for i in tokens:
        processed=processed+" "+i
    return processed

def find_query_pos(query): 
    words = query.split()
    uniqueDocIds = []
    doc_list=[]
    
    doc_list = []
    for i in range(len(query.split()) - 1): ## taking the combinations of the phrase as 2 words
        word1 = query.split()[i]
        word2 = query.split()[i+1]
        if word1 in loaded_index and word2 in loaded_index:  ## checking if both words in index 
            for docID in loaded_index[word1]["documents list"]:
                if docID in loaded_index[word2]["documents list"]: ## Checking if both words are present in same document 
                    for instance1 in loaded_index[word1]["documents list"][docID]:
                        for instance2 in loaded_index[word2]["documents list"][docID]: ## taking the instance of the words
                            if instance2 == instance1 + 1: ## Checking if both words are consecutive and together or not
                                doc_list.append(docID) 
    doc_list = np.unique(doc_list)
    doc_list =doc_list
                                
    return doc_list


def load_index(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


def find_query_iv(query):
  
    index=load_index("b_indexfile.pkl")

    query_bigrams = [query[i:i+2] for i in range(len(query)-1)]
    doc_sets = []
    for bigram in query_bigrams:
        if bigram in index:
            doc_sets.append(index[bigram])
        else: 
            doc_sets.append(set())
    result_set = set.intersection(*map(set,doc_sets))
    return(sorted(result_set))


print("Enter Number of Queries Followed By Queries")   ##Taking the query input 
a = int(input())
queries=[]
for i in range(a):
    queries.append(str(input()))

i = 0
for j in queries:
    i=i+1
    processed_q=pre_process(j)

    result=find_query_iv(processed_q)
    print("Number of Documents Retrived for Query using bigram inverted index"+str(i)+":"+str(len(result)))
    print("Names of Documents Retrived for Query using bigram inverted index"+str(i)+":"+str(result))

    list=find_query_pos(processed_q)
    print("Number of Documents Retrived for Query using Positional Index "+str(i)+": "+str(len(list)))
    print("Names of Documents Retrived for Query using Positional Index : ", end=" ")

    for k in range(0,len(list)):
        if (k <10):
            url2 = "cranfield000"+str(list[k])
        elif (k<100):
            url2= "cranfield00"+str(list[k])
        elif (k<1000):
            url2 = "cranfield0"+str(list[k])
        elif (k<10000):
            url2 = "cranfield"+str(list[k])
        if(k==len(list)-1):
            print(url2, end=" ")
            break
        print(url2 , end=" ,   ")
    
    print("\n")
        