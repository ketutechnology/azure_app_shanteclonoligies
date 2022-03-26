import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


country_name_id = {"Austria":"AT","Belgium":"BE","Bulgaria":"BG","Croatia":"HR","Cyprus":"CY","Czech rep":"CZ","Denmark":"DK","Estonia":"EE","Finland":"FI","France":"FR","Germany":"DE","Greece":"GR"}
startDay ="01"
startMonth = "03"
startYear = "2022"
endDay ="10"
endMonth = "03"
endYear = "2022"

countryName = input(str("enter country name : "))
countryCode = country_name_id.get(countryName)
print(countryCode)
startDay = input(str("Enter Day : "))
startMonth = input(str("Enter Month : "))
startYear = input(str("Enter Year : "))
endDay = input(str("Enter End day : "))
endMonth = input(str("Enter End month : "))
endYear = input(str("Enter End year : "))
searchUrl = "https://ec.europa.eu/taxation_customs/dds2/ebti/ebti_consultation.jsp?Lang=en&Lang=en&refcountry="+countryCode+"&reference=&valstartdate1=01-01-2020&valstartdate="+startDay+"%2F"+startMonth+"%2F"+startYear+"&valstartdateto1=14-03-2022&valstartdateto="+endDay+"%2F"+endMonth+"%2F"+endYear+"&valenddate1=&valenddate=&valenddateto1=&valenddateto=&suppldate1=&suppldate=&nomenc=&nomencto=&keywordsearch1=&keywordsearch=&specialkeyword=&keywordmatchrule=OR&excludekeywordsearch1=&excludekeywordsearch=&excludespecialkeyword=&descript=&orderby=0&Expand=true&offset=1&viewVal=&isVisitedRef=false&allRecords=1&showProgressBar=false"

# Using urlopen() function with url in it  
#webUrl = urllib.request.urlopen(searchUrl)
page = requests.get(searchUrl)
#print(page)
soup = BeautifulSoup(page.content,'html.parser')
print(soup)
results = soup.find('tbody',class_='ecl-table__body')
print(results)

