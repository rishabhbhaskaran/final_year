from pylab import *

def sin_cos_waves(data,times):
	f = fft(data)
	N = len(data)
	# The real components of the fft are the cos components, the imaginary are the sin 
	fN2 = f[:(N/2)]
	am = real(fN2)
	bm = imag(fN2)

	# For each weight up to N/2 we calculate sin/cos for each time period and weight accordingly 
	# something is still wrong here in terms of the scale, but it is almost there
	allsin = [bm[i] * sin((times*i))/N for i in range(len(bm))]
	allcos = [am[i] * cos((times*i))/N for i in range(len(am))]

	return allsin + allcos


def drawall(a):
	# A bunch of time...for argument sake one complete rotation
	t = arange(0,pi*2,0.001)
	waves = sin_cos_waves(a,t)
	figure()
	print len(waves)
	for x in waves:
		plot(x)

	figure()

	sumwaves = sum(waves,axis=0)
	plot(sumwaves)
	dataroll = roll(a,0)
	y = [[x]*(len(t)/len(a)) for x in dataroll]
	y = [item for sublist in y for item in sublist]
	plot(y)
	rng = max(a)-min(a)

	ylim([min(a)-rng*0.1,max(a)+rng*0.1]);

# Mark's example
data = np.loadtxt(open("data1.csv", "rb"), delimiter=",", skiprows=1) #change_file_name
drawall(data)

# A box wave
#data = [0]*100 + [1]*100 + [0]*100
#drawall(data)

#show()
