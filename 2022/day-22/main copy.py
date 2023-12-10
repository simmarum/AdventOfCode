import sys
import copy
import re
from collections import defaultdict as dd
read = sys.stdin.read
f = open("input.txt")

inp, seq = [z.split('\n') for z in f.read().split('\n\n')]

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]

seq = seq[0]

x, y, d = 0, 0, 0
z = 0

n = len(inp)
m = max([len(inp[i]) for i in range(n)])

for i in range(n):
    while len(inp[i]) < m:
        inp[i] += ' '

k = len(seq)

while inp[x][y] == ' ':
    y += 1

while z < k:
    num = seq[z]
    while z + 1 < k and '0' <= seq[z + 1] <= '9':
        z += 1
        num += seq[z]
    z += 1

    num = int(num)
    mv = 0
    while mv < num:
        dx, dy = DX[d], DY[d]
        X = (x + dx) % n
        Y = (y + dy) % m
        if inp[X][Y] == '.':
            x = X
            y = Y
            mv += 1
        elif inp[X][Y] == ' ':
            x = X
            y = Y
        else:
            break

    while inp[x][y] == ' ':
        x = (x - dx) % n
        y = (y - dy) % m

    if z < k:
        assert seq[z] in ['L', 'R']
        if seq[z] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        z += 1

print((x + 1) * 1000 + (y + 1) * 4 + d)
