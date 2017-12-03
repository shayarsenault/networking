new_letters = []

msg = input(':')

for char in msg:
	new_letters.append(chr(ord(char) - 3))

print(':' + ''.join(new_letters))
