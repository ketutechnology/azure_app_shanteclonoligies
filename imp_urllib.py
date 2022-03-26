import requests
from bs4 import BeautifulSoup
from csv import writer


url = "https://ec.europa.eu/taxation_customs/dds2/ebti/ebti_details.jsp?Lang=en&selectedReference=&reference=ATBTI2020000507-DEC&refcountry=AT&valstartdate=01/03/2020&valstartdateto=14/03/2022&valenddate=&valenddateto=&suppldate=&nomenc=&nomencto=&keywordsearch=&excludekeywordsearch=&descript=&orderby=0&totalRecords=1055&linkVal=&viewVal=&keywordmatchrule=OR&specialkeyword=&excludespecialkeyword="
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.content,'html.parser')
#print(soup)
results = soup.find_all('tbody',class_='ecl-table__body')
print(results)
	
#for result in results:
title =result.find('td',class_='ecl-table__cell').text.replace('\n','')
rating =result.find('td',class_='ecl-table__cell').text.replace('\n','')
# 	description =result.find('div',class_='fMghEO').text.replace('\n','')
# 	price =result.find('div',class_='_25b18c').text.replace('\n','')
	

print(f"product_name : {title.text}")
print(f"product_rating : {rating.text}")