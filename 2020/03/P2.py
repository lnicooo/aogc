from sys import argv

a = open(argv[1]).read().splitlines()

mod = len(a[0])
down_size = len(a)

def slope(right, down):
	first = down%2
	pace = right + first
	trees = 0
	for i in range(first,down_size, down):
		b=a[i]
		if(b[pace-1]=="#"):
			trees+=1
		pace+=right
		pace=pace%mod

	return trees

count = slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2)

print(count)

