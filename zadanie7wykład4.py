#zdn7
def count_chars(x):
    slownik = {} #deklaracja słownika (tworzę pusty słownik)
    x = x.lower()
    for i in range(0,len(x)):
        slownik[x[i]] = 0
    for i in range(0,len(x)):
        slownik[x[i]] = slownik[x[i]] + 1
    print(slownik)
count_chars("Przykładp")