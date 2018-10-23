def printPairs(arr, size, sum):
	s = set()

	# ok = True

	for i in range(0, size):
		# ok = True
		temp = sum - arr[i]
		if temp in s:
			if arr[i]<temp:
				print(arr[i], temp)
				return
			elif arr[i]>=temp:
				print(temp, arr[i])
				return
			# else:
				# ok=False
				# break
		# else:
			# ok = False
		s.add(arr[i])

	# if ok==False:
		# print("!OK")
	print("!OK")

# a = [-1,1,9,8]
# a = [4,1,1,8]
# a=[1,1,4,8]
# printPairs(a,len(a), 8)

# def has2(arr, size, sum):
# 	arr.sort()
# 	l=0
# 	r=size-1

# 	while l<r:
# 		if (arr[l]+arr[r])==sum:
# 			return 1
# 		elif (arr[l]+arr[l])<sum:
# 			l+=1
# 		else:
# 			r-=1
# 	return 0


t = int(input())
for i in range(t):
	s, e = input().split()
	s = int(s)
	e = int(e)
	ea = []
	if e!=0:
		ea = [int(n) for n in input().split()]
	else:
		blank = input()
	printPairs(ea, e, s)