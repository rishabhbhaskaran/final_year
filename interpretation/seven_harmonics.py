import matplotlib.pyplot as plt
from pylab import *

def vec(filename):
	data= np.loadtxt(open(filename, "rb"), delimiter=",", skiprows=1)
	f = fft(data)
	N = len(data)
#freq=[]
	amp1=[]
#amp2=[]
# The real components of the fft are the cos components, the imaginary are the sin 
	fN2 = f[:(N/2)]
	am = real(fN2)
	bm = imag(fN2)
	times=arange(0,2*pi,0.001)

	fig, ax = plt.subplots()
#ax.set_color_cycle(['red', 'black', 'yellow'])

#first harmonics
	print "first harmonic"
	sin0=bm[0] * sin((times*1))/N
	cos0=am[0] * cos((times*1))/N
	harm1=sin0 + cos0
	amp1.append(max(harm1))
	#plt.plot(harm1,label='1st'.format(True))

#second harmonic
	print "second harmonic"
	sin0=bm[1] * sin((times*2))/N
	cos0=am[1] * cos((times*2))/N
	harm2=sin0 + cos0
	amp1.append(max(harm2))
	#plt.plot(harm2,label='2nd'.format(True))

#third harmonic
	print "third harmonic"
	sin0=bm[2] * sin((times*3))/N
	cos0=am[2] * cos((times*3))/N
	harm2=sin0 + cos0
	amp1.append(max(harm2))
	#plt.plot(harm2,label='3rd'.format(True))

#fourth harmonic
	print "fourth harmonic"
	sin0=bm[3] * sin((times*4))/N
	cos0=am[3] * cos((times*4))/N
	harm2=sin0 + cos0
	amp1.append(max(harm2))
	#plt.plot(harm2,label='4th'.format(True))

#fifth harmonic
	print "five harmonic"
	sin0=bm[4] * sin((times*5))/N
	cos0=am[4] * cos((times*5))/N
	harm2=sin0 + cos0
	amp1.append(max(harm2))
	#plt.plot(harm2,label='5th'.format(True))

#sixth harmonic
	print "six harmonic"
	sin0=bm[5] * sin((times*6))/N
	cos0=am[5] * cos((times*6))/N
	harm2=sin0 + cos0
	amp1.append(max(harm2))
	#plt.plot(harm2,label='6th'.format(True))

#seventh harmonic
	print "seven harmonic"
	sin0=bm[6] * sin((times*7))/N
	cos0=am[6] * cos((times*7))/N
	harm2=sin0 + cos0
	amp1.append(max(harm2))
	#plt.plot(harm2,label='7th'.format(True))
	return amp1


'''
data1= np.loadtxt(open("data2.csv", "rb"), delimiter=",", skiprows=1)
f1 = fft(data1)
N1 = len(data1)
# The real components of the fft are the cos components, the imaginary are the sin 
fN21 = f[:(N1/2)]
am1 = real(fN21)
bm1 = imag(fN21)
times=arange(0,2*pi,0.001)

fig, ax = plt.subplots()
#ax.set_color_cycle(['red', 'black', 'yellow'])

#first harmonics
print "first harmonic"
sin0=bm1[0] * sin((times*1))/N
cos0=am1[0] * cos((times*1))/N
harm1=sin0 + cos0
amp2.append(max(harm1))
#plt.plot(harm1,label='1st'.format(True))

#second harmonic
print "second harmonic"
sin0=bm1[1] * sin((times*2))/N
cos0=am1[1] * cos((times*2))/N
harm2=sin0 + cos0
amp2.append(max(harm2))
#plt.plot(harm2,label='2nd'.format(True))

#third harmonic
print "third harmonic"
sin0=bm1[2] * sin((times*3))/N
cos0=am1[2] * cos((times*3))/N
harm2=sin0 + cos0
amp2.append(max(harm2))
#plt.plot(harm2,label='3rd'.format(True))

#fourth harmonic
print "fourth harmonic"
sin0=bm1[3] * sin((times*4))/N
cos0=am1[3] * cos((times*4))/N
harm2=sin0 + cos0
amp2.append(max(harm2))
#plt.plot(harm2,label='4th'.format(True))

#fifth harmonic
print "five harmonic"
sin0=bm1[4] * sin((times*5))/N
cos0=am1[4] * cos((times*5))/N
harm2=sin0 + cos0
amp2.append(max(harm2))
#plt.plot(harm2,label='5th'.format(True))

#sixth harmonic
print "six harmonic"
sin0=bm1[5] * sin((times*6))/N
cos0=am1[5] * cos((times*6))/N
harm2=sin0 + cos0
amp2.append(max(harm2))
#plt.plot(harm2,label='6th'.format(True))

#seventh harmonic
print "seven harmonic"
sin0=bm1[6] * sin((times*7))/N
cos0=am1[6] * cos((times*7))/N
harm2=sin0 + cos0
amp2.append(max(harm2))
#plt.plot(harm2,label='7th'.format(True))

'''


v1=vec("data1.csv")
v2=vec("data2.csv")

v1=np.array(v1) #daytime
v2=np.array(v2) #lasttime

activity_score1=0
activity_score2=0

diff_vec=v1-v2

for i in range(len(diff_vec)):
	if diff_vec[i] > 0:
		activity_score1+=abs(diff_vec[i])*i
	elif diff_vec[i] < 0:
		activity_score2+=abs(diff_vec[i])*i


		
	


#plt.legend(loc='best')
#plt.show()




	# For each weight up to N/2 we calculate sin/cos for each time period and weight accordingly 
	# something is still wrong here in terms of the scale, but it is almost there
#allsin = [bm[i] * sin((times*i))/N for i in range(len(bm))]
#allcos = [am[i] * cos((times*i))/N for i in range(len(am))]

