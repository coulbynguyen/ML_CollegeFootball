import urllib.request
from bs4 import BeautifulSoup
import time
base_url = 'https://www.espn.com'

espn = 'https://www.espn.com/college-football/teams'

with urllib.request.urlopen(espn) as url:
    page = url.read()

soup = BeautifulSoup(page, 'html.parser')

team_box = soup.find_all('section', attrs={'class': 'TeamLinks flex items-center'})

img_links = []
print('[')
for x in team_box:
    img_links.append(x.find('a'))

for z,x in enumerate(img_links):
    new_url = base_url + x['href']
    with urllib.request.urlopen(new_url) as url:
        team_page = url.read()

    team_soup = BeautifulSoup(team_page, 'html.parser')

    team_name = team_soup.find('span', attrs={'class': 'ClubhouseHeader__Location'})

    div_soup = team_soup('div', attrs={'class': 'Image__Wrapper'})
    for x in div_soup:
        image_section = x.find('source')
        print('{')
        print("'key':'" + str(team_name.text.strip()) + "',")
        print("'text':'" + str(team_name.text.strip()) + "',")
        print("'imgsrc':'" + str(image_section['data-srcset']) + "',")
        print("'value':'" + str(z) + "'")
        print('},')
