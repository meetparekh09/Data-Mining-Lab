from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import pca
import csv


def plotK(data, verbose = False, r = 20):
	k = []
	iner = []
	for i in range(2, r+1):
		if(verbose):
			print 'Training for clusters = '+str(i)+'\n'
		k.append(i)
		iner.append(KMeans(n_clusters = i).fit(data).inertia_)
	plt.plot(k, iner)
	plt.xlabel('K')
	plt.ylabel('Inertia')
	plt.show()

def main(no):
	data = pca.main()
	kmeans = KMeans(n_clusters = no).fit_predict(data)
	wr = []

	for i in range(0, len(data)):
		wrt = []
		for no in data[i]:
			wrt.append(no)
		wrt.append(kmeans[i])
		wr.append(wrt)

	csvfile = open('cluster_result.csv', 'wb')
	writer = csv.writer(csvfile)
	writer.writerows(wr)

if __name__ == '__main__':
	main()