import os
import string
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords

and_op = ''

or_op = ''

not_op = ''

path = '/Users/vedant/Downloads/Work'
index = {}
stop_words = set(stopwords.words('english'))

for file_name in os.listdir(path):
    with open(os.path.join(path, file_name)) as f:
        for line in f:
            for word in line.strip().split():
                word = word.lower()
                if word not in stop_words and word not in string.punctuation:
                    if word in index:
                        index[word].add(file_name)
                    else:
                        index[word] = {file_name}

num_queries = int(input("Enter number of queries: "))
queries = []

for i in range(num_queries):
    query = input(f"Enter query {i+1}: ")
    operations = input("Enter operations (separated by commas): ")
    queries.append((query, operations))

for query, operations in queries:
    op_list = operations.split(',')
    documents = set()
    output_query = ""
    not_op = False  
    for i, word in enumerate(query.split()):
        if word.lower() in stop_words or word in string.punctuation:
            continue
        if word == "NOT" and i < len(query.split()) - 1:
            if not documents:
                documents = set(path)
            not_op = True
            continue  
        if not_op:
            not_op = False
            output_query += "NOT "
            
            if operator == "AND":
                documents = documents.intersection(index[word])
                
            elif operator == "OR":
                documents = documents.union(index[word])
                
            elif operator == "AND NOT":
                documents = documents.difference(index[word])
                
            elif operator == "OR NOT":
                documents = documents.union(set(path).difference(index[word]))
                
        elif word in op_list:
            operator = word
            output_query += f" {operator} "
        elif not_op:
            not_op = False
            output_query += "NOT "
            if operator == "AND":
                documents = documents.intersection(index[word.lower()])
                
            elif operator == "OR":
                documents = documents.union(index[word.lower()])
                
            elif operator == "AND NOT":
                documents = documents.difference(index[word.lower()])
                
            elif operator == "OR NOT":
                documents = documents.union(set(path).difference(index[word.lower()]))
                
        elif word.lower() in index:
            if not documents:
                documents = index[word.lower()]
                output_query += word
                
            elif operator == "AND":
                documents = documents.intersection(index[word.lower()])
                output_query += f" {operator} {word}"
                
            elif operator == "OR":
                documents = documents.union(index[word.lower()])
                output_query += f" {operator} {word}"
                
            elif operator == "AND NOT":
                documents = documents.difference(index[word.lower()])
                output_query += f" {operator} {word}"
                
            elif operator == "OR NOT":
                documents = documents.union(set(path).difference(index[word.lower()]))
                output_query += f" {operator} {word}"
    
    print(f'Number of documents retrieved: {len(documents)}')
    
    print(f'Names of docs retrieved: {documents}')
    
    print(f'Number of comparisons required: {len(query.split()) - query.count("NOT") - len(op_list)}\n')
