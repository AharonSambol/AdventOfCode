from functools import reduce

def add(n1, n2):
    ln = max(len(n1), len(n2)) + 1
    res, carry = [], 0
    for d1, d2 in zip(*map(lambda x: x[::-1].ljust(ln, '0'), (n1, n2))):
        d1, d2 = map(lambda x: '=-012'.index(x) - 2, (d1, d2))
        carry, add = divmod(d1 + d2 + carry, 5)
        carry += add // abs(add) if abs(add) > 2 else 0
        res.append('=-012'[(add + 2) % 5])
    return ''.join(res[::-1]).lstrip('0')


with open("../Inputs/InputDay25.txt") as file:
    print(reduce(add, file.read().split('\n')))