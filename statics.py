#statics.py
def getMode(numList) :
    
    numList_set = set(numList)
    numList_dict = dict()
    for n in numList_set :
        numList_dict[n] =  numList.count(n)
    # print(numList_dict)

    max_num = max(numList_dict.values())
    modes = []
    for k,v in numList_dict.items() :
        if v == max_num :
            print('최빈값', k,v)
            # mode = k #최빈값
            modes.append(k)
            # break
    return modes

def getAvg(numList) :
    return sum(numList)/len(numList)
    