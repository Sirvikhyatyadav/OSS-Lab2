def Duplicate(l):
	l1=[]
	for i in l:
		if i not in l1:
			l1.append(i)
		else:
			print(i,end=' ')


l = [1,2,3,4,5,5,7,8,8,2,1]
Duplicate(l)