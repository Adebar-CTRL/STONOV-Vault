listn = [3, 0, 1, 8, 7, 2, 5, 4, 9, 6]
print(len(listn))
storage = []
#listn.sort()
for x in range(len(listn)):
    for i in range(0,len(listn)):
        first = listn[0]
        if len(listn) > 1:
            second = listn[1]
        else:
            storage.append(listn[0])
            listn.pop(0)
            break
        if first < second:
            storage.append(first)
            listn.pop(0)
        else:
            storage.append(second)
            listn.pop(1)
    print(storage)
    listn.extend(storage)
    storage.clear()
    print(listn)
