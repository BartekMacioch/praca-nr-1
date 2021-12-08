#zdn4
kapital = int(input('Podaj kapital poczatkowy: '))
wplywy = int(input('Podaj miesieczne wplywy: '))
okres = int(input('Podaj okres inwestowania: '))
inwestycja = int(input('Podaj pozadana koncowa wartosc inwestycji:'))
if (kapital >= 0 and wplywy >= 0 and okres >= 0 and inwestycja >= kapital):
    zysk = (kapital + wplywy * okres) * 1.02
    if (inwestycja > zysk):
        print('pozadana koncowa wartosc inwestycji jest wieksza niz koncowy kapital')
    else:
        print('pozadana koncowa wartosc inwestycji jest mniejsza niz koncowy kapital')
else:
    print('Powinienes poprawic dane wejsciowe. Oczekiwana wrtosc koncowa powinna byc wieksza niz kapital poczatkowy ')
