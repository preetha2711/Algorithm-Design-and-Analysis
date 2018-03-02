import math

def skyline(new,height_index):
	#height_index.update({new[0]:0})
	for i in range(new[0]+1,new[2]+1):
		if new[1]>height_index[i]:
			height_index.update({i:new[1]})
	return height_index



n=input()
a=[None]*n
for i in range (n):
    a[i]=map(int,raw_input().split())#a contains list of buildings
maxh=-1
for i in a:
    maxh=max(maxh,i[2])#finding the x coordinate of the building furthest away from origin



height_index={0:0}
for i in range (maxh+1):#creating a list where index corresponds to x axis and value corresponds to height at coordinate (y axis)
	height_index.update({i:0})#making the height of each building 0 initially



for i in range (n):
	height_index=skyline(a[i],height_index)
         

final=[]
for i in range(1,len(height_index)-1):
	if(height_index[i]!=height_index[i+1]):
		final.append(i)
		final.append(height_index[i+1])
final.append(len(height_index)-1)
#del final[0]
print final