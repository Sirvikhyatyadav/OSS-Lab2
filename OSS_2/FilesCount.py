with open('Intro.txt','r') as W:
	
	no_of_lines=0
	no_of_words=0
	no_of_characters=0
	for line in W:
		line=line.strip("\n")
		words=line.split()
		no_of_words=len(words)
		no_of_lines+=1
		no_of_characters=len(line)
	print("Words:",no_of_words,"Characters:",no_of_characters,"Lines:",no_of_lines)
