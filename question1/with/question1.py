import matplotlib.pyplot as graph
import numpy as array
import math
u=10
theta=37
vx=u*math.cos(math.radians(theta))
vy=u*math.sin(math.radians(theta))
time=array.arange(0,10,0.0001)
he=[]
x=[]
vyd=vy
h=0
hd=h

time1=array.arange(0,10,0.0001)
#let u=10m/s
#theta=37degree
vx1=6
vy1=8
x1=[]
y1=[]
h1=0
for t1 in time:
	h1=vx1*t1-5*t1*t1
	if(h1<0):
		break
	x1.append(vx1*t1)
	y1.append(h1)


for t in time:
	h=hd+vy*0.0001
	vy=vyd+(-9.8-vy)*0.0001
	vyd=vy
	hd=h
	if(h<0):
		break
	he.append(h)
	x.append(vx*t)
graph.plot(x,he,label="with resistance")
graph.plot(x1,y1,label="without resistance")
graph.legend()
graph.show()