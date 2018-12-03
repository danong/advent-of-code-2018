with open('input/day01.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]

# part 1
val = ''.join(inp)
print(eval(val))

# part 2
start = 0
seen = {0}
while True:
    for num in inp:
        start += int(num)
        if start in seen:
            print(start)
            exit()
        else:
            seen.add(start)
