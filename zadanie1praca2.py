wiek = int(input('podaj swoj wiek'))
if(wiek<0):
    print('blad')
else:
    if(wiek>18):
        print('jestes pelnoletni')
    else:
        print('nie masz ukonczonych 18 lat')
