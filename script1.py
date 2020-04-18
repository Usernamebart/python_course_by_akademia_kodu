#Zadanie1 - Napisz program Hello World w Pythonie
print('Hello Friend!')

#Zadanie2 - Napisz program wczytujący 2 liczby całkowite z konsoli i wypisujący iloczyn l liczb
x = int(input('Podaj pierwszą liczbę całkowitą: '))
y = int(input('Podaj drugą liczbę całkowitą: '))

print('Iloczyn podanych liczb to: ', x * y)

#Zadanie3 - Napisz program, który odczytuje 2 liczby całkowite i sumuje je
a = int(input('Podaj pierwszą liczbę całkowitą: '))
b = int(input('Podaj drugą liczbę całkowitą: '))

print('Suma powyższych liczb to: ', a + b)

#Zadanie4 - Napisz program, który wypisuje na ekran liczbę 1000
z = 1000
print('Wypisuję na ekran liczbę', z)

#Zadanie5 - Napisz program, który wypisuje na ekran 100*30000
num1 = 100
num2 = 30_000
print('Iloczyn num1 i num2 wynosi:', num1 * num2)

#Zadanie6 - Napisz program, który odczytuje wyraz i wypisuje 2 pierwsze litery
wyraz = input('Podaj wyraz: ')
print('Dwie pierwsze litery podanego wyrazu to:', wyraz[:2])

#alternatywnie
print('Dwie pierwsze litery podanego wyrazu to:', wyraz[0] + wyraz[1])

#####
name = 'Michał'
index = 0
index2 = -1
print(name[index])      #index = 0, print(name[0])
print(name[index2])     #index = -1, print(name[-1])
#####

#Zadanie7 - Napisz program odczytujący z konsoli imię i sprawdzający czy imię jest męskie czy żeńskie
imie = input('Podaj imie: ')
if imie[-1] != 'a' or imie == 'Barnaba':
    print(imie, 'to imię męskie')
else:
    print(imie, 'to imię żeńskie')

#Zadanie8 - Napisz program, który odczytuje liczbę i pokazuje na ekran ostatnią cyfrę danej liczby
liczba = int(input('Podaj liczbę: '))
if liczba < 10:
    print('Podałeś cyfrę zamiast liczby!')
else:
    print('Ostatnia cyfra to: ', liczba%10)
