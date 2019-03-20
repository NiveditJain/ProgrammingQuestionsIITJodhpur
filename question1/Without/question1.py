import matplotlib.pyplot as graph
import numpy as array
import math
time=array.arange(0,10,0.0001)
#let u=10m/s
#theta=37degree
vx=6
vy=8
x=[]
y=[]
h=0
for t in time:
	h=vx*t-5*t*t
	if(h<0):
		break
	x.append(vx*t)
	y.append(h)
graph.title("Without Air Resistance")
graph.plot(x,y)
graph.show()

graph.title("range as a funtion of theta")
o=array.arange(0,90,1)
r=[]
for O in o:
	r.append(10*math.sin(2*math.radians(O)))
graph.plot(o,r)
graph.show()