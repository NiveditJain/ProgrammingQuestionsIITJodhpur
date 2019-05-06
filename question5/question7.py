
#Name: Nivedit Jain
#Roll Number: B18CSE039

import matplotlib.pyplot as graph
import numpy as array
import math
day=array.arange(1,365,1)
#rajasthan at tropic cancer
latitude_factor=math.tan(math.radians(23.5))
length_of_day=[]
length_of_night=[]
twelve=[]
for d in day:
	delta=23.45*math.sin(math.radians((360*(284+d))/365))
	alpha=math.acos(-math.tan(math.radians(delta))*latitude_factor)
	x=(24*alpha)/math.pi
	length_of_day.append(x)
	length_of_night.append(24-x)
	twelve.append(12)
graph.title("length of day VS nth day")
graph.plot(day,length_of_day,label='light time')
graph.plot(twelve)
graph.plot(day,length_of_night,label='night time')
graph.legend()
graph.show()