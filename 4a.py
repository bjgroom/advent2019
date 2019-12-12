#! /usr/bin/python3

total = 0

for n in range(172930, 683082):
	s = str(n)	
	if s[0] <= s[1] <= s[2] <= s[3] <= s[4] <= s[5]:
		if s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4] or s[4] == s[5]:
			total += 1

print(total)

