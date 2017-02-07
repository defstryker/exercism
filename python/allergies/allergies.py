
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
