import os
import pickle
from collections import defaultdict

def build_inverted_index(folder_path):
    inverted_index = defaultdict(list)
    for root, _, files in os.walk(folder_path):
        for file in files:
            with open(os.path.join(root, file), 'r') as f:
                doc_id = file
                content = f.read().strip().split()
                for word in content:
                    inverted_index[word].append(doc_id)
    return dict(sorted(inverted_index.items()))

def save_inverted_index(inverted_index, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(inverted_index, f)

def load_inverted_index(file_path):
    with open(file_path, 'rb') as f:
        inverted_index = pickle.load(f)
    return inverted_index

folder_path = '/Users/vedant/Downloads/Work'
inverted_index = build_inverted_index(folder_path)

for word, doc_ids in inverted_index.items():
    print(word,":",doc_ids)

file_path = os.path.expanduser('~/inverted_index.pickle')
save_inverted_index(inverted_index, file_path)

inverted_index = load_inverted_index(file_path)

for word, doc_ids in inverted_index.items():
    print(word,":",doc_ids)
