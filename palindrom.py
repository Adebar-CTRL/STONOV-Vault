def check(text):
    store = ''
    for i in text:
        store =  i + store
    if store == text:
        print('Palindom')
    else:
        print('kein Palindom')
check(input("enter text"))