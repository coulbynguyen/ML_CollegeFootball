import csv
import argparse

# matchupsfilenames = ['weeklymatchups/2018/Week2.csv','weeklymatchups/2018/Week3.csv','weeklymatchups/2018/Week4.csv','weeklymatchups/2018/Week5.csv','weeklymatchups/2018/Week6.csv','weeklymatchups/2018/Week7.csv','weeklymatchups/2018/Week8.csv','weeklymatchups/2018/Week9.csv','weeklymatchups/2018/Week10.csv','weeklymatchups/2018/Week11.csv','weeklymatchups/2018/Week12.csv','weeklymatchups/2018/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2017/Week2.csv','weeklymatchups/2017/Week3.csv','weeklymatchups/2017/Week4.csv','weeklymatchups/2017/Week5.csv','weeklymatchups/2017/Week6.csv','weeklymatchups/2017/Week7.csv','weeklymatchups/2017/Week8.csv','weeklymatchups/2017/Week9.csv','weeklymatchups/2017/Week10.csv','weeklymatchups/2017/Week11.csv','weeklymatchups/2017/Week12.csv','weeklymatchups/2017/Week13.csv']
matchupsfilenames = ['weeklymatchups/2016/Week2.csv','weeklymatchups/2016/Week3.csv','weeklymatchups/2016/Week4.csv','weeklymatchups/2016/Week5.csv','weeklymatchups/2016/Week7.csv','weeklymatchups/2016/Week8.csv','weeklymatchups/2016/Week9.csv','weeklymatchups/2016/Week10.csv','weeklymatchups/2016/Week11.csv','weeklymatchups/2016/Week12.csv','weeklymatchups/2016/Week13.csv']



# statfilenames =     ['weeklystats/2018/Week1.csv','weeklystats/2018/Week2.csv','weeklystats/2018/Week3.csv','weeklystats/2018/Week4.csv','weeklystats/2018/Week5.csv','weeklystats/2018/Week6.csv','weeklystats/2018/Week7.csv','weeklystats/2018/Week8.csv','weeklystats/2018/Week9.csv','weeklystats/2018/Week10.csv','weeklystats/2018/Week11.csv','weeklystats/2018/Week12.csv']
# statfilenames =     ['weeklystats/2017/Week1.csv','weeklystats/2017/Week2.csv','weeklystats/2017/Week3.csv','weeklystats/2017/Week4.csv','weeklystats/2017/Week5.csv','weeklystats/2017/Week6.csv','weeklystats/2017/Week7.csv','weeklystats/2017/Week8.csv','weeklystats/2017/Week9.csv','weeklystats/2017/Week10.csv','weeklystats/2017/Week11.csv','weeklystats/2017/Week12.csv']
statfilenames =     ['weeklystats/2016/Week1.csv','weeklystats/2016/Week2.csv','weeklystats/2016/Week3.csv','weeklystats/2016/Week4.csv','weeklystats/2016/Week5.csv','weeklystats/2016/Week7.csv','weeklystats/2016/Week8.csv','weeklystats/2016/Week9.csv','weeklystats/2016/Week10.csv','weeklystats/2016/Week11.csv','weeklystats/2016/Week12.csv']


def getstats(query, column):
    for x,y in enumerate(column):
        if query == y[0]:
            return (x+1)

for week,(matchup,stat) in enumerate(zip(matchupsfilenames, statfilenames)):
    # filename = 'researchdata/2018/Week' + str(week+2) + '.csv'
    # filename = 'researchdata/2017/Week' + str(week+2) + '.csv'
    filename = 'researchdata/2016/Week' + str(week+2) + '.csv'
    f = open(filename, 'w')
    raw_team_stats = []
    raw_matchups = []

    with open(stat) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            raw_team_stats.append(row)

    with open(matchup) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            raw_matchups.append(row)

    passing_offense = []
    passing_defense = []
    rushing_offense = []
    rushing_defense = []
    overall_offense = []
    overall_defense = []
    games_played = {}

    for x in raw_team_stats:
        key = x.pop(0)
        myarray = list(map(float, x))

        overall_offense.append((key, myarray[0]/myarray[6]))
        overall_defense.append((key, myarray[1]/myarray[6]))

        passing_offense.append((key, myarray[2]/myarray[6]))
        passing_defense.append((key, myarray[3]/myarray[6]))

        rushing_offense.append((key, myarray[4]/myarray[6]))
        rushing_defense.append((key, myarray[5]/myarray[6]))

        games_played[key] = myarray[6]


    overall_offense.sort(key=lambda tup:tup[1], reverse=True)
    overall_defense.sort(key=lambda tup:tup[1])
    passing_offense.sort(key=lambda tup:tup[1], reverse=True)
    passing_defense.sort(key=lambda tup:tup[1])
    rushing_offense.sort(key=lambda tup:tup[1], reverse=True)
    rushing_defense.sort(key=lambda tup:tup[1])

    # print(passing_offense)
    # print(passing_defense)
    # print(rushing_offense)
    # print(rushing_defense)
    # print(overall_offense)
    # print(overall_defense)
    # print(games_played)
    # exit()
    for x in raw_matchups:
        away_team = x.pop(0)
        home_team = x.pop(0)
        myarray = list(map(float, x))
        features = []
        try:
            #add the label first
            features.append(myarray[2])
            #away teams rank
            features.append(myarray[0])
            features.append(getstats(away_team,overall_offense))
            features.append(getstats(away_team,overall_defense))
            features.append(getstats(away_team,passing_offense))
            features.append(getstats(away_team,passing_defense))
            features.append(getstats(away_team,rushing_offense))
            features.append(getstats(away_team,rushing_defense))
            features.append(games_played[away_team])

            #home teams rank
            features.append(myarray[1])
            features.append(getstats(home_team,overall_offense))
            features.append(getstats(home_team,overall_defense))
            features.append(getstats(home_team,passing_offense))
            features.append(getstats(home_team,passing_defense))
            features.append(getstats(home_team,rushing_offense))
            features.append(getstats(home_team,rushing_defense))
            features.append(games_played[home_team])
        except:
            continue


        for y,z in enumerate(features):
            if y == len(features)-1:
                f.write(str(z) + '\n')
            else:
                f.write(str(z) + ',')
