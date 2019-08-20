import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('datafile')

args = parser.parse_args()

raw_training = []

with open(args.datafile) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        raw_training.append(row)
training = []

passing_offense = []
passing_defense = []
rushing_offense = []
rushing_defense = []
overall_offense = []
overall_defense = []
games_played = {}

for x in raw_training:
    key = x.pop(0)
    myarray = list(map(float, x))
    passing_offense.append((key, myarray[0]/myarray[6]))
    passing_defense.append((key, myarray[1]/myarray[6]))
    rushing_offense.append((key, myarray[2]/myarray[6]))
    rushing_defense.append((key, myarray[3]/myarray[6]))
    overall_offense.append((key, myarray[4]/myarray[6]))
    overall_defense.append((key, myarray[5]/myarray[6]))
    games_played[key] = myarray[6]

passing_offense.sort(key=lambda tup:tup[1], reverse=True)
passing_defense.sort(key=lambda tup:tup[1])
rushing_offense.sort(key=lambda tup:tup[1], reverse=True)
rushing_defense.sort(key=lambda tup:tup[1])
overall_offense.sort(key=lambda tup:tup[1], reverse=True)
overall_defense.sort(key=lambda tup:tup[1])


def printstats(column):
    for x,y in enumerate(column):
        if query == y[0]:
            print(str(x+1), end=' ')

count = 0
while True:
    count += 1
    if count % 2 == 0:
        print()
    query = input("Enter The Team Name: ")
    printstats(passing_offense)
    printstats(passing_defense)
    printstats(rushing_offense)
    printstats(rushing_defense)
    printstats(overall_offense)
    printstats(overall_defense)
    print(games_played[query])
