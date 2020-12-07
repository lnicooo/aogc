from sys import argv
a = open(argv[1]).readlines()
d=0

for i in a:
	i=i.strip()
	i=i.split(' ')
	flag = False
	letter = i[1][0]
	string = i[2]

	c = i[0].split('-')
	
	if(letter == string[int(c[0])-1]):
		flag = not flag
		
	if(letter == string[int(c[1])-1]):
		flag = not flag
	
	if(flag):
		d+=1

print(d)
