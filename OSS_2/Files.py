with open('Intro.txt','r') as W:
	#read
	print(W.read(),end='\n')
	
with open('Intro.txt','r') as W:
	#readline
	print(W.readline(),end='\n')

with open('Intro.txt','a') as W:
	#write
	W.write('I am in my 3rd year')
	# W.writeline('Hello')
	# print(W.read(),end='\n')




