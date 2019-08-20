import csv
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random

raw_trainingX = []
raw_trainingY = []

test_x = []
test_y = []

testing_data  = ['researchdata/2018/Week2.csv','researchdata/2018/Week3.csv','researchdata/2018/Week4.csv','researchdata/2018/Week5.csv','researchdata/2018/Week6.csv','researchdata/2018/Week7.csv','researchdata/2018/Week8.csv','researchdata/2018/Week9.csv','researchdata/2018/Week10.csv','researchdata/2018/Week11.csv','researchdata/2018/Week12.csv','researchdata/2018/Week13.csv']
data = ['researchdata/2017/Week2.csv','researchdata/2017/Week3.csv','researchdata/2017/Week4.csv','researchdata/2017/Week5.csv','researchdata/2017/Week6.csv','researchdata/2017/Week7.csv','researchdata/2017/Week8.csv','researchdata/2017/Week9.csv','researchdata/2017/Week10.csv','researchdata/2017/Week11.csv','researchdata/2017/Week12.csv','researchdata/2017/Week13.csv']
data += ['researchdata/2016/Week2.csv','researchdata/2016/Week3.csv','researchdata/2016/Week4.csv','researchdata/2016/Week5.csv','researchdata/2016/Week7.csv','researchdata/2016/Week8.csv','researchdata/2016/Week9.csv','researchdata/2016/Week10.csv','researchdata/2016/Week11.csv','researchdata/2016/Week12.csv','researchdata/2016/Week13.csv']
data += ['researchdata/2015/Week2.csv','researchdata/2015/Week3.csv','researchdata/2015/Week4.csv','researchdata/2015/Week5.csv','researchdata/2015/Week6.csv','researchdata/2015/Week7.csv','researchdata/2015/Week8.csv','researchdata/2015/Week9.csv','researchdata/2015/Week10.csv','researchdata/2015/Week11.csv','researchdata/2015/Week12.csv','researchdata/2015/Week13.csv']
data += ['researchdata/2014/Week2.csv','researchdata/2014/Week3.csv','researchdata/2014/Week4.csv','researchdata/2014/Week5.csv','researchdata/2014/Week6.csv','researchdata/2014/Week7.csv','researchdata/2014/Week8.csv','researchdata/2014/Week9.csv','researchdata/2014/Week10.csv','researchdata/2014/Week11.csv','researchdata/2014/Week12.csv','researchdata/2014/Week13.csv']
data += ['researchdata/2013/Week2.csv','researchdata/2013/Week3.csv','researchdata/2013/Week4.csv','researchdata/2013/Week5.csv','researchdata/2013/Week6.csv','researchdata/2013/Week7.csv','researchdata/2013/Week8.csv','researchdata/2013/Week9.csv','researchdata/2013/Week10.csv','researchdata/2013/Week11.csv','researchdata/2013/Week12.csv','researchdata/2013/Week13.csv']
data += ['researchdata/2012/Week2.csv','researchdata/2012/Week3.csv','researchdata/2012/Week4.csv','researchdata/2012/Week5.csv','researchdata/2012/Week6.csv','researchdata/2012/Week7.csv','researchdata/2012/Week8.csv','researchdata/2012/Week9.csv','researchdata/2012/Week10.csv','researchdata/2012/Week11.csv','researchdata/2012/Week12.csv','researchdata/2012/Week13.csv']
data += ['researchdata/2011/Week2.csv','researchdata/2011/Week3.csv','researchdata/2011/Week4.csv','researchdata/2011/Week5.csv','researchdata/2011/Week6.csv','researchdata/2011/Week7.csv','researchdata/2011/Week8.csv','researchdata/2011/Week9.csv','researchdata/2011/Week10.csv','researchdata/2011/Week11.csv','researchdata/2011/Week12.csv','researchdata/2011/Week13.csv']
data += ['researchdata/2010/Week2.csv','researchdata/2010/Week3.csv','researchdata/2010/Week4.csv','researchdata/2010/Week5.csv','researchdata/2010/Week6.csv','researchdata/2010/Week7.csv','researchdata/2010/Week8.csv','researchdata/2010/Week9.csv','researchdata/2010/Week10.csv','researchdata/2010/Week11.csv','researchdata/2010/Week12.csv','researchdata/2010/Week13.csv']
data += ['researchdata/2009/Week2.csv','researchdata/2009/Week3.csv','researchdata/2009/Week4.csv','researchdata/2009/Week5.csv','researchdata/2009/Week6.csv','researchdata/2009/Week7.csv','researchdata/2009/Week8.csv','researchdata/2009/Week9.csv','researchdata/2009/Week10.csv','researchdata/2009/Week11.csv','researchdata/2009/Week12.csv','researchdata/2009/Week13.csv']


for myfile in testing_data:
    with open(myfile) as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            test_y.append(row[0])
            test_x.append(row[1:])

for myfile in data:
    with open(myfile) as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            raw_trainingY.append(row[0])
            raw_trainingX.append(row[1:])



# random.seed(a=None)
#
# for x in range(500):
#     z = random.randrange(len(raw_trainingX))
#     test_x.append(raw_trainingX.pop(z))
#     test_y.append(raw_trainingY.pop(z))

clf = RandomForestClassifier(n_estimators=1000, max_depth=11, n_jobs=-1)

clf.fit(raw_trainingX, raw_trainingY)
print(clf.feature_importances_)

print(clf.score(raw_trainingX, raw_trainingY))
print(clf.score(test_x, test_y))

print(clf.predict_proba([[50.0,29,45,2,15,187,43,5.0,50.0,69,163,75,111,52,187,5.0]]))
