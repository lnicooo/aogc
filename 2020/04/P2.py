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
		keys_valid=0
		for j in i:
			j = j.split(':')
			if(j[0] == keys[0] and j[1]>=1920 and j[1]<=2002):
				keys_valid+=1
			if(j[0] == keys[1] and j[1]>=2010 and j[1]<=2020):
				keys_valid+=1
			if(j[0] == keys[2] and j[1]>=2020 and j[1]<=2030):
				keys_valid+=1
			if(j[0] == keys[3]):
				m=j[1][-2:]
				val=j[1][:-2]
				if(m=='cm' and val>=150 and val<=193):
					keys_valid+=1
				if(m=='in' and val>=59 and val<=76):
					keys_valid+=1
			if(j[0] == keys[4] and j[1]>=1920 and j[1]<=2002):
				keys_valid+=1
			if(j[0] == keys[5] and j[1]>=1920 and j[1]<=2002):
				keys_valid+=1
			if(j[0] == keys[6] and j[1]>=1920 and j[1]<=2002):
				keys_valid+=1
				

		
print(valid)