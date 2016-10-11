
def detect_anagrams(s, vals):
    ans = []
    for i in list(filter(lambda x: len(x) == len(s), vals)):
        if ''.join(sorted(i.lower())) == ''.join(sorted(s.lower())) and i.lower() != s.lower():
            ans.append(i)
    return ans
