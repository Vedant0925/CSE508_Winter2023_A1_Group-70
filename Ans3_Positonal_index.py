
documents=[]
index={}


### Q.3 (ii) 1.

documents=[]
pos_index={}


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
    for q in range(0,len(doc_tok)): ## Iterate through each word
        instance = q
        word = doc_tok[q]
        if word not in pos_index:  ##if word not in Index, create a new instance
            pos_index[word] = {"Total count": 0, "documents list": {}}
        if docID not in pos_index[word]["documents list"]:
            pos_index[word]["documents list"][docID] = []
        pos_index[word]["Total count"] += 1
        pos_index[word]["documents list"][docID].append(instance)
print(pos_index)





