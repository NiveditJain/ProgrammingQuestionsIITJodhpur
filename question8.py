import matplotlib.pyplot as graph
import numpy as numg
time=numg.arange(0,1,0.001)
frequency=int(input("Enter the frequency of function generator:"))
amplitude=int(input("Enter the frequency of amplitude generator:"))
period=1/frequency
period_half=period/2
check=0
input_signal=[]
for x in time:
	if(check<period_half):
		input_signal.append(amplitude)
	else:
		input_signal.append(-amplitude)
	check=check+0.0001
	if(check>period):
		check=0
graph.plot(input_signal)
graph.show()		