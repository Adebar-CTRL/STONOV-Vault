def check(number):
    store = 0
    for i in number:
        store = store + int(i)
    print(store)
check(input("enter number"))
