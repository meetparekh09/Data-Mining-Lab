from sklearn import svm
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

reader = csv.reader(open('cluster_result.csv', 'rb'), delimiter = ',')
f = []
for row in reader:
	f.append(row)
f = np.array(f)
data = f[:, 0:5]
result = f[:, 5]
train = len(data)*3/4

def plot():
	c = np.arange(0.1, 1.1, 0.1)
	acc = []
	tacc = []
	for C in c:
		print 'C = '+str(C)
		clf = svm.SVC(C = C).fit(data[:train], result[:train])
		acc.append(100*clf.score(data[train:], result[train:]))
		tacc.append(100*clf.score(data[:train], result[:train]))
	lamb = 1/c
	print lamb
	print acc
	plt.plot(lamb, acc, 'r')
	plt.plot(lamb, tacc, 'b')
	plt.xlabel("Lambda")
	plt.ylabel("Accuracy")
	red_patch = mpatches.Patch(color = 'red', label = 'Cross Validation Set')
	blue_patch = mpatches.Patch(color = 'blue', label = 'Training Set')
	plt.legend(handles=[red_patch, blue_patch])
	plt.show()
