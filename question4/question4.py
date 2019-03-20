import matplotlib.pyplot as graph
import numpy as numbers
#assuming ball is thrown up with a velocity of 10m/sec 
#cofficient of resitution is 0.75
time=numbers.arange(0,10,0.000001)
t0=0
v=10
e=0.75
h=0
height=[]
for x in time:
	h=v*(x-t0)-5*(x-t0)*(x-t0)
	if(h<0):
		h=0
		t0=x
		v=e*v
	height.append(h)
graph.xlabel("time")
graph.ylabel("height")
graph.plot(time,height)
graph.show()