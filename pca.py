import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def main():
	data = preprocessing.main()
	std_data = StandardScaler().fit_transform(data)
	cor_mat = np.corrcoef(std_data.T)
	eigval, eigvec = np.linalg.eig(cor_mat)
	print eigval
	eigval = np.sort(eigval)[::-1]
	sum = 0
	for n in eigval:
		sum += n
	num = 0
	var = []
	pcaComponents = np.arange(1, len(data[0])+1, 1)
	s = 0
	no = 1
	f = True
	for n in eigval:
		s += (n/sum)
		var.append(s)
		if s > 0.8 and f:
			num = no
			f = False
		no += 1

	if __name__ == '__main__':
		plt.plot(pcaComponents, var)
		plt.xlabel("No of PCA Components")
		plt.ylabel("Variance")
		plt.show()

	pca_data = PCA(n_components = num).fit_transform(std_data)
	return pca_data

if __name__ == '__main__':
	main()