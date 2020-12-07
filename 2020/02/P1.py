from sys import argv
a = open(argv[1]).readlines()
d=0
for i in a:
	i=i.strip()
	i=i.split(' ')
	b = i[2].count(i[1][0])
	c = i[0].split('-')
	if(b>=int(c[0]) and b<=int(c[1])):
		print(i[2])
		d+=1
print(d)
