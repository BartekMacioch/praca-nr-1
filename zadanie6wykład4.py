#zdn6
def remove_outer_characters(lista):
    string=""
    for i in range(1, len(lista)-1):
        string=string+lista[i]
    print(string)
remove_outer_characters("warszawa")