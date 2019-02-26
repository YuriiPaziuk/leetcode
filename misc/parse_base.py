result = []

with open('base.lst') as file:
	for line in file:
		if line[0] != ' ':
			result.append(line.split()[0])

print(len(result))
print(result[:10])

word = 'ковзати'
print(word in result)