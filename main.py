from time import perf_counter as pf

now = pf()

a = 1000_000
f = list(range(a))
t = [2,]

for i in range(3, a, 2):
    if f[i] == 0: continue
    for j in range(2 * i, a, i): f[j] = 0
    t.append(i)

print(pf() - now)
# s = set(t)

from itertools import combinations as c

slr = lambda i, k: c(range(1, i), k)

def makemask(idxs):
    return sum(map(lambda i: 10 ** i, idxs))

def strip(p, idxs):
    m = 1
    r = 0
    i = 0
    while p > 0:
        r += (p % 10) * (i not in idxs) * m
        p //= 10
        m *= 10
        i += 1
    return r

for p in t:
    l = len(str(p))
    for i in range(1, l):
        for idxs in slr(l, i):
            m = makemask(idxs)
            t = strip(p, idxs)
            k = (((f[t] != 0) and (len(str(t)) == l))) + sum((f[(t + i * m)] != 0) for i in range(1, 10))
            if k == 8:
                print(pf() - now)
                for o in range(10):
                    print(t + o * m, f[t + o * m] != 0)
                raise Exception(p)

