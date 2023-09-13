import pandas as pd

TRANSACTIONS = {}
UNIQUE_ITEMS = {}

MIN_SUPPORT_COUNT = 2
CONFIDENCE = 50


def removeChar(word, charToRemove):
    while len(word) != 0 and word[0] == charToRemove:
        word = word[1:]

    while len(word) != 0 and word[-1] == charToRemove:
        word = word[0:len(word)-1]

    return word


def findFrequenctItems(filePath):
    file = open(filePath, 'r')
    for line in file:
        transac = line.split(" ")
        TRANSACTIONS[transac[0]] = []
        for item in transac[2].split(","):
            item = removeChar(item, '\n')
            TRANSACTIONS[transac[0]].append(item)
            if UNIQUE_ITEMS.get(item) == None:
                UNIQUE_ITEMS[item] = 1


findFrequenctItems("Transactions.txt")
# print(TRANSACTIONS);
# print(UNIQUE_ITEMS);
UNIQUE_ITEMS_ARR = list(UNIQUE_ITEMS.keys())
# print(UNIQUE_ITEMS_ARR);


CANDIDATE_SETS = {}


def findSupportCount(arr):
    count = 0
    for transac in TRANSACTIONS:
        flag = True
        for i in range(0, len(arr)):
            if (arr[i] not in TRANSACTIONS[transac]):
                flag = False
                break
        if (flag):
            count += 1
    return count


def findCandidateSet(indx, k, arr, c_index):
    if (k == 0):
        if (CANDIDATE_SETS.get(c_index) == None):
            CANDIDATE_SETS[c_index] = {}
        str = " "
        CANDIDATE_SETS[c_index][str.join(arr)] = findSupportCount(arr)
        return
    if (indx >= len(UNIQUE_ITEMS_ARR)):
        return

    findCandidateSet(indx+1, k, arr, c_index)
    arr.append(UNIQUE_ITEMS_ARR[indx])
    findCandidateSet(indx+1, k-1, arr, c_index)
    arr.pop()


for i in range(1, len(UNIQUE_ITEMS_ARR)+1):
    findCandidateSet(0, i, [], i)

VALID_CANDIDATE_SETS = {}

print("\n\n------------------------DICTIONARY FORMAT------------------------\n")
for i in CANDIDATE_SETS:
    for j in CANDIDATE_SETS[i]:
        if (CANDIDATE_SETS[i][j] >= MIN_SUPPORT_COUNT):
            if (VALID_CANDIDATE_SETS.get(i) == None):
                VALID_CANDIDATE_SETS[i] = {}
            VALID_CANDIDATE_SETS[i][j] = CANDIDATE_SETS[i][j]

    if (VALID_CANDIDATE_SETS.get(i) != None):
        print("Candidate Set", i, '\n', VALID_CANDIDATE_SETS[i])


print("\n\n------------------------TABULAR FORMAT------------------------\n")
df = pd.DataFrame(VALID_CANDIDATE_SETS)
print(df)


def checkDuplicateItems(set1, set2):
    items = set(set1.split(" "))

    for m in set2.split(" "):
        if (m in items):
            return True

    return False


def combineSets(set1, set2):
    list1 = list(set1.split(" "))+list(set2.split(" "))
    list1.sort(reverse=False)
    new_str = " "
    new_str = new_str.join(list1)
    return new_str


print("\n\n------------------------ASSOCIATION RULES AND CONFIDENCE------------------------\n")
for i in VALID_CANDIDATE_SETS:
    for j in VALID_CANDIDATE_SETS:
        for k in VALID_CANDIDATE_SETS[i]:
            for l in VALID_CANDIDATE_SETS[j]:
                if (k == l and i == j):
                    continue

                # Checking for the duplicate items in both the sets
                if checkDuplicateItems(k, l):
                    continue

                new_set = combineSets(k, l)
                size = (len(new_set)+1)/2
                if VALID_CANDIDATE_SETS.get(size) == None or VALID_CANDIDATE_SETS[size].get(new_set) == None:
                    continue

                #                                            lhs         rhs
                # Calculating confidence A B => C  =  (support(A B C)/support(A B))*100

                lhs_support = VALID_CANDIDATE_SETS[size][new_set]
                rhs_support = VALID_CANDIDATE_SETS[i][k]
                confidence = (lhs_support/rhs_support)*100

                if (confidence < CONFIDENCE):
                    continue
                
                print(k, "=>", l, " = ", confidence, "%")


"""
T1  A,B,C
T2  A,D,E
T3  B,E
T4  D,C
T5  A,E
T6  B,C,D
"""
