
"""
ID: smaylni1
LANG: PYTHON3
PROB: beads
"""

def counter_left(i):
    l = 1
    current = beads[i]
    while (beads[i - 1] == beads[i]) or (beads[i - 1] == 'w') or (beads[i] == 'w'):
        fl = beads[i]
        if (beads[i - 1] == beads[i]) or (beads[i - 1] == 'w') or (beads[i] == 'w'):
            l += 1
        i -= 1
        if (beads[i] == 'w') and (beads[i - 1] != current):
            if (beads[i - 1] == 'w'):
                continue
            else:
                break
    return l

def counter_right(i):
    r = 1
    current = beads[i]
    while (beads[(i + 1) % len(beads)] == beads[i % len(beads)]) or (beads[(i + 1) % len(beads)] == 'w') or (beads[i % len(beads)] == 'w'):
        fl = beads[i % len(beads)]
        if (beads[(i + 1) % len(beads)] == beads[i % len(beads)]) or (beads[(i + 1) % len(beads)] == 'w') or (beads[i % len(beads)] == 'w'):
            r += 1
        i += 1
        if (beads[i % len(beads)] == 'w') and (beads[(i + 1) % len(beads)] != current):
            if (beads[(i + 1) % len(beads)] == 'w'):
                continue
            else:
                break
    return r

f = open('beads.in', 'r')
beads = f.readlines()
f.close()

beads = beads[1]
max = -1

beads = beads.replace('\n', '')
beads += beads

if ('r' in beads) and ('b' in beads):
    for i in range(1, len(beads) - 1, 1):
        l = counter_left(i)
        r = counter_right(i + 1)
        if (l + r > max):
            max = l + r
else:
    max = len(beads) // 2

if max > len(beads) // 2:
    max = len(beads) // 2

f = open('beads.out', 'w')
f.write(str(max) + '\n')
f.close()