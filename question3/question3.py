import matplotlib.pyplot as graph
import numpy as array
import math
#assuming length of pendulum is equal to g
theta=array.arange(0,90,1)
dt=0.001
time=array.arange(0,70,dt)
def timer(the):
	w=0
	o=the
	for t in time:
		w=w+math.sin(math.radians(o))*dt
		o=o-w*dt
		if(o<=-the):
			return 2*t
period=[]
for x in theta:
	period.append(timer(x))
graph.xlabel("theta")
graph.ylabel("time")
graph.plot(period)
graph.show()