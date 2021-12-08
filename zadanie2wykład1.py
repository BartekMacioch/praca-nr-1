#zdn 2
name = input('jak masz na imie? ')
age = input('ile masz lat? ')
if(type(age)==int):
    print('twoje imie to'+ name + 'i masz' + age + 'lat')
else:
    print('age nie jest typu int, zmieniam na typ int')
    age = int(age)
    print(type(age))
    #print('twoje imie to'+ name + 'i masz' + age + 'lat') tylko dla parametow typu string
    print('Twoje imię to %s i masz %i lat' % (name, age))
