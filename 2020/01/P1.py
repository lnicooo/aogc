from sys import argv

ab = open(argv[1]).read().splitlines()
ab = [int(x) for x in ab]

for a in ab:
    for b in ab:
        if(a+b == 2020):
            print(a*b)
            