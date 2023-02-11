with open('kino.txt') as f:
    bigList = []
    for i in f.read().split('\n'):
        bigList.append(i.rsplit(',', 2))

# bigList.sort(key= lambda bigList: bigList[2])
# for i in bigList:
#     print(i)
print(bigList[2])