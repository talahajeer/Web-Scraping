#  using jupyter is easy for exploring in each step import requests
URL='https://web.archive.org/web/20210115215722/https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
import requests
page=requests.get(URL)
print(page.content)


from bs4 import BeautifulSoup 