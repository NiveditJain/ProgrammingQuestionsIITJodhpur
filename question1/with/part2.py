import matplotlib.pyplot as graph
import numpy as array
import math
u=10
theta=array.arange(0,90,1)
def rangef(theta):
	vx=u*math.cos(math.radians(theta))
	vy=u*math.sin(math.radians(theta))
	time=array.arange(0,10,0.0001)
	vyd=vy
	h=0
	hd=h
	for t in time:
		h=hd+vy*0.0001
		vy=vyd+(-9.8-vy)*0.0001
		vyd=vy
		hd=h
		if(h<0):
			return vx*t
range=[]
for tet in theta:
	range.append(rangef(tet))
graph.plot(theta,range)
graph.xlabel("theta")
graph.ylabel("range")
graph.show()