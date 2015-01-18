n = 20

def waysRunningUpStairs(n):
	if n == 0:
		return 1
	elif n == 1:
		return waysRunningUpStairs(n-1)
	elif n == 2:
		return waysRunningUpStairs(n-1)+waysRunningUpStairs(n-2)
	else:
		return waysRunningUpStairs(n-1)+waysRunningUpStairs(n-2)+waysRunningUpStairs(n-3)

def waysRunningUpStairsDP(n, array):
	if n < 0 :
		return 0
	elif n == 0:
		return 1
	else:
		if array[n] != 0:
			return array[n]
		else:
			array[n] = waysRunningUpStairsDP(n-1,array)+waysRunningUpStairsDP(n-2,array)+waysRunningUpStairsDP(n-3,array)
			return array[n]
a = [0] * (n+1)

print waysRunningUpStairsDP(n,a)
