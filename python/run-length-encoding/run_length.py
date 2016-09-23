from itertools import groupby
from re import sub

def encode(arg=''):
    fin =''
    l = [(len(list(g)), k) for k, g in groupby(arg)]
    for n,a in l:
        if n != 1:
            fin += '{}{}'.format(n,a)
        else:
            fin += a
    return fin

def decode(args=''):
    a = sub(r'(\d+)(\D)', lambda x: x.group(2) * int(x.group(1)), args)
    return a
