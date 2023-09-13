import math;
import pandas as pd;

DOCUMENTS_PATH=['Files/d1.txt','Files/d2.txt','Files/d3.txt','Files/d4.txt','Files/d5.txt']

STOP_WORDS={
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
}

DOCUMENTS_DATA_FREQUENCY=[];

#  remove unwanted words like , . from statring and ending of the word
def removeChar(word,charToRemove):
    while len(word)!=0 and word[0]==charToRemove:
        word=word[1:];

    while len(word)!=0 and word[-1]==charToRemove:
        word=word[0:len(word)-1];

    return word;


def findFrequencyOfWordInDocument(filePath):
    file=open(filePath,'r');
    MAP={};
    for line in file:
        for word in line.split(" "):
            word=removeChar(word,'\n');
            word=removeChar(word,',');
            word=removeChar(word,'.');
            word=removeChar(word,':');
            word=removeChar(word,'(');
            word=removeChar(word,')');
            word=word.lower();

            if(len(word)==0):continue;
            if(word in STOP_WORDS):continue;

            if MAP.get(word)!=None:
                MAP[word]+=1
            else:
                MAP[word]=1;
    # print(MAP);
    return MAP

UNION_WORDS={};
for doc in range(0,len(DOCUMENTS_PATH)):
    freq=findFrequencyOfWordInDocument(DOCUMENTS_PATH[doc])
    for word in freq:
        if UNION_WORDS.get(word)!=None:
            UNION_WORDS[word][doc]+=freq[word];
        else:
            UNION_WORDS[word]=[0]*len(DOCUMENTS_PATH);
            UNION_WORDS[word][doc]+=freq[word];

df=pd.DataFrame(UNION_WORDS);
print(df,"\n");

COSINE_SIMILARITY=[];

for doc1 in range(0,len(DOCUMENTS_PATH)):
    for doc2 in range(0,len(DOCUMENTS_PATH)):
        if doc1>=doc2: continue;
        numerator=0;
        deno1=0;
        deno2=0;
        for word in UNION_WORDS:
            numerator+=UNION_WORDS[word][doc1]*UNION_WORDS[word][doc2];
            deno1+=UNION_WORDS[word][doc1]**2;
            deno2+=UNION_WORDS[word][doc2]**2;
        
        deno1=math.sqrt(deno1);
        deno2=math.sqrt(deno2);
        print('Doc '+str(doc1)+' Doc '+str(doc2),"  ",numerator/(deno1*deno2));
        # COSINE_SIMILARITY.append(['Doc '+doc1+ ' Doc '+doc2,numerator/(deno1*deno2)]);

# print(COSINE_SIMILARITY);