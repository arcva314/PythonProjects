import requests
from bs4 import BeautifulSoup as bs

disease = input('Enter name of disease: ')
disease = disease.capitalize()
#searches for disease webpage by using the first letter of the disease
d = disease[0]

#webpage of all diseases beginning with the first letter is pulled up
result = requests.get('https://www.mayoclinic.org/diseases-conditions/index?letter='+d)
base = 'https://www.mayoclinic.org'
src = result.content
soup = bs(result.text, 'html.parser')
listt = soup.find_all('li')

#searches the exact webpage for the disease from the list elements
for item in listt:
    try:
        if disease in item.find('a').text:
            website = item.find('a').get('href')
            website = base + website
            print('Further Reading:', website)
            break
    except:
        continue
        
#once webpage is found, extract all list elements pertaining to Symptoms
result2 = requests.get(website)
src2 = result2.content
soup2 = bs(result2.text, 'html.parser')
heads = soup2.find_all('h2')
for head in heads:
    if 'Symptoms' in head.text:
        symptoms = head.find_next_sibling('ul')
        symptoms = symptoms.find_all('li')
        print('\nSYMPTOMS:')
        for symptom in symptoms:
            print('-\t', symptom.text)