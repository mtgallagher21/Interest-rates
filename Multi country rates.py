import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd

# Hong Kong
# Making a GET request
r = requests.get('https://www.citibank.com.hk/english/personal-banking/interest-and-foreign-exchange-rates/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
rates = []
country1 = "HK"

hk_rates = soup.find('span', class_='hdMidTxt')
rates.append(country1)
rates.append(hk_rates.text)

# New York
# Making a GET request
r = requests.get('https://fred.stlouisfed.org/series/EFFR')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country2 = "NY"

ny_rates = soup.find('span', class_='series-meta-observation-value')
rates.append(country2)
rates.append(ny_rates.text)


# ECB - Short Term Rate
# Making a GET request
r = requests.get('https://www.ecb.europa.eu/stats/financial_markets_and_interest_rates/euro_short-term_rate/html/index.en.html')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country4 = "ECB short-term rate"

euro_rates = soup.find('div', class_='table')
rows = euro_rates.find_all('td')
for j in rows[0:1]:
	rates.append(country4)
	rates.append(j.text)
	
# Australia
# Making a GET request
r = requests.get('https://www.rba.gov.au/statistics/cash-rate/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country5 = "Australia"

australia_rates = soup.find('table', class_='table-linear table-numeric')
rows = australia_rates.find_all('td')

for k in rows[1:2]:
	rates.append(country5)
	rates.append(k.text)

# Denmark
# Making a GET request
r = requests.get('https://www.nationalbanken.dk/en/what-we-do/stable-prices-monetary-policy-and-the-danish-economy/destr')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country6 = "Denmark"

denmark_rates = soup.find('div', class_='table')
rows = denmark_rates.find_all('td')

for l in rows[1:2]:
	rates.append(country6)
	rates.append(l.text)

# Norway
# Making a GET request
r = requests.get('https://www.norges-bank.no/en/topics/Statistics/nowa-data/Nowa-daily/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country7 = "Norway"

norway_rates = soup.find('div', class_='row mid-content-content-area')
rows = norway_rates.find_all('td')

for m in rows[1]:
	rates.append(country7)
	rates.append(m.text)

# Sweden
# Making a GET request
r = requests.get('https://www.riksbank.se/en-gb/statistics/swestr/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country8 = "Sweden"

sweden_rates = soup.find('div', class_='data-block__value')
content = sweden_rates.find_all('span')
rates.append(country8)
rates.append(sweden_rates.text)

# France
# Making a GET request
r = requests.get('https://www.global-rates.com/fr/taux-de-interets/saron/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country10 = "France"

france_rates = soup.find('table', class_='table')
rows = france_rates.find_all('td')

for p in rows[1:2]:
	rates.append(country10)
	rates.append(p.text)

# Singapore
# Making a GET request
r = requests.get('https://housingloansg.com/hl/charts/sibor-sor-daily-chart')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country11 = "Singapore"

singapore_rates = soup.find('table', class_='zebra')
rows = singapore_rates.find_all('td')

for q in rows[2:3]:
	rates.append(country11)
	rates.append(q.text)

# ECB - Deposit Facility
# Making a GET request
r = requests.get('https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country12 = "ECB - Deposit Facility"

ecb_rates = soup.find('div', class_='table')
rows = ecb_rates.find_all('td')

for r in rows[2:3]:
	rates.append(country12)
	rates.append(r.text)

# Mexico - Interest Rate
# Making a GET request
r = requests.get('https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?sector=18&accion=consultarCuadroAnalitico&idCuadro=CA51&locale=en')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country13 = "Mexico - Interest Rate"

mexico2_rates = soup.find('div', class_='table-responsive')
rows = mexico2_rates.find_all('td')

for s in rows[86]:
	rates.append(country13)
	rates.append(s.text)

# Mexico - Gov Securities
# Making a GET request
r = requests.get('https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CF107&sector=22&locale=en')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country14 = "Mexico - Gov Securities"

mexico1_rates = soup.find_all('td', class_='cd_tabla_renglon tdObservacion paddingr')
rows = mexico1_rates

for t in rows[8:9]:
	rates.append(country14)
	rates.append(t.text)	
			
# Canada
# Making a GET request
r = requests.get('https://www.citigroup.com/canada/en/customer-information/rates.html#:~:text=Citi%27s%20Canadian%20Dollar%20PRIME%20Lending%20Rate%20is%207.10%25%20per%20annum.')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the relevant information from the HTML code
country15 = "Canada"

canada_rates = soup.find('div', class_='inner-row wide')
rows = canada_rates.find_all('p')

for u in rows[0:1]:
	rates.append(country15)
	rates.append(u.text)
	
# Store the information in a pandas dataframe
df = pd.DataFrame({'Interest Rates':rates})

# Export the data to a CSV file
df.to_csv('Interest-Rates.csv', index=False)

