import urllib.request
from bs4 import BeautifulSoup
import time

wiki = 'https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_FBS_football_programs'


with urllib.request.urlopen(wiki) as url:
    page = url.read()

soup = BeautifulSoup(page, 'html.parser')

team_rows = soup.find_all('tr')

for x in team_rows:
    try:
        print(x.find('td').text.strip())
    except:
        continue
