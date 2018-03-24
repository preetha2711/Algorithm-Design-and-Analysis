# -*- coding: utf-8 -*-

a = [2,3,5,6]
k = 9
n = len(a)



def rec(i,k):
    if i ==0 and k == 0 :
        return 'true'
    elif i ==0:
        return 'false'

    x = p(i-1,k)
    if (x =='false'):
        x = p[i-1][k-a[i-1]]
    return x
