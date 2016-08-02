import random

def bubbleSort(lis):
	counter = 0
	maxRange = len(lis)-1
	for i in range(maxRange):
		if lis[i] > lis[i+1]:
			temp = lis[i+1]
			lis[i+1] = lis[i]
			lis[i] = temp
			counter += 1
	while counter>0:
		maxRange -= 1
		counter = 0
		for i in range(maxRange):
			if lis[i] > lis[i+1]:
				temp = lis[i+1]
				lis[i+1] = lis[i]
				lis[i] = temp
				counter += 1
	return lis


sample = []
for i in range(100):
	sample.append(random.randint(0,10000))
bubbleSort(sample)