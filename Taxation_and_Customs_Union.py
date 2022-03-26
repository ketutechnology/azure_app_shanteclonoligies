import requests
from bs4 import BeautifulSoup
from csv import writer


url = "https://ec.europa.eu/taxation_customs/dds2/ebti/ebti_consultation.jsp?Lang=en&Lang=en&refcountry=IE&reference=&valstartdate1=01-01-2022&valstartdate=01%2F01%2F2022&valstartdateto1=28-02-2022&valstartdateto=28%2F02%2F2022&valenddate1=&valenddate=&valenddateto1=&valenddateto=&suppldate1=&suppldate=&nomenc=&nomencto=&keywordsearch1=&keywordsearch=&specialkeyword=&keywordmatchrule=OR&excludekeywordsearch1=&excludekeywordsearch=&excludespecialkeyword=&descript=&orderby=0&Expand=true&offset=1&viewVal=&isVisitedRef=true&allRecords=0&showProgressBar=true"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content,'html.parser')
#print(soup)
results = soup.find_all('div',class_='_13oc-S')
#print(results)

# with open('products.csv','w',newline='',encoding='utf8') as f:
#     thewriter = writer(f)
#     header =['Title','Rating','description','price']
#     thewriter.writerow(header)
    
#     for result in results:
#         title =result.find('div',class_='_4rR01T').text.replace('\n','')
#         rating =result.find('span',class_='_1lRcqv').text.replace('\n','')
#         description =result.find('div',class_='fMghEO').text.replace('\n','')
#         price =result.find('div',class_='_25b18c').text.replace('\n','')
#         prdinfo = [title,rating,description,price]
#         thewriter.writerow(prdinfo)


#     #print(f"product_name : {title.text}")
#     #print(f"product_rating : {rating.text}")
#     #print(f"product_description : {description.text}")
#     #print(f"product_price : {price.text}",'\n')
