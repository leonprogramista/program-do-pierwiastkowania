liczba = int (input ('podaj liczbe ktora chcesz potengowac: '))
ilosc_poteng = int (input ('podaj potenge liczby, ta liczba u gory: '))
wynik = liczba

if liczba == 0:
    print ('0')
elif liczba == 1:
    print( 'twój wynik to: ', liczba )
else:
    if ilosc_poteng == 0:
            print('twój wynik to: ', '1')
    elif ilosc_poteng == 1:
            print( 'twój wynik to: ', liczba )
    else:
        for i in range(ilosc_poteng - 1):
           wynik = wynik * liczba 
        print( 'twój wynik to: ', wynik)