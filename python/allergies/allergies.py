
p = [2 ** i for i in range(8)]
p = p[::-1]
print p

allergy = {
    1: 'eggs',
    2: 'peanuts',
    4: 'shellfish',
    8: 'strawberries',
    16: 'tomatoes',
    32: 'chocolate',
    64: 'pollen',
    128: 'cats'
}
l = []

def Allergies(val):
    for i in p:
        if val % i is not 0:
            l.append(i)
            val = val % i
        #elif val % i is 0 and val in p:
        #    l.append(i)

Allergies(34)

print l

ans = []
for i in l:
    ans.append(allergy[i])

print ans
