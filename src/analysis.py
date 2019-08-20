import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
import random

raw_trainingX = []
raw_trainingY = []
data  = ['researchdata/2018/Week2.csv','researchdata/2018/Week3.csv','researchdata/2018/Week4.csv','researchdata/2018/Week5.csv','researchdata/2018/Week6.csv','researchdata/2018/Week7.csv','researchdata/2018/Week8.csv','researchdata/2018/Week9.csv','researchdata/2018/Week10.csv','researchdata/2018/Week11.csv','researchdata/2018/Week12.csv','researchdata/2018/Week13.csv']
data += ['researchdata/2017/Week2.csv','researchdata/2017/Week3.csv','researchdata/2017/Week4.csv','researchdata/2017/Week5.csv','researchdata/2017/Week6.csv','researchdata/2017/Week7.csv','researchdata/2017/Week8.csv','researchdata/2017/Week9.csv','researchdata/2017/Week10.csv','researchdata/2017/Week11.csv','researchdata/2017/Week12.csv','researchdata/2017/Week13.csv']
data += ['researchdata/2016/Week2.csv','researchdata/2016/Week3.csv','researchdata/2016/Week4.csv','researchdata/2016/Week5.csv','researchdata/2016/Week7.csv','researchdata/2016/Week8.csv','researchdata/2016/Week9.csv','researchdata/2016/Week10.csv','researchdata/2016/Week11.csv','researchdata/2016/Week12.csv','researchdata/2016/Week13.csv']
data += ['researchdata/2015/Week2.csv','researchdata/2015/Week3.csv','researchdata/2015/Week4.csv','researchdata/2015/Week5.csv','researchdata/2015/Week6.csv','researchdata/2015/Week7.csv','researchdata/2015/Week8.csv','researchdata/2015/Week9.csv','researchdata/2015/Week10.csv','researchdata/2015/Week11.csv','researchdata/2015/Week12.csv','researchdata/2015/Week13.csv']
data += ['researchdata/2014/Week2.csv','researchdata/2014/Week3.csv','researchdata/2014/Week4.csv','researchdata/2014/Week5.csv','researchdata/2014/Week6.csv','researchdata/2014/Week7.csv','researchdata/2014/Week8.csv','researchdata/2014/Week9.csv','researchdata/2014/Week10.csv','researchdata/2014/Week11.csv','researchdata/2014/Week12.csv','researchdata/2014/Week13.csv']

for myfile in data:
    with open(myfile) as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            raw_trainingY.append(row[0])
            raw_trainingX.append(row[1:])


random.seed(a=None)

test_x = []
test_y = []

for x in range(500):
    z = random.randrange(len(raw_trainingX))
    test_x.append(raw_trainingX.pop(z))
    test_y.append(raw_trainingY.pop(z))


logreg = LogisticRegression(C=1e5, solver='liblinear', max_iter=1000)

logreg.fit(raw_trainingX, raw_trainingY)


print(logreg.score(raw_trainingX, raw_trainingY))
print(logreg.score(test_x, test_y))


print(logreg.coef_)
print(logreg.intercept_)
print(logreg.n_iter_)
