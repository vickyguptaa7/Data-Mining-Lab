import pandas as pd
import math

STOP_WORDS={
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"
}

QUESTIONS_PATH=['Files/q1.txt','Files/q2.txt','Files/q3.txt','Files/q4.txt','Files/q5.txt']
ANSWERS_PATH=['Files/a1.txt','Files/a2.txt','Files/a3.txt','Files/a4.txt','Files/a5.txt']

ANSWERS_LIST=[];

#  remove unwanted words like , . from statring and ending of the word
def removeChar(word,charToRemove):
    while len(word)!=0 and word[0]==charToRemove:
        word=word[1:];

    while len(word)!=0 and word[-1]==charToRemove:
        word=word[0:len(word)-1];

    return word;

QUESTIONS_WORD_FREQ=[];

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
            word=removeChar(word,'?');
            word=word.lower();

            if(len(word)==0):continue;
            if(word in STOP_WORDS):continue;

            if MAP.get(word)!=None:
                MAP[word]+=1
            else:
                MAP[word]=1;
    # print(MAP);
    return MAP

for i in range(0,len(QUESTIONS_PATH)):
    QUESTIONS_WORD_FREQ.append(findFrequencyOfWordInDocument(QUESTIONS_PATH[i]))

for i in range(0,len(ANSWERS_PATH)):
    file=open(ANSWERS_PATH[i],'r');
    ANSWERS_LIST.append(file.read());

print("\n#-------QUESTIONS_WORD_FREQ------#\n")
for i in range(0,len(QUESTIONS_WORD_FREQ)):
    print('Questions',i,QUESTIONS_WORD_FREQ[i],"\n")

# new_ques=input("Enter a question to find the answer : ");

new_ques_freq=findFrequencyOfWordInDocument('Files/new_ques.txt');

def findCosineSimilarity(word_freq):
    numerator=0;
    deno1=0;
    deno2=0;
    for word in word_freq:
        numerator+=word_freq[word][0]*word_freq[word][1];
        deno1+=word_freq[word][0]**2;
        deno2+=word_freq[word][1]**2;
    deno=math.sqrt(deno1*deno2);

    return numerator/deno;


# print(new_ques_freq)
suitable_ans_indx=0;
max_cosine_similarity=0;
for ques in range(0,len(QUESTIONS_WORD_FREQ)):
    union={};
    print("Considering Question :",ques,'\n')
    for word in new_ques_freq:
        union[word]=[new_ques_freq[word],0];

    for word in QUESTIONS_WORD_FREQ[ques]:
        if union.get(word)==None:
            union[word]=[0,QUESTIONS_WORD_FREQ[ques][word]];
        else:
            union[word][1]=QUESTIONS_WORD_FREQ[ques][word];
    df=pd.DataFrame(union)
    print(df)
    cosine_similarity=findCosineSimilarity(union);
    print("Cosine Similarity :",cosine_similarity,"\n\n")
    if max_cosine_similarity<cosine_similarity :
        max_cosine_similarity=cosine_similarity
        suitable_ans_indx=ques

print("\n#-------ANSWER------#")
print(ANSWERS_LIST[suitable_ans_indx]);
print(max_cosine_similarity);


