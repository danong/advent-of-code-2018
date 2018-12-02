inp = """ivyhczwokexltwhsfamqprbnuy
ivjhcjdokexltwwsfamqpabnuy
ivjhczdokebltwgsfydqprbnuy
ivjhczdoknxltwgssamqsrbnuy
ivjhczdokexltwgswadqprbruy
ivjhcjdokexltwfsfamqpabnuy
uvjhczrozexltwgsfamqprbnuy
ivjhjzdxkexltwgsffpqprbnuy"""

from collections import Counter

# part 1
twos = 0
threes = 0
for id in inp.splitlines():
  count = Counter(id)
  if 2 in count.values():
    twos += 1
  if 3 in count.values():
    threes += 1
print(twos * threes)

# part 2
lines = inp.splitlines()
for idx1 in range(len(lines)):
    for idx2 in range(idx1, len(lines)):
        id1, id2 = lines[idx1], lines[idx2]
        dif = 0
        for idxc in range(len(id1)):
            if id1[idxc] != id2[idxc]:
                dif += 1
        if dif == 1:
            print(id1, id2)
            exit()