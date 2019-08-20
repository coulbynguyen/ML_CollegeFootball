import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random

def get_prediction(query):
    raw_trainingX = []
    raw_trainingY = []

    data = ['src/researchdata/2017/Week2.csv','src/researchdata/2017/Week3.csv','src/researchdata/2017/Week4.csv','src/researchdata/2017/Week5.csv','src/researchdata/2017/Week6.csv','src/researchdata/2017/Week7.csv','src/researchdata/2017/Week8.csv','src/researchdata/2017/Week9.csv','src/researchdata/2017/Week10.csv','src/researchdata/2017/Week11.csv','src/researchdata/2017/Week12.csv','src/researchdata/2017/Week13.csv']
    data += ['src/researchdata/2016/Week2.csv','src/researchdata/2016/Week3.csv','src/researchdata/2016/Week4.csv','src/researchdata/2016/Week5.csv','src/researchdata/2016/Week7.csv','src/researchdata/2016/Week8.csv','src/researchdata/2016/Week9.csv','src/researchdata/2016/Week10.csv','src/researchdata/2016/Week11.csv','src/researchdata/2016/Week12.csv','src/researchdata/2016/Week13.csv']
    data += ['src/researchdata/2015/Week2.csv','src/researchdata/2015/Week3.csv','src/researchdata/2015/Week4.csv','src/researchdata/2015/Week5.csv','src/researchdata/2015/Week6.csv','src/researchdata/2015/Week7.csv','src/researchdata/2015/Week8.csv','src/researchdata/2015/Week9.csv','src/researchdata/2015/Week10.csv','src/researchdata/2015/Week11.csv','src/researchdata/2015/Week12.csv','src/researchdata/2015/Week13.csv']
    data += ['src/researchdata/2014/Week2.csv','src/researchdata/2014/Week3.csv','src/researchdata/2014/Week4.csv','src/researchdata/2014/Week5.csv','src/researchdata/2014/Week6.csv','src/researchdata/2014/Week7.csv','src/researchdata/2014/Week8.csv','src/researchdata/2014/Week9.csv','src/researchdata/2014/Week10.csv','src/researchdata/2014/Week11.csv','src/researchdata/2014/Week12.csv','src/researchdata/2014/Week13.csv']
    data += ['src/researchdata/2013/Week2.csv','src/researchdata/2013/Week3.csv','src/researchdata/2013/Week4.csv','src/researchdata/2013/Week5.csv','src/researchdata/2013/Week6.csv','src/researchdata/2013/Week7.csv','src/researchdata/2013/Week8.csv','src/researchdata/2013/Week9.csv','src/researchdata/2013/Week10.csv','src/researchdata/2013/Week11.csv','src/researchdata/2013/Week12.csv','src/researchdata/2013/Week13.csv']
    data += ['src/researchdata/2012/Week2.csv','src/researchdata/2012/Week3.csv','src/researchdata/2012/Week4.csv','src/researchdata/2012/Week5.csv','src/researchdata/2012/Week6.csv','src/researchdata/2012/Week7.csv','src/researchdata/2012/Week8.csv','src/researchdata/2012/Week9.csv','src/researchdata/2012/Week10.csv','src/researchdata/2012/Week11.csv','src/researchdata/2012/Week12.csv','src/researchdata/2012/Week13.csv']
    data += ['src/researchdata/2011/Week2.csv','src/researchdata/2011/Week3.csv','src/researchdata/2011/Week4.csv','src/researchdata/2011/Week5.csv','src/researchdata/2011/Week6.csv','src/researchdata/2011/Week7.csv','src/researchdata/2011/Week8.csv','src/researchdata/2011/Week9.csv','src/researchdata/2011/Week10.csv','src/researchdata/2011/Week11.csv','src/researchdata/2011/Week12.csv','src/researchdata/2011/Week13.csv']
    data += ['src/researchdata/2010/Week2.csv','src/researchdata/2010/Week3.csv','src/researchdata/2010/Week4.csv','src/researchdata/2010/Week5.csv','src/researchdata/2010/Week6.csv','src/researchdata/2010/Week7.csv','src/researchdata/2010/Week8.csv','src/researchdata/2010/Week9.csv','src/researchdata/2010/Week10.csv','src/researchdata/2010/Week11.csv','src/researchdata/2010/Week12.csv','src/researchdata/2010/Week13.csv']
    data += ['src/researchdata/2009/Week2.csv','src/researchdata/2009/Week3.csv','src/researchdata/2009/Week4.csv','src/researchdata/2009/Week5.csv','src/researchdata/2009/Week6.csv','src/researchdata/2009/Week7.csv','src/researchdata/2009/Week8.csv','src/researchdata/2009/Week9.csv','src/researchdata/2009/Week10.csv','src/researchdata/2009/Week11.csv','src/researchdata/2009/Week12.csv','src/researchdata/2009/Week13.csv']

    for myfile in data:
        with open(myfile) as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                raw_trainingY.append(row[0])
                raw_trainingX.append(row[1:])

    clf = RandomForestClassifier(n_estimators=1000, max_depth=11, n_jobs=-1)

    clf.fit(raw_trainingX, raw_trainingY)

    return(clf.predict_proba([query]))
