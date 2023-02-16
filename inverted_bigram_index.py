import os
import nltk
import re
import string
import pickle

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



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

def save_index(index, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(index, f)

def load_index(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)

def create_index(directory):
    index = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            contents = file.read()
            d_bigrams = [contents[i:i+2] for i in range(len(contents)-1)]
            for bigram in d_bigrams:
                if bigram not in index:
                     index[bigram] = []
                index[bigram].append(filename)
                 
    return(index)

def find_query(query):
  
    index=load_index("indexfile")

    query_bigrams = [query[i:i+2] for i in range(len(query)-1)]
    doc_sets = []
    for bigram in query_bigrams:
        if bigram in index:
            doc_sets.append(index[bigram])
        else: 
            doc_sets.append(set())
    result_set = set.intersection(*map(set,doc_sets))
    return(sorted(result_set))
    



if __name__ == '__main__':
    import nltk
    nltk.download('stopwords')
    path ="Work"
    index=create_index(path)
    save_index(index,"indexfile")
    print("Enter Number of Queries Followed By Queries")
    a = int(input())
    queries=[]
    for i in range(a):
        queries.append(str(input()))
    i=0
    for j in queries:
        i=i+1
        processed_q=pre_process(j)
        result=find_query(processed_q)
        print("Number of Documents Retrived for Query "+str(i)+":"+str(len(result)))
        print("Names of Documents Retrived for Query "+str(i)+":"+str(result))
        



  


   