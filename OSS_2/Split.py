def Group(l,si):
	l1=[]
	ans=[]
	for i in range(0,len(l)):
		k=i%si

		if k==0:
			if len(l1)==0:
				
				l1.append(l[i])
			else:
				ans.append(l1)
				l1=[]
				l1.append(l[i])
		else:
			l1.append(l[i])

	if len(l1)!=0:
		ans.append(l1)
	return ans

l = [1,2,3,4,5,5,7,8,8,2,1]
final = Group(l,4)

for i in final:
	print(i,end=' ')

