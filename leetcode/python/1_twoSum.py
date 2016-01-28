
num = [3,2,4]
target = 6

def twoSum(num, target):
	processed ={}
	for i in range(0,len(num)):
		if target-num[i] in processed:
			return (processed.get(target-num[i])+1,i+1)
		else:
			processed[num[i]]=i

	print processed

print twoSum(num,target)