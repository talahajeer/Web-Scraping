import requests
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    result_list = list(result)
    length=len(result_list)
    return f'Number of citation {length}'



def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result1 = soup.find('div', class_="mw-parser-output")
    txt=[]
    paragraphs = result1.find_all('p')
    for p in paragraphs:
        p2 = p.find('span',string=lambda text: 'citation needed' in text)
        if p2 :
            txt.append(p.text.strip())

    for a in txt:
        print(a)
        print('-'*20)
    return txt
        

if __name__ == '__main__':
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
    # In collaboration with Raneem, Manar