from sys import argv
import re

a = open(argv[1]).read().split('\n\n')

keys=['byr','iyr','eyr','hgt','hcl','ecl','pid']
eyes=['amb','blu','brn','gry','grn','hzl','oth']

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
			#byr
			if(j[0] == keys[0] and int(j[1])>=1920 and int(j[1])<=2002):
				keys_valid+=1
			#iyr
			if(j[0] == keys[1] and int(j[1])>=2010 and int(j[1])<=2020):
				keys_valid+=1
			#eyr
			if(j[0] == keys[2] and int(j[1])>=2020 and int(j[1])<=2030):
				keys_valid+=1
			#hgt
			if(j[0] == keys[3]):
				match = re.search(r'^((1[5-8][0-9]|19[0-3])cm$)$|^(([5-6][0-9]|7[0-6])in$)$',j[1])
				if(match):
					keys_valid+=1		
			#hcl
			if(j[0] == keys[4]):
				match = re.search(r'^#[a-f0-9]{6}$',j[1])
				if(match):
					keys_valid+=1		
			#ecl
			if(j[0] == keys[5] and j[1] in eyes):
				keys_valid+=1			
			#pid
			if(j[0] == keys[6]):
				match = re.search(r'^[\d]{9}$',j[1])
				if(match):
					keys_valid+=1

	
	if(keys_valid>=7):
		valid+=1
		
print(valid)