wiek = int(input('podaj swoj wiek'))
if (wiek>21):
    print('Mozesz prowadzic samochod oraz glosowac w wyborach')
if (wiek>17 and wiek<21):
    print('Mozesz prowadzic samochod')
else:
    print('Nie mozesz glosowac ani prowadzic samochodu')
