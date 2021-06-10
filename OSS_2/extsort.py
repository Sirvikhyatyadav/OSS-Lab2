def Extsort(l):
	l = sorted(l,key=lambda x:x.split('.')[1])
	print(l)

l = ['a.py','b.exe','c.jpg','d.cpp']
Extsort(l)