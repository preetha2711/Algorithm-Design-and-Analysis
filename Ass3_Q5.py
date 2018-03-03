import math
num = float(raw_input("pls enter"))
ln = math.log(num,2)
ln = math.ceil(ln)
ln = int(ln)
t = [[] for i in range(ln)]
t[0].append('0')
t[0].append('1')
for i in range (1, ln):
    for j in t[i-1]:
        term =  '0'+  j
        t[i].append(term)
    for j in t[i-1][::-1]:
        term =  '1'+  j
        t[i].append(term)

ans_array = []
#num is even
temp = 2**ln - num #to be rem
print int((len(t[i])/2) + int(temp/2))
if temp %2 ==0:
    ans_array = t[i][0:(int(len(t[i])/2) - int(temp/2))]+t[i][int((len(t[i])/2) + int(temp/2)):]
elif temp%2 !=0:
    ans_array = t[i][0:(int(len(t[i])/2) - int(temp/2))]+t[i][int((len(t[i])/2) + int(temp/2) +1 ):]
#for i in t[0: (len(t)/2 - temp/2)]:
#    ans_array.append(t[i])
#print ans_array
print ans_array
