#first load centroid points as vector
vector4=np.loadtxt(open("first_diff12.csv", "rb"), delimiter=",", skiprows=1) #change_file_name
d=np.diff(vector4,axis=0)
seg=np.hypot(d[:,0],d[:,1])
for ele in seg:
	print ele
