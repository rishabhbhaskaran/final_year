#data prepared in fourier.csv

import csv
import numpy as np

vector=np.loadtxt(open("fourier.csv", "rb"), delimiter=",", skiprows=1)
res=np.fft.fft2(vector)
s=""
with open('coeff_1.csv','w') as f:
	for ele in res:
		s=str(ele[0])+","+str(ele[1])
		print >> f,s






