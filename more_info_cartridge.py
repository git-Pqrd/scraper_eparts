from bs4 import BeautifulSoup
import requests
import csv
import re
import os  



urls_to_visit = [] # encore une fois je vais la joué safe avec les urls 
#j'inclus aussi img car + tricky de les shopper sur page produit
with open( './cs_combined.csv' , 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        i = [ row[1][6:], row[3]]
        urls_to_visit.append(i)
        
urls_visited = [] # encore une fois je vais la joué safe avec les urls
if os.path.exists('./full_cartridge.csv'):
    with open( './full_cartridge.csv' , 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            i = row[0]
            urls_visited.append(i)

count = 0
with open( './full_cartridge.csv', 'a' ) as csvfile : 
    writer = csv.writer(csvfile, delimiter=",", quotechar='"')
    for i in urls_to_visit :
        count += 1
        print(str(count) + " out of "+ str(len(urls_to_visit)))
        if i[0] in urls_visited  : continue
        #getting the content
        result = requests.get(i[0])
        content = result.content
        status = result.status_code
        soup = BeautifulSoup(content, 'html.parser')

        #getting multiple li to class the one conso and the one spare
        name = "product_name : " + soup.find_all('h1', class_='page-title')[0].text
        img = i[1]
        try : nmbr_page = "nmbr_page : " + soup.find_all('span', class_='yield')[0].text
        except : nmbr_page = "unknown" 

        try : color = "color : " + soup.find_all('span', class_='sprite')[0]['class'][1]
        except : color = "incolor" 
        desc = "desc : " + soup.find_all('div', class_='inner-content article')[0].find_all('p')[0].get_text(separator=". ")

        compat_printer = []
        for a in soup.find_all('div', class_="compatible_printers")[0].find_all('a', class_='p_link'): 
            compat_printer.append(a.text)

        product_spec =  []
        for tr in soup.find_all('table', class_='additional-attributes')[0].find_all('tr'):
            carac_key = tr.find_all('th')[0].get_text(separator=". ")
            carac_val = tr.find_all('td')[0].get_text(separator=". ")
            product_spec.append(carac_key + " : " + carac_val )

        urls_visited.append(i)
        row_done = [i[0], name ,  img , nmbr_page, color, desc] + compat_printer + product_spec 
        writer.writerow(row_done)
        print(row_done)

