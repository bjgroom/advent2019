#! /usr/bin/python3
import re
total = 0

for n in range(172930, 683082):
	s = str(n)
	if s[0] <= s[1] <= s[2] <= s[3] <= s[4] <= s[5]:
		if (s[0] == s[1] != s[2]):
			total += 1
			continue
		elif (s[0] != s[1] == s[2] != s[3]):
			total += 1
			continue
		elif (s[1] != s[2] == s[3] != s[4]):
			total += 1
			continue
		elif (s[2] != s[3] == s[4] != s[5]):
			total += 1
			continue
		elif (s[3] != s[4] == s[5]):
			total += 1
print(total)

