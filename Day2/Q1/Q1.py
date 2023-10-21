import math 

ATTRIBUTES={
    'war':0,
    'fly':1,
    'ver':2,
    'end':3,
    'gro':4,
    'hai':5,
}

NO_OF_ATTRIBUTE=6

# Given Data Set
DATA_SET={
    "ant":[1,1,2,1,3,1],
    "bee":[1,2,1,1,2,2],
    "cat":[2,1,2,1,1,2],
    "cpl":[1,1,1,1,1,2],
    "chi":[2,1,2,2,2,2],
    "cow":[2,1,2,1,2,2],
    "duc":[2,2,2,1,2,1],
    "eag":[2,2,2,2,1,1],
    "ele":[2,1,2,2,2,1],
    "fly":[1,2,1,1,1,1],
    "fro":[1,1,2,2,"NA",1],
    "her":[1,1,2,1,2,1],
    "lio":[2,1,2,"NA",2,2],
    "liz":[1,1,2,1,1,1],
    "lob":[1,1,1,1,"NA",1],
    "man":[2,1,2,2,2,2],
    "rab":[2,1,2,1,2,2],
    "sal":[1,1,2,1,"NA",1],
    "spi":[1,1,1,"NA",1,2],
    "wha":[2,1,2,2,2,1]
}

DATA_SET_INDEXING={}

index=0;
for data in DATA_SET:
    DATA_SET_INDEXING[data]=index
    index+=1;

# print("\n#-------DATA_INDEXING------#")
# for data in DATA_SET_INDEXING:
#     print(data,DATA_SET_INDEXING[data])

ONE_FREQ=[0]*NO_OF_ATTRIBUTE
TWO_FREQ=[0]*NO_OF_ATTRIBUTE

# Finding the freq of one's and two's
for data in DATA_SET.values():
    for i in range(0,NO_OF_ATTRIBUTE):
        if data[i]==1:
            ONE_FREQ[i]+=1
        elif data[i]==2:
            TWO_FREQ[i]+=1

print("\n#-------FREQUENCY------#")
print(ONE_FREQ)
print(TWO_FREQ)

PROCESSED_DATA={};

# Filling the missing values
for data in DATA_SET:
    PROCESSED_DATA[data]=[0]*NO_OF_ATTRIBUTE
    for i in range(0,NO_OF_ATTRIBUTE):
        if DATA_SET[data][i]=="NA":
            if ONE_FREQ[i]>TWO_FREQ[i]:
                PROCESSED_DATA[data][i]=1
            else :
                PROCESSED_DATA[data][i]=2
        else :
            PROCESSED_DATA[data][i]=DATA_SET[data][i];

print("\n#-------PROCESSED DATA------#")
for data in PROCESSED_DATA:
    print(data,PROCESSED_DATA[data])

CALC_DATA=[]

print("\n#-----CALCULATED_PART------#")
for data1 in PROCESSED_DATA:
    for data2 in PROCESSED_DATA:
        if DATA_SET_INDEXING[data1]<DATA_SET_INDEXING[data2]:
            euclid_distance=0;
            for i in range(0,NO_OF_ATTRIBUTE):
                euclid_distance+=(PROCESSED_DATA[data1][i]-PROCESSED_DATA[data2][i])**2;
            euclid_distance=math.sqrt(euclid_distance);
            CALC_DATA.append((euclid_distance,data1+' '+data2));





CALC_DATA.sort()

for i in range(len(CALC_DATA)):
    print(CALC_DATA[i]);