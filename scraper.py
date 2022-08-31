from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

r = requests.get('https://stackoverflow.com/jobs?d=50&l=Germany&q=developer&r=true&u=Km')
soup = BeautifulSoup(r.text, 'html.parser')
pagination_item = soup.find_all('a', {'class':'s-pagination--item is-selected'})
page_count = pagination_item[0]['title'].split(' ')[3]
page_count = int(page_count)
jobs_list = []
company_list = []
url_list = []

print(page_count)

for i in range(page_count):
    r_temp = requests.get(f'https://stackoverflow.com/jobs?d=50&l=Germany&q=developer&r=true&u=Km&pg={i+1}')
    soup = BeautifulSoup(r.text, 'html.parser')
    jobs = soup.find_all('h2', class_ = 'mb4 fc-black-800 fs-body3')
    companies = soup.find_all('h3', class_ = 'fc-black-700 fs-body1 mb4')
    source_urls = soup.find_all('a', class_ = 's-link stretched-link')
    jobs_list += [jobs[i].getText().strip() for i in range(len(jobs))]
    company_list += [companies[i].getText().split('                \r\n                •\r\n                \r\n')[0].strip().replace('\n', '').replace('\r','') for i in range(len(companies))]
    url_list += [('https://stackoverflow.com' + source_urls[i]['href']) for i in range(len(source_urls))]
    print('Cycle complete')
    time.sleep(10)

df = pd.DataFrame(data = {'Company': company_list, 'Position': jobs_list, 'Sources': url_list})
df.to_csv('final_data.csv')

print(r)
print(*url_list, sep ='\n')
print(df)