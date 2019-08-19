import urllib.request
from bs4 import BeautifulSoup
import time

base_url = 'https://www.espn.com'
# 2018
# espn = 'https://www.espn.com/college-football/schedule/_/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/2/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/3/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/4/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/5/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/6/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/7/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/8/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/9/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/10/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/11/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/12/year/2018'
# espn = 'https://www.espn.com/college-football/schedule/_/week/13/year/2018'
#2017
# espn = 'https://www.espn.com/college-football/schedule/_/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/2/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/3/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/4/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/5/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/6/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/7/year/2017'
# espn ='https://www.espn.com/college-football/schedule/_/week/8/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/9/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/10/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/11/year/2017'
# espn = 'https://www.espn.com/college-football/schedule/_/week/12/year/2017'
#2016
# espn = 'https://www.espn.com/college-football/schedule/_/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/2/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/3/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/4/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/5/year/2016'
# week 6 is not working
# espn = 'https://www.espn.com/college-football/schedule/_/week/7/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/8/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/9/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/10/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/11/year/2016'
# espn = 'https://www.espn.com/college-football/schedule/_/week/12/year/2016'



with urllib.request.urlopen(espn) as url:
    page = url.read()

soup = BeautifulSoup(page, 'html.parser')

score_box = soup.find_all('a', attrs={'name':'&lpos=college-football:schedule:score'})

game_url = []

for x in score_box:
    game_url.append(x['href'])

for x in game_url:
    new_url = base_url + x
    try:
        with urllib.request.urlopen(new_url) as url:
            game_page = url.read()
    except:
        continue

    game_soup = BeautifulSoup(game_page, 'html.parser')

    game_box_score_box = game_soup.find('a', attrs={'name':'&lpos=ncf:game:post:subnav:box score'})
    try:
        box_score_url = game_box_score_box['href']
    except:
        continue

    box_score_url_page = base_url + box_score_url
    try:
        with urllib.request.urlopen(box_score_url_page) as url:
            box_score_page = url.read()
    except:
        continue

    box_score_soup = BeautifulSoup(box_score_page, 'html.parser')

    team_names_box = box_score_soup.find_all('span', attrs={'class':'long-name'})
    for y in team_names_box:
        print(y.text.strip(), end=',')

    # try:
    #     away_team_box = box_score_soup.find('div', attrs={'class': 'team away'})
    #     away_team_rank = away_team_box.find('span', attrs={'class': 'rank'})
    #     print(away_team_rank.text.strip(), end=',')
    # except:
    #     print('-1,')
    #
    # try:
    #     home_team_box = box_score_soup.find('div', attrs={'class', 'team home'})
    #     home_team_rank = home_team_box.find('span', attrs={'class': 'rank'})
    #     print(home_team_rank.text.strip(), end=',')
    # except:
    #     print('-1,')
    #

    away_score_box = box_score_soup.find('div', attrs={'class':'score icon-font-after'})
    home_score_box = box_score_soup.find('div', attrs={'class':'score icon-font-before'})

    print(away_score_box.text.strip(), end=',')
    print(home_score_box.text.strip(), end=',')


    all_stats = box_score_soup.find_all('tr', attrs={'class':'highlight'})

    for y,z in enumerate(all_stats):
        feature_stat = z.find('td', attrs={'class':'yds'})
        clean_feature_stat = feature_stat.text.strip()
        if y == 3:
            print(clean_feature_stat)
            break
        else:
            print(clean_feature_stat, end=',')
    time.sleep(.25)
