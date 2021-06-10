with open('Intro.txt','r') as W:
	k=W.readlines()
	k = [i.rstrip()[::-1] for i in k]
	print(k)