#fail not working

height = [0,1,0,2,1,0,1,3,2,1,2,1]

fill = 0
for i in range(max(height)) : #0,1,2
	fillLine = 0
	step = i+1
	print(step)
	for j in range(len(height)) :
		savepoint = -1
		print('pre savepoint :',savepoint)
		if height[j] >= step :
			width = j - savepoint -1
			print('width :', width)
			if width > 0 :
				fillLine += width
			savepoint = j
			print('changed savepoint :',savepoint)
	fill += fillLine

print(fill)
