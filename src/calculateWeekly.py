import csv

# datafiles = ['data/2018/week1year2018.csv','data/2018/week2year2018.csv','data/2018/week3year2018.csv','data/2018/week4year2018.csv','data/2018/week5year2018.csv','data/2018/week6year2018.csv','data/2018/week7year2018.csv','data/2018/week8year2018.csv','data/2018/week9year2018.csv','data/2018/week10year2018.csv','data/2018/week11year2018.csv','data/2018/week12year2018.csv','data/2018/week13year2018.csv']
# datafiles = ['data/2017/Week1.csv','data/2017/Week2.csv','data/2017/Week3.csv','data/2017/Week4.csv','data/2017/Week5.csv','data/2017/Week6.csv','data/2017/Week7.csv','data/2017/Week8.csv','data/2017/Week9.csv','data/2017/Week10.csv','data/2017/Week11.csv','data/2017/Week12.csv']
# datafiles = ['data/2016/Week1.csv','data/2016/Week2.csv','data/2016/Week3.csv','data/2016/Week4.csv','data/2016/Week5.csv','data/2016/Week7.csv','data/2016/Week8.csv','data/2016/Week9.csv','data/2016/Week10.csv','data/2016/Week11.csv','data/2016/Week12.csv']
# datafiles = ['data/2015/Week1.csv','data/2015/Week2.csv','data/2015/Week3.csv','data/2015/Week4.csv','data/2015/Week5.csv','data/2015/Week6.csv','data/2015/Week7.csv','data/2015/Week8.csv','data/2015/Week9.csv','data/2015/Week10.csv','data/2015/Week11.csv','data/2015/Week12.csv']
# datafiles = ['data/2014/Week1.csv','data/2014/Week2.csv','data/2014/Week3.csv','data/2014/Week4.csv','data/2014/Week5.csv','data/2014/Week6.csv','data/2014/Week7.csv','data/2014/Week8.csv','data/2014/Week9.csv','data/2014/Week10.csv','data/2014/Week11.csv','data/2014/Week12.csv']
# datafiles = ['data/2013/Week1.csv','data/2013/Week2.csv','data/2013/Week3.csv','data/2013/Week4.csv','data/2013/Week5.csv','data/2013/Week6.csv','data/2013/Week7.csv','data/2013/Week8.csv','data/2013/Week9.csv','data/2013/Week10.csv','data/2013/Week11.csv','data/2013/Week12.csv']
# datafiles = ['data/2012/Week1.csv','data/2012/Week2.csv','data/2012/Week3.csv','data/2012/Week4.csv','data/2012/Week5.csv','data/2012/Week6.csv','data/2012/Week7.csv','data/2012/Week8.csv','data/2012/Week9.csv','data/2012/Week10.csv','data/2012/Week11.csv','data/2012/Week12.csv']
# datafiles = ['data/2011/Week1.csv','data/2011/Week2.csv','data/2011/Week3.csv','data/2011/Week4.csv','data/2011/Week5.csv','data/2011/Week6.csv','data/2011/Week7.csv','data/2011/Week8.csv','data/2011/Week9.csv','data/2011/Week10.csv','data/2011/Week11.csv','data/2011/Week12.csv']
# datafiles = ['data/2010/Week1.csv','data/2010/Week2.csv','data/2010/Week3.csv','data/2010/Week4.csv','data/2010/Week5.csv','data/2010/Week6.csv','data/2010/Week7.csv','data/2010/Week8.csv','data/2010/Week9.csv','data/2010/Week10.csv','data/2010/Week11.csv','data/2010/Week12.csv']
datafiles = ['data/2009/Week1.csv','data/2009/Week2.csv','data/2009/Week3.csv','data/2009/Week4.csv','data/2009/Week5.csv','data/2009/Week6.csv','data/2009/Week7.csv','data/2009/Week8.csv','data/2009/Week9.csv','data/2009/Week10.csv','data/2009/Week11.csv','data/2009/Week12.csv']



teamstats = {}

for week,file in enumerate(datafiles):
    raw_training = []

    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            raw_training.append(row)

    for x in raw_training:
        away = x.pop(0)
        home = x.pop(0)
        myarray = list(map(float, x))
        try:
            #points scored
            teamstats[away][0] += myarray[0]
            #points allowed
            teamstats[away][1] += myarray[1]
            #passing yards gained
            teamstats[away][2] += myarray[2]
            #passing yards allowed
            teamstats[away][3] += myarray[3]
            #rushing yards gained
            teamstats[away][4] += myarray[4]
            #rushing yards allowed
            teamstats[away][5] += myarray[5]
            #number of bcs games played
            teamstats[away][6] += 1
        except:
            teamstats[away] = [myarray[0], myarray[1], myarray[2], myarray[3], myarray[4], myarray[5], 1]

        try:
            #points scored
            teamstats[home][0] += myarray[1]
            #points allowed
            teamstats[home][1] += myarray[0]
            #passing yards gained
            teamstats[home][2] += myarray[3]
            #passing yards allowed
            teamstats[home][3] += myarray[2]
            #rushing yards gained
            teamstats[home][4] += myarray[5]
            #rushing yards allowed
            teamstats[home][5] += myarray[4]
            #number of bcs games played
            teamstats[home][6] += 1
        except:
            teamstats[home] = [myarray[1], myarray[0], myarray[3], myarray[2], myarray[5], myarray[4], 1]

    filename = "weeklystats/2009/Week" + str(week+1) + ".csv"
    f = open(filename, "w")

    for x in teamstats:
        f.write(str(x) + ',')
        f.write(str(teamstats[x][0]) + ',')
        f.write(str(teamstats[x][1]) + ',')
        f.write(str(teamstats[x][2]) + ',')
        f.write(str(teamstats[x][3]) + ',')
        f.write(str(teamstats[x][4]) + ',')
        f.write(str(teamstats[x][5]) + ',')
        f.write(str(teamstats[x][6]) + '\n')
    f.close()
