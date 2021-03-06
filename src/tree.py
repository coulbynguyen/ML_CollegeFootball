import csv
import numpy as np
from sklearn import tree
import random
raw_trainingX = []
raw_trainingY = []
data  = ['researchdata/2018/Week2.csv','researchdata/2018/Week3.csv','researchdata/2018/Week4.csv','researchdata/2018/Week5.csv','researchdata/2018/Week6.csv','researchdata/2018/Week7.csv','researchdata/2018/Week8.csv','researchdata/2018/Week9.csv','researchdata/2018/Week10.csv','researchdata/2018/Week11.csv','researchdata/2018/Week12.csv','researchdata/2018/Week13.csv']
data += ['researchdata/2017/Week2.csv','researchdata/2017/Week3.csv','researchdata/2017/Week4.csv','researchdata/2017/Week5.csv','researchdata/2017/Week6.csv','researchdata/2017/Week7.csv','researchdata/2017/Week8.csv','researchdata/2017/Week9.csv','researchdata/2017/Week10.csv','researchdata/2017/Week11.csv','researchdata/2017/Week12.csv','researchdata/2017/Week13.csv']

for myfile in data:
    with open(myfile) as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            raw_trainingY.append(row[0])
            raw_trainingX.append(row[1:])

random.seed(a=None)

test_x = []
test_y = []

for x in range(200):
    z = random.randrange(len(raw_trainingX))
    test_x.append(raw_trainingX.pop(z))
    test_y.append(raw_trainingY.pop(z))


clf = tree.DecisionTreeClassifier()
clf = clf.fit(raw_trainingX, raw_trainingY)
print(clf.score(raw_trainingX, raw_trainingY))
print(clf.get_depth())
print(clf.get_n_leaves())

print(clf.score(test_x, test_y))
