from bs4 import BeautifulSoup


print("Printing 5 sample before any changes \n")

for i in range (1,6):
    url = "CSE508_Winter2023_Dataset\cranfield000"+str(i)
    with open(url) as infile:
        soup = BeautifulSoup(infile) 
    print(soup.prettify())
    print("\n")

########### Printing 5 sample before



for i in range (1,1401):
    if (i <10):
        url = "CSE508_Winter2023_Dataset\cranfield000"+str(i)
    elif (i<100):
        url = "CSE508_Winter2023_Dataset\cranfield00"+str(i)
    elif (i<1000):
        url = "CSE508_Winter2023_Dataset\cranfield0"+str(i)
    elif (i<10000):
        url = "CSE508_Winter2023_Dataset\cranfield"+str(i)
    
    
    with open(url) as infile:
        soup = BeautifulSoup(infile) 
    
    el = soup.find("text") 

    el_text = el.string 
    if (i <10):
        url2 = "CSE508_Winter2023_Dataset\cranfield000"+str(i)
    elif (i<100):
        url2= "CSE508_Winter2023_Dataset\cranfield00"+str(i)
    elif (i<1000):
        url2 = "CSE508_Winter2023_Dataset\cranfield0"+str(i)
    elif (i<10000):
        url2 = "CSE508_Winter2023_Dataset\cranfield"+str(i)
    
    f = open(url2, "w")
    f.write((soup.title.string))
    f.close
    f = open(url2, "a")
    f.write(el_text)




print("Printing 5 samples after the changes \n")


for i in range (1,6):
    f = open("CSE508_Winter2023_Dataset\cranfield000"+str(i), "r")
    print(f.read())
    print("\n")

########### Printing 5 sample after



import nltk
nltk.download('punkt')


import nltk
nltk.download('punkt')
nltk.download('stopwords')
import itertools




from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords



for i in range (1,1401):
    tokens =[]
    new_words =[]
    filtered_tokens=[]
    final_words=[]

    
    if (i <10):
        url2 = "CSE508_Winter2023_Dataset\cranfield000"+str(i)
    elif (i<100):
        url2= "CSE508_Winter2023_Dataset\cranfield00"+str(i)
    elif (i<1000):
        url2 = "CSE508_Winter2023_Dataset\cranfield0"+str(i)
    elif (i<10000):
        url2 = "CSE508_Winter2023_Dataset\cranfield"+str(i)


    ### Tokenizing 
    f = open(url2, "r")
    text = f.read()

    lower_text = text.lower()
    text = lower_text
    if (i<6):
        print("case-"+str(i)+" text after lowercasing the text")
        print(text)
        print("\n")

    # tokens = word_tokenize(text)
    text = text.replace(' ', '@')
    text = text.replace('-', ' ')
    
    # ll = [[' ',word_tokenize(w)] for w in text.split()]
    # tokens = list(itertools.chain(*list(itertools.chain(*ll))))
    # tokens = text.split(' ')
    tokens = word_tokenize(text)
    tokens = list(map(lambda x: x.replace('@', ' '), tokens))
    
    if (i<6):
        print("case-"+str(i)+"  Tokens are")
        print(tokens)
        print("\n")



    ## Removing Stop Words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [w for w in tokens if not w.lower() in stop_words]
    if (i<6):
        print("case-"+str(i)+"  Tokens after removing stop Words")
        print(filtered_tokens) 
        print("\n")


    ### Remove Punctuations
    new_words=[word.lower() for word in filtered_tokens if (word.isalpha() or word==' ')]
    if (i<6):
        print("case-"+str(i)+"  Tokens after removing punctiations")
        print(new_words)
        print("\n")


    ### Remove Blank Spaces 
    final_words=[word.lower() for word in new_words if word.isalpha() ]
    final_text=""
    for j in range(0,len(final_words)):
        final_text = final_text + final_words[j]+" "
    
    
    if (i<6):
        print("case-"+str(i)+" Tokens after removing Blank Spaces")
        print(final_words)
        print("\n")

    f = open(url2, "w")
    f.write(final_text)
    f.close()   

