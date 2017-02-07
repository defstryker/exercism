
<<<<<<< HEAD
ar = {
    1:   "eggs",
    2:   "peanuts",
    4:   "shellfish",
    8:   "strawberries",
    16:  "tomatoes",
    32:  "chocolate",
    64:  "pollen",
    128: "cats"
}

class Allergies():
    def __init__(self, value):
        n = value

    def is_allergic_to(self):
        global ar
        l = []
        t = 128
        while t > 0:
            val = self.n % t
            if val > 0:
                print ("{} : {}".format(t, ar[t]))
                l.append(ar[t])
                self.n -= val
            elif val is 0:
                print("why is it wrong??")
            t //= 2

        print(l)

if __name__ == '__main__':
    Allergies(34)
=======
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
>>>>>>> 7b48798e8f8cda201fabd75337f5abd115860f90
