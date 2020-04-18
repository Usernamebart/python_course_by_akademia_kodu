#Zadanie9 - Napisz program wypisujący kalendarz z 2016 roku luty
import calendar
print(calendar.month(2016,2))

#alternatywnie można zaimportować calendar jako c / skrocenie nazwy, alias dla kalendarza
import calendar as c
print(c.month(2016,2))

#Zadanie10 - Napisz program wypisujący kalendarz, gdzie rok i miesiąc podany jest przez użytkownika
import calendar as cal
year = int(input('Podaj rok: '))
month = int(input('Podaj numer miesiąca: '))

print(cal.month(year,month))

#Zadanie11 - Napisz program, który odczytuje wyraz i sprawdza czy wprowadzony wyraz to Akademia
Akademia = True
wyraz = input('Podaj wyraz: ')
if wyraz == 'Akademia':
    print(Akademia)
else:
    print(not Akademia)

##### początek kodu prowadzącego

word = input('Podaj wyraz: ')
#Akademia, akademia
if word.lower() == 'akademia': #zabezpieczenie aby nie zależnie od wielkości liter słowo było traktowane jako poprawne
    print('Podałeś poprawny wyraz')
else:
    print('Podałeś niepoprawny wyraz')

##### koniec kodu prowadzącego

#Zadanie12 - Sprawdź czy liczba wprowadzona jest podzielna przez 3 lub 5
number = int(input('Podaj liczbę: '))
if number % 3 == 0 or number % 5 == 0:
    print(f'Liczba {number} jest podzielna przez 3 lub 5')
else:
    print(f'Liczba {number} nie jest podzielna przez 3 lub 5')

#Zadanie13 - Odczytaj wiek osoby i sprawdź czy osoba jest pełnoletnia czy niepełnoletnia
wiek = int(input("Podaj swój wiek: "))
if wiek >= 0 and wiek < 18:
    print('Jesteś niepełnoletni')
else:
    print('Jesteś pełnoletni')

#Zadanie14 - Napisz program wypisujący liczby od 1 do 10
for i in range(1,11):
    print(i)

#alternatywnie
for i in range(0,10):
    print(i+1)

#Zadanie15 - Napisz program wypisujący liczby do 20 do 1 (w tej kolejności)
for i in range(20,0,-1):
    print(i)

#Zadanie16 - Napisz program drukujący na ekranie 10 gwiazdek: **********
print('*' * 10)

for i in range(1,11):
    print('*', end='')

#Zadanie17 - Napisz program, który wypisuje liczby od 2 do 50
for i in range(2,51):
    print(i)
