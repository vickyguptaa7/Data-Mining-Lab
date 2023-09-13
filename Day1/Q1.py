# Given a text file, write a python code to display the frequency of occurrence of each word in the file.

MAP={};

file=open("text.txt","r");

#  remove unwanted words like , . from statring and ending of the word
def removeChar(word,charToRemove):
    while len(word)!=0 and word[0]==charToRemove:
        word=word[1:];

    while len(word)!=0 and word[-1]==charToRemove:
        word=word[0:len(word)-1];

    return word;



# read file and store word count in map
for line in file:
    for word in line.split(" "):
        word=removeChar(word,'\n');
        word=removeChar(word,',');
        word=removeChar(word,'.');
        if(len(word)==0):continue;
        if MAP.get(word)!=None:
            MAP[word]+=1
        else:
            MAP[word]=1;


WORD_LIST=[];

# convert map to list
for x in MAP:
    WORD_LIST.append((MAP[x],x));

# sort list in reverse
WORD_LIST.sort(reverse=True);

# print list
for x in WORD_LIST:
    print(x[0],x[1]);