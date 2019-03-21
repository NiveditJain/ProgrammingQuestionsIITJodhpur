import math
#assumed any part as a polygon 
coordinates=[
			[0,0],
			[0,1],
			[1,1],
			[1,0]
			]
#add the coordinates as per required
#in format x,y
centroid=[0,0]
area=0
p1=coordinates[0]
p2=coordinates[1]
def area_triangle(p1,p2,p3):
	l1=math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))
	l2=math.sqrt((p2[0]-p3[0])*(p2[0]-p3[0])+(p2[1]-p3[1])*(p2[1]-p3[1]))
	l3=math.sqrt((p1[0]-p3[0])*(p1[0]-p3[0])+(p1[1]-p3[1])*(p1[1]-p3[1]))
	s=(l1+l2+l3)/2
	return(math.sqrt(s*(s-l1)*(s-l2)*(s-l3)))
def centroid_tringle(p1,p2,p3):
	return([(p1[0]+p2[0]+p3[0])/3,(p1[1]+p2[1]+p3[1])/3])

for x in range (2,len(coordinates)):
	p3=coordinates[x]
	areat=area_triangle(p1,p2,p3)
	area=area+areat
	centroidt=centroid_tringle(p1,p2,p3)
	centroid[0]=centroid[0]+areat*centroidt[0]
	centroid[1]=centroid[1]+areat*centroidt[1]
	p2=p3
centroid[0]=centroid[0]/area
centroid[1]=centroid[1]/area
print(centroid)