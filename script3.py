# # Zadanie18 - Napisz program, który symuluje działanie słownika polsko-angielskiego. Użytkownik podaje słowo po
# #            Polsku i w odpowiedzi otrzymuje słowo po angielsku
# dictionary = {
#     'cześć' : 'hello',
#     'mama' : 'mother',
#     'tata' : 'father',
#     'pies' : 'dog'
# }
#
# pl_word = input('Podaj słowo po polsku: ')
# if pl_word in dictionary:
#     print(f'{pl_word} po angielsku to:', dictionary[pl_word])
# else:
#     print('Brak słowa w słowniku')

# Zadanie20 - Zainstaluj pakiet BeautifulSoup i odczytaj ze strony pracuj.pl ilość ofert pracy w Pythonie
#             web scraping: https://www.dataquest.io/blog/web-scraping-tutorial-python/
#             lista pakietów/bibliotek do zaimportowania w pythonie: pypi.org
import requests as r
from bs4 import BeautifulSoup

url = 'https://www.pracuj.pl/praca/python;kw?rd=0' # adres strony z ktorej bedziemy zaciagac dane
page = r.get(url) # łączymy sie ze stroną

soup = BeautifulSoup(page.content,'html.parser') # zupa przetwarza nam tekst

# print(page) # w odpowiedzi dostajemy kod http
# print(page.text) # w odpowiedzi dostajemy html
# print(soup.title) # w odpowiedzi dostajemy tytuł strony

# <span class="results-header__offer-count-text-number">256</span> => element z inspektora
# .find - znajduje element na stronie
element = soup.find('span', class_="results-header__offer-count-text-number")
print('Liczba ofert pracy w Pythonie to:', element.text)
