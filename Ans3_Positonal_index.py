### Q.3 (ii) 1.

documents=[]
pos_index=[{},{}]
zero = 0


for i in range (1,10):
    if (i <10):
        url2 = "CSE508_Winter2023_Dataset\cranfield000"+str(i)
    elif (i<100):
        url2= "CSE508_Winter2023_Dataset\cranfield00"+str(i)
    elif (i<1000):
        url2 = "CSE508_Winter2023_Dataset\cranfield0"+str(i)
    elif (i<10000):
        url2 = "CSE508_Winter2023_Dataset\cranfield"+str(i)

    f = open(url2, "r")
    text =  f.read()
    f.close

    tokens = text.split()
    documents.append(tokens)


# Iterate through each document
for p in range(0,len(documents)):
    docID = p
    doc_tok = documents[p]
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

print(pos_index)

import pickle



with open('PosInd\inverted_index.pkl', 'wb') as f:
    pickle.dump(pos_index, f)

# Load the inverted index from the file
with open('PosInd\inverted_index.pkl', 'rb') as f:
    loaded_index = pickle.load(f)

# Print the loaded index to verify it matches the original index
# print(loaded_index)
