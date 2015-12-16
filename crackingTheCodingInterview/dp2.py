import math

x = 10
y = 10

def path(x,y):
	if x == 0 and y == 0:
		return 1
	elif x == 0:
		return 1 + path(x,y-1)
	elif y == 0:
		return 1 + path(x-1,y)
	else:
		return 1 + path(x-1,y) + path(x,y-1)

print path(x,y)

def pathdp(x,y,array):
	if x == 0 and y == 0:
		return 1
	elif x == 0:
		if(array[x][y] != 0):
			return array[x][y]
		else:
			array[x][y] = 1 + pathdp(x,y-1,array)
			return array[x][y]
	elif y == 0:
		if(array[x][y] != 0):
			return array[x][y]
		else:
			array[x][y] = 1 + pathdp(x-1,y,array)
			return array[x][y]
	else:
		if(array[x][y] != 0):
			return array[x][y]
		else:
			array[x][y] = 1 + pathdp(x-1,y,array) + pathdp(x,y-1,array)
			return array[x][y]
array2 = [[0 for y in xrange(y+1)] for x in xrange(x+1)]
print pathdp(x,y,array2)


print math.factorial(x+y)/math.factorial(y)/math.factorial(x)