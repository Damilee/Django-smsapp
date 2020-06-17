import requests
from bs4 import BeautifulSoup

URL = 'https://ncdc.gov.ng/news/press'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='example')
news_elems = results.find_all('div', class_='col-sm-10')
# print(results.prettify())
# print(news_elems)
for news_elem in news_elems:
    title_elem = news_elem.find('h3')
    date_elem = news_elem.find('h4')
    # sub_elem = news_elem.find(id='text')
    link_elem = news_elem.find('a', class_='white-text')
    if None in (title_elem, date_elem, link_elem):
        continue
    title = title_elem.text.strip()
    date = date_elem.text.strip()
    link = link_elem.get('href')
    space = ''
    scrape = print(title, date, link, space)
    context = {'scrape': scrape}
    print (scrape)
    