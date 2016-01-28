import math

def solution(n,array,count):
	if count == 1:
		for i in range(1,n+1):
			array.append(str(i))
		return array
	else:
		temp = []
		array = solution(n,array,count-1)
		for s in array:
			for i in range(1,n+1):
				temp.append(s+str(i))
		array = temp
		return array



def perm(n,k):
	arr = range(1,n+1)
	n = n-1
	res = ''
	while(n>0):
		fct = math.factorial(n)
		t = arr[(k-1)/fct]
		k = k%fct
		res += str(t)
		arr.remove(t)
		n -= 1
	res += str(arr[0])
	return res
print perm(3,6)