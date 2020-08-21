#!/usr/bin/python3


def power_mod(b, m):
    if b >= m:
        return powers_mod(b % m, m)
    if m == 1:
        return (1, [0])
    res = [1]
    for i in range(m):
        res.append((res[i] * b) % m)
    val = res[-1]
    j = m
    while True:
        res.append((res[j] * b) % m)
        j += 1
        if (val == res[-1]):
            break
    return (j - m, res)
