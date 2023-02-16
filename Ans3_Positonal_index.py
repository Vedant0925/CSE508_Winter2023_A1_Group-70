### Q.3 (ii) 1.



documents=[]
pos_index=[{},{}]
zero = 0
import os
folder_path = "CSE508_Winter2023_Dataset"


for root, _, files in os.walk(folder_path):
    for file in files:
            with open(os.path.join(root, file), 'r') as f:
                doc_id = file
                content = f.read().strip().split()
                
                documents.append(content)

    

# Iterate through each document
for p in range(0,len(documents)):
    docID = p
    doc_tok = documents[p]
    docID = docID+1

    for q in range(zero,len(doc_tok)): ## Iterate through each word
        instance = q
        word = doc_tok[q]

        if word not in pos_index[zero]:  ##if word not in Index, create a new instance
            pos_index[zero][word] = {"Total count": 0, "documents list": {}}
        if docID not in pos_index[zero][word]["documents list"]:
            pos_index[zero][word]["documents list"][docID] = []
        pos_index[zero][word]["Total count"] += 1
        pos_index[zero][word]["documents list"][docID].append(instance)

pos_index = pos_index[zero]

# print(pos_index)

import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import numpy as np


### Saving and loading index

with open('PosInd\Positional_index.pkl', 'wb') as f:
    pickle.dump(pos_index, f)

# Load the inverted index from the file
with open('PosInd\Positional_index.pkl', 'rb') as f:
    loaded_index = pickle.load(f)


## PreProcessing the text in the query to match the data stored in index
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

def find_query(query): 
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


print("Enter Number of Queries Followed By Queries")   ##Taking the query input 
a = int(input())
queries=[]
for i in range(a):
    queries.append(str(input()))

i = 0
for j in queries:
    i=i+1
    processed_q=pre_process(j)
    list=find_query(processed_q)
    print("Number of Documents Retrived for Query "+str(i)+": "+str(len(list)))
    print("Names of Documents Retrived for Query : ", end=" ")

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
        


