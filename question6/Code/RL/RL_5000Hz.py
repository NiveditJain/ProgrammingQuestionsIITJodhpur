import matplotlib.pyplot as graph
import numpy as numg
import math
time=numg.arange(0,0.001,0.000001)
frequency=5000
amplitude=5
period=1/frequency
period_half=period/2
check=0
input_signal=[]
output_signal=[]
R=100
L=0.001
time_contant_inverse=R/L
ex=0.000001*time_contant_inverse
y=[]
v_prev=0
for x in time:
	v_o=amplitude
	if(check<period_half):
		input_signal.append(amplitude)
	else:
		input_signal.append(-amplitude)
		v_o=-v_o
	v_prev=float(v_o+math.exp(-ex)*(v_prev-v_o))
	output_signal.append(v_prev)
	check=check+0.000001
	y.append(0)
	if(check>period):
		check=0
graph.title("RL Time Response 5000Hz")
graph.xlabel("time(microS)")
graph.ylabel("Voltage(V)")
graph.plot(y,label="X-Axix")
graph.plot(input_signal,label="Input Signal")
graph.plot(output_signal,label="Output Signal")
graph.legend()
graph.show()		