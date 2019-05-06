import matplotlib.pyplot as graph
import numpy as array
import math
g=9.8
w=2*math.pi/(24*3600)
r=6371000
p=w*w*r
prem=p*(p - 2*g)
o=array.arange(0,90,1)
a=[]
for O in o:
	a.append(math.sqrt(g*g+(math.cos(math.radians(O))*math.cos(math.radians(O)))*prem))
graph.xlabel("degree")
graph.ylabel("g")
graph.plot(o,a)
graph.show()