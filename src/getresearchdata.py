import csv
import argparse

matchupsfilenames = ['weeklymatchups/2018/Week2.csv','weeklymatchups/2018/Week3.csv','weeklymatchups/2018/Week4.csv','weeklymatchups/2018/Week5.csv','weeklymatchups/2018/Week6.csv','weeklymatchups/2018/Week7.csv','weeklymatchups/2018/Week8.csv','weeklymatchups/2018/Week9.csv','weeklymatchups/2018/Week10.csv','weeklymatchups/2018/Week11.csv','weeklymatchups/2018/Week12.csv','weeklymatchups/2018/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2017/Week2.csv','weeklymatchups/2017/Week3.csv','weeklymatchups/2017/Week4.csv','weeklymatchups/2017/Week5.csv','weeklymatchups/2017/Week6.csv','weeklymatchups/2017/Week7.csv','weeklymatchups/2017/Week8.csv','weeklymatchups/2017/Week9.csv','weeklymatchups/2017/Week10.csv','weeklymatchups/2017/Week11.csv','weeklymatchups/2017/Week12.csv','weeklymatchups/2017/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2016/Week2.csv','weeklymatchups/2016/Week3.csv','weeklymatchups/2016/Week4.csv','weeklymatchups/2016/Week5.csv','weeklymatchups/2016/Week7.csv','weeklymatchups/2016/Week8.csv','weeklymatchups/2016/Week9.csv','weeklymatchups/2016/Week10.csv','weeklymatchups/2016/Week11.csv','weeklymatchups/2016/Week12.csv','weeklymatchups/2016/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2015/Week2.csv','weeklymatchups/2015/Week3.csv','weeklymatchups/2015/Week4.csv','weeklymatchups/2015/Week5.csv','weeklymatchups/2015/Week6.csv','weeklymatchups/2015/Week7.csv','weeklymatchups/2015/Week8.csv','weeklymatchups/2015/Week9.csv','weeklymatchups/2015/Week10.csv','weeklymatchups/2015/Week11.csv','weeklymatchups/2015/Week12.csv','weeklymatchups/2015/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2014/Week2.csv','weeklymatchups/2014/Week3.csv','weeklymatchups/2014/Week4.csv','weeklymatchups/2014/Week5.csv','weeklymatchups/2014/Week6.csv','weeklymatchups/2014/Week7.csv','weeklymatchups/2014/Week8.csv','weeklymatchups/2014/Week9.csv','weeklymatchups/2014/Week10.csv','weeklymatchups/2014/Week11.csv','weeklymatchups/2014/Week12.csv','weeklymatchups/2014/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2013/Week2.csv','weeklymatchups/2013/Week3.csv','weeklymatchups/2013/Week4.csv','weeklymatchups/2013/Week5.csv','weeklymatchups/2013/Week6.csv','weeklymatchups/2013/Week7.csv','weeklymatchups/2013/Week8.csv','weeklymatchups/2013/Week9.csv','weeklymatchups/2013/Week10.csv','weeklymatchups/2013/Week11.csv','weeklymatchups/2013/Week12.csv','weeklymatchups/2013/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2012/Week2.csv','weeklymatchups/2012/Week3.csv','weeklymatchups/2012/Week4.csv','weeklymatchups/2012/Week5.csv','weeklymatchups/2012/Week6.csv','weeklymatchups/2012/Week7.csv','weeklymatchups/2012/Week8.csv','weeklymatchups/2012/Week9.csv','weeklymatchups/2012/Week10.csv','weeklymatchups/2012/Week11.csv','weeklymatchups/2012/Week12.csv','weeklymatchups/2012/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2011/Week2.csv','weeklymatchups/2011/Week3.csv','weeklymatchups/2011/Week4.csv','weeklymatchups/2011/Week5.csv','weeklymatchups/2011/Week6.csv','weeklymatchups/2011/Week7.csv','weeklymatchups/2011/Week8.csv','weeklymatchups/2011/Week9.csv','weeklymatchups/2011/Week10.csv','weeklymatchups/2011/Week11.csv','weeklymatchups/2011/Week12.csv','weeklymatchups/2011/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2010/Week2.csv','weeklymatchups/2010/Week3.csv','weeklymatchups/2010/Week4.csv','weeklymatchups/2010/Week5.csv','weeklymatchups/2010/Week6.csv','weeklymatchups/2010/Week7.csv','weeklymatchups/2010/Week8.csv','weeklymatchups/2010/Week9.csv','weeklymatchups/2010/Week10.csv','weeklymatchups/2010/Week11.csv','weeklymatchups/2010/Week12.csv','weeklymatchups/2010/Week13.csv']
# matchupsfilenames = ['weeklymatchups/2009/Week2.csv','weeklymatchups/2009/Week3.csv','weeklymatchups/2009/Week4.csv','weeklymatchups/2009/Week5.csv','weeklymatchups/2009/Week6.csv','weeklymatchups/2009/Week7.csv','weeklymatchups/2009/Week8.csv','weeklymatchups/2009/Week9.csv','weeklymatchups/2009/Week10.csv','weeklymatchups/2009/Week11.csv','weeklymatchups/2009/Week12.csv','weeklymatchups/2009/Week13.csv']



statfilenames =     ['weeklystats/2018/Week1.csv','weeklystats/2018/Week2.csv','weeklystats/2018/Week3.csv','weeklystats/2018/Week4.csv','weeklystats/2018/Week5.csv','weeklystats/2018/Week6.csv','weeklystats/2018/Week7.csv','weeklystats/2018/Week8.csv','weeklystats/2018/Week9.csv','weeklystats/2018/Week10.csv','weeklystats/2018/Week11.csv','weeklystats/2018/Week12.csv']
# statfilenames =     ['weeklystats/2017/Week1.csv','weeklystats/2017/Week2.csv','weeklystats/2017/Week3.csv','weeklystats/2017/Week4.csv','weeklystats/2017/Week5.csv','weeklystats/2017/Week6.csv','weeklystats/2017/Week7.csv','weeklystats/2017/Week8.csv','weeklystats/2017/Week9.csv','weeklystats/2017/Week10.csv','weeklystats/2017/Week11.csv','weeklystats/2017/Week12.csv']
# statfilenames =     ['weeklystats/2016/Week1.csv','weeklystats/2016/Week2.csv','weeklystats/2016/Week3.csv','weeklystats/2016/Week4.csv','weeklystats/2016/Week5.csv','weeklystats/2016/Week7.csv','weeklystats/2016/Week8.csv','weeklystats/2016/Week9.csv','weeklystats/2016/Week10.csv','weeklystats/2016/Week11.csv','weeklystats/2016/Week12.csv']
# statfilenames =     ['weeklystats/2015/Week1.csv','weeklystats/2015/Week2.csv','weeklystats/2015/Week3.csv','weeklystats/2015/Week4.csv','weeklystats/2015/Week5.csv','weeklystats/2015/Week6.csv','weeklystats/2015/Week7.csv','weeklystats/2015/Week8.csv','weeklystats/2015/Week9.csv','weeklystats/2015/Week10.csv','weeklystats/2015/Week11.csv','weeklystats/2015/Week12.csv']
# statfilenames =     ['weeklystats/2014/Week1.csv','weeklystats/2014/Week2.csv','weeklystats/2014/Week3.csv','weeklystats/2014/Week4.csv','weeklystats/2014/Week5.csv','weeklystats/2014/Week6.csv','weeklystats/2014/Week7.csv','weeklystats/2014/Week8.csv','weeklystats/2014/Week9.csv','weeklystats/2014/Week10.csv','weeklystats/2014/Week11.csv','weeklystats/2014/Week12.csv']
# statfilenames =     ['weeklystats/2013/Week1.csv','weeklystats/2013/Week2.csv','weeklystats/2013/Week3.csv','weeklystats/2013/Week4.csv','weeklystats/2013/Week5.csv','weeklystats/2013/Week6.csv','weeklystats/2013/Week7.csv','weeklystats/2013/Week8.csv','weeklystats/2013/Week9.csv','weeklystats/2013/Week10.csv','weeklystats/2013/Week11.csv','weeklystats/2013/Week12.csv']
# statfilenames =     ['weeklystats/2012/Week1.csv','weeklystats/2012/Week2.csv','weeklystats/2012/Week3.csv','weeklystats/2012/Week4.csv','weeklystats/2012/Week5.csv','weeklystats/2012/Week6.csv','weeklystats/2012/Week7.csv','weeklystats/2012/Week8.csv','weeklystats/2012/Week9.csv','weeklystats/2012/Week10.csv','weeklystats/2012/Week11.csv','weeklystats/2012/Week12.csv']
# statfilenames =     ['weeklystats/2011/Week1.csv','weeklystats/2011/Week2.csv','weeklystats/2011/Week3.csv','weeklystats/2011/Week4.csv','weeklystats/2011/Week5.csv','weeklystats/2011/Week6.csv','weeklystats/2011/Week7.csv','weeklystats/2011/Week8.csv','weeklystats/2011/Week9.csv','weeklystats/2011/Week10.csv','weeklystats/2011/Week11.csv','weeklystats/2011/Week12.csv']
# statfilenames =     ['weeklystats/2010/Week1.csv','weeklystats/2010/Week2.csv','weeklystats/2010/Week3.csv','weeklystats/2010/Week4.csv','weeklystats/2010/Week5.csv','weeklystats/2010/Week6.csv','weeklystats/2010/Week7.csv','weeklystats/2010/Week8.csv','weeklystats/2010/Week9.csv','weeklystats/2010/Week10.csv','weeklystats/2010/Week11.csv','weeklystats/2010/Week12.csv']
# statfilenames =     ['weeklystats/2009/Week1.csv','weeklystats/2009/Week2.csv','weeklystats/2009/Week3.csv','weeklystats/2009/Week4.csv','weeklystats/2009/Week5.csv','weeklystats/2009/Week6.csv','weeklystats/2009/Week7.csv','weeklystats/2009/Week8.csv','weeklystats/2009/Week9.csv','weeklystats/2009/Week10.csv','weeklystats/2009/Week11.csv','weeklystats/2009/Week12.csv']

fbs_teams = open("fbsteams.txt")
teams = {}

for x in fbs_teams:
    teams[x.rstrip()] = True

def getstats(query, column):
    for x,y in enumerate(column):
        if query == y[0]:
            return (x+1)


for week,(matchup,stat) in enumerate(zip(matchupsfilenames, statfilenames)):
    filename = 'FBSresearchdata/2018/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2017/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2016/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2015/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2014/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2013/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2012/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2011/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2010/Week' + str(week+2) + '.csv'
    # filename = 'FBSresearchdata/2009/Week' + str(week+2) + '.csv'
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
        try:
            val = teams[key]
        except:
            continue
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
            try:
                val = teams[away_team]
            except:
                continue
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
            try:
                val = teams[home_team]
            except:
                continue
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
