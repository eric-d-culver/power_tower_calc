#!/usr/bin/python3

from math import log


def powers_mod_cycle(b, m):
    if b >= m:
        return powers_mod_cycle(b % m, m)
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

def is_one(pt):
    if len(pt) == 0: # no more powers is the same as a power of 1
        return True
    if pt[-1] == 1: # chop off 1's at top of tower
        return is_one(pt[:-1])
    if pt[-1] == 0: # power of 0 makes power below become 1
        return is_one(pt[:-2]+[1])
    return False

def exceeds(pt, m):
    val = m
    for i in range(len(pt)):
        if pt[i] > val:
            return True
        if pt[i] == 0:
            return False
        val = log(val, pt[i])
    return False

def calc(pt):
    acc = 1
    for i in range(len(pt)):
        acc = pt[-(i+1)]**acc
    return acc

def mod_power_tower(pt, m):
    if m == 1:
        return 0
    b = pt[0]
    p = pt[1:]
    if is_one(p):
        return b % m
    c, mods = powers_mod_cycle(b, m)
    if exceeds(p, m):
        diff = mod_power_tower(p, c)
        if diff < (m % c):
            return mods[m - (m % c) + c + diff]
        return mods[m - (m % c) + diff]
    return mods[calc(p)]
