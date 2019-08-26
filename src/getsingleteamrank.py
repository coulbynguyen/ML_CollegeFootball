import csv
import argparse


def get_solo_team_rank(week,team):
    raw_training = []
    filename = 'src/weeklystats/2018/Week' + str(week-1) + '.csv'
    team_rank_filename = 'src/weeklymatchups/2018/Week' + str(week) + '.csv'

    fbs_teams = open("src/fbsteams.txt")
    teams = {}

    for x in fbs_teams:
        teams[x.rstrip()] = True

    fbs_teams.close()

    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            raw_training.append(row)

    team_ranks = {}
    with open(team_rank_filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            away_name = row.pop(0)
            home_name = row.pop(0)
            myarray = list(map(float, row))
            team_ranks[away_name] = row.pop(0)
            team_ranks[home_name] = row.pop(0)

    passing_offense = []
    passing_defense = []
    rushing_offense = []
    rushing_defense = []
    overall_offense = []
    overall_defense = []
    games_played = {}

    for x in raw_training:
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

    team_features = []

    # team_features.append(int(team_ranks[team]))

    features_list = [overall_offense, overall_defense, passing_offense, passing_defense, rushing_offense, rushing_defense]
    for feature in features_list:
        for x,y in enumerate(feature):
            if team == y[0]:
                team_features.append(x+1)

    team_features.append(games_played[team])
    return(team_features)
