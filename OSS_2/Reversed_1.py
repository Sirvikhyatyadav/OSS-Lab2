with open('Intro.txt','r') as W:
	k=W.readlines()
	t=reversed(k)
	for i in t:
		print(i.rstrip(),end='\n')