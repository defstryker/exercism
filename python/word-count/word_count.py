import string, re
def word_count(s):
    mwa = string.punctuation[:26] + string.punctuation[27:]
    s = s.strip().lower().replace('\\n', ' ').replace('\n', ' ')\
        .replace('\r', '').replace('_', ' ').replace(',', ' ')\
        .replace('\t', ' ').replace('🖖', ' ')
    s = ''.join([c for c in list(s) if c not in mwa])
    l = s.split(' ')
    d = dict()
    uniq = set(l)
    for i in uniq:
        if i != '':
            d[i] = l.count(i)
    return d
