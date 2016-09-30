from _md5 import MD5Type as z

def is_flag(s):  
	varA = int(s[pow(ord(s[0]), 2) - 7226:])
	varB = list(filter(lambda q: q % 3 == 0, [varA, varA * 2, varA * 3, varA * 4, varA * 5]))
	if len(varB) != 5:
		print("First false")
		return False
	varC = s[1:-2]
	if (len([n for n in list(varC) if lambda y: i in varB])) != 8:
		print("Second false")		
		return False
	varD = [(ord(x) - 48) for x in list(s)]
	if s.count('U') != 3:
		print("Third false")
		return False
	if varC.index('_') != varC[::-1].index('_'):
		print("Forth false")
		return False
	if (s[varD[3]]) != 'W':
		print("Fifth false")
		return False
	return True

print(is_flag('UUU9__aaaW3'))
