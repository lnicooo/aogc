from sys import argv

a = open(argv[1]).read().split('\n\n')

keys=['byr','iyr','eyr','hgt','hcl','ecl','pid']

a = [x.replace('\n',' ')  for x in a]

valid = 0

for i in a:
	keys_valid=0
	i=i.split(' ')
	for j in i:
		if(j.split(':')[0] in keys):
			keys_valid+=1
	if(keys_valid>=7):
		valid+=1
print(valid)