

def to_rna(val):
    ans = ''
    d = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }
    for i in val:
        ans += d[i]
    return ans
