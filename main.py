import urllib3
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = 'https://www.tecnocasa.tn/vendre/immeubles/centre-est-ce/sousse.html/pag-' + str(8)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
estates = soup.find_all('div', class_='immobiliListaAnnuncioContenuto col-lg-7 col-md-7 col-sm-12 col-xs-12')
list_of_lists = []


for estate in estates:
        list_of_estate = []
        estate_local = estate.find('div', class_='immobiliListaAnnuncioSottotitolo').text.split()[-1].strip()
        list_of_estate.append(estate_local)
        estate_type = estate.find('div', class_='immobiliListaAnnuncioSottotitolo').text.split()[0].strip()
        list_of_estate.append(estate_type)
        estate_price = estate.find('div', class_='immobiliListaAnnuncioPrezzo').text.replace('DT', '').strip()
        list_of_estate.append(estate_price)
        estate_other = estate.find('div', class_='immobiliListaAnnuncioDettagli').text.split()[-2].strip()
        list_of_estate.append(estate_other)
        estate_other1 = estate.find('div', class_='immobiliListaAnnuncioDettagli').text.split()[0].strip()
        list_of_estate.append(estate_other1)
        list_of_lists.append(list_of_estate)
        print(estate_local + '/' + estate_type + '/' + estate_price + '/' + estate_other + '/' + estate_other1)

df = pd.DataFrame(list_of_lists, columns=['local', 'type', 'prix', 'surface', 'nb_piece'])
df.to_csv('SO8.csv', index=False, sep=';')






