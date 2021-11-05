def runloop(amount):
    store = 0
    for i in range(1,amount + 1, 2):
        store = store + i
        print(i)
    print(store)
runloop(int(input("enter number"))) 