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

# print(pos_index)

import pickle



with open('PosInd\inverted_index.pkl', 'wb') as f:
    pickle.dump(pos_index, f)

# Load the inverted index from the file
with open('PosInd\inverted_index.pkl', 'rb') as f:
    loaded_index = pickle.load(f)

# Print the loaded index to verify it matches the original index
# print(loaded_index)

def find_query(query):
    # index=load_index("indexfile")
    tok = query.split()
    ret = [] ##doclist
    count =0
    docIds=[]
    for b in tok:
        if b in loaded_index:
            ret.append(loaded_index[b]['documents list'])
            # count = count+ len(loaded_index[b]['documents list'] )
            # docId.append(list(loaded_index[b]['documents list'].keys()))
            docIds = docIds + list(loaded_index[b]['documents list'].keys())
            uniqueDocIds = [ x for i, x in enumerate(docIds) if x not in docIds[:i]]
            count = len(uniqueDocIds)
    return count ,uniqueDocIds

print("Enter Number of Queries Followed By Queries")
a = int(input())
queries=[]
for i in range(a):
    queries.append(str(input()))

i = 0
for j in queries:
    i=i+1
    count , list=find_query(j)
    # print(result)
    print("Number of Documents Retrived for Query "+str(i)+": "+str(count))
    print("Names of Documents Retrived for Query ")
    for k in list:
        if (k <10):
            url2 = "cranfield000"+str(k)
        elif (k<100):
            url2= "cranfield00"+str(k)
        elif (k<1000):
            url2 = "cranfield0"+str(k)
        elif (k<10000):
            url2 = "cranfield"+str(k)
        print(url2+" ")
        


