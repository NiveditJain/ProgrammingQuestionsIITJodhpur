import matplotlib.pyplot as graph
import numpy as numg
time=numg.arange(0,0.1,0.0001)
frequency=100
period=1/frequency
period_half=period/2
check=0
input_signal=[]
for x in time:
	if(check<period_half):
		input_signal.append(10)
	else:
		input_signal.append(-10)
	check=check+0.0001
	if(check>period):
		check=0
graph.plot(time,input_signal)
graph.show()		