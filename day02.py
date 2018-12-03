from collections import Counter

with open('input/day02.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]

# part 1
twos = 0
threes = 0
for id in inp:
    count = Counter(id)
    if 2 in count.values():
        twos += 1
    if 3 in count.values():
        threes += 1
print(twos * threes)

# part 2
for idx1 in range(len(inp)):
    for idx2 in range(idx1, len(inp)):
        id1, id2 = inp[idx1], inp[idx2]
        dif = 0
        for idxc in range(len(id1)):
            if id1[idxc] != id2[idxc]:
                dif += 1
        if dif == 1:
            print(id1, id2)
            exit()
