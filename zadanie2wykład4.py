#zdn2
def find_min(lista):
    x = lista[0]
    for i in range(0, len(lista)):
        if(x > lista[i]):
            x = lista[i]
    print(x)
find_min([12, 3, 29, 4, -1, 90, -10, -90])