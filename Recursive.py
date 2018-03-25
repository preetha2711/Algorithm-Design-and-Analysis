# -*- coding: utf-8 -*-


def p(i, k):
	if (k == 1):
		return i
	if (k>i):
		return 0

	ans = p(i-1, k) + p(i-1, k-1)

	return ans

print p(1000,100)
