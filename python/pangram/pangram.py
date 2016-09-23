
import string

def is_pangram(s):

    # list of all ascii in lower.
    # convert input into lowercase too.
    s = s.lower()
    base = list(string.ascii_lowercase)

    for i in s:
        if i in base:
            base.pop(base.index(i))

    if len(base) is not 0:
        return False
    else:
        return True
