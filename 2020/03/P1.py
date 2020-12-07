from sys import argv

a = open(argv[1]).read().splitlines()
a = a[1:]

mod = len(a[0])

pace = 4
trees = 0

for i in a:

	if(i[pace-1]=="#"):
		trees+=1
	pace+=3
	pace=pace%mod

print(trees)
