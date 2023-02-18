import os
import string
import nltk
import pickle

nltk.download('stopwords')

from nltk.corpus import stopwords

and_op = ''

or_op = ''

not_op = ''

path = '/Users/vedant/Downloads/Work'
file_path = os.path.expanduser('~/inverted_index.pickle')
stop_words = set(stopwords.words('english'))

def load_inverted_index(file_path):
    with open(file_path, 'rb') as f:
        inverted_index = pickle.load(f)
    return inverted_index
inverted_index=load_inverted_index(file_path)
num_queries = int(input("Enter number of queries: "))
queries = []

for i in range(num_queries):
    query = input(f"Enter query {i + 1}: ")
    operations = input("Enter operations (separated by commas): ")
    queries.append((query, operations))

for i, (query, operations) in enumerate(queries):

    op_list = operations.split(',')
    documents = set()
    output_query = ""
    not_op = False
    for j, word in enumerate(query.split()):
        if word.lower() in stop_words or word in string.punctuation:
            continue
        if word == "NOT" and j < len(query.split()) - 1:
            if not documents:
                documents = set(path)
            not_op = True
            continue
        if not_op:
            not_op = False
            output_query += "NOT "

            if operator == "AND":
                documents = documents.intersection(inverted_index[word])

            elif operator == "OR":
                documents = documents.union(inverted_index[word])

            elif operator == "AND NOT":
                documents = documents.difference(inverted_index[word])

            elif operator == "OR NOT":
                documents = documents.union(set(path).difference(inverted_index[word]))

        elif word in op_list:
            operator = word
            output_query += f" {operator} "
        elif not_op:
            not_op = False
            output_query += "NOT "
            if operator == "AND":
                documents = documents.intersection(inverted_index[word.lower()])

            elif operator == "OR":
                documents = documents.union(inverted_index[word.lower()])

            elif operator == "AND NOT":
                documents = documents.difference(inverted_index[word.lower()])

            elif operator == "OR NOT":
                documents = documents.union(set(path).difference(inverted_index[word.lower()]))

        elif word.lower() in inverted_index:
            if not documents:
                documents = inverted_index[word.lower()]
                output_query += word

            elif operator == "AND":
                documents = documents.intersection(inverted_index[word.lower()])
                output_query += f" {operator} {word}"

            elif operator == "OR":
                documents = documents.union(inverted_index[word.lower()])
                output_query += f" {operator} {word}"

            elif operator == "AND NOT":
                documents = documents.difference(inverted_index[word.lower()])
                output_query += f" {operator} {word}"

            elif operator == "OR NOT":
                documents = documents.union(set(path).difference(inverted_index[word.lower()]))
                output_query += f" {operator} {word}"


    print(f'Number of documents retrieved for query {i + 1}: {len(documents)}')
    print(f'Names of the documents retrieved for query {i + 1}: {", ".join(list(documents))}')
    print(f'Number of comparisons required for query {i + 1}: {len(query.split()) - query.count("NOT") - len(op_list)}\n')
