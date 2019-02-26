result = set()

with open('base.lst', encoding='utf8') as file:
    for line in file:
        if line[0] != ' ':
            result.add(line.split()[0])

import itertools

anagrams = set()
word = 'фруктовий'
for i in range(3, len(word) + 1):
    for x in itertools.combinations(word, i):
    #for x in itertools.combinations_with_replacement(word, i):
        x = ''.join(x)
        for t in itertools.permutations(x):
            t = ''.join(t)
            if t in result:
                anagrams.add(t)
                #print(t)


from pprint import pprint


print(len(result))

pprint(sorted(anagrams))
