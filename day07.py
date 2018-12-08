from collections import defaultdict

with open('input/day07.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]

adj = defaultdict(set)

for requirement in inp:
    split = requirement.split(' ')
    n1 = split[1]
    n2 = split[7]
    adj[n1].add(n2)

visited = set()
order = []


def visit(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in sorted(adj[node], reverse=True):
        visit(neighbor)
    order.append(node)


for node in sorted(list(adj), reverse=True):
    visit(node)

print(''.join(reversed(order)))

# part 2
safe = {n: False for n in adj}
todo = set(adj)
done = set()


def update_safe(safe, adj):
    vals = {item for sublist in adj.values() for item in sublist}
    for n in safe:
        if n not in vals:
            safe[n] = True


def update_adj(n, adj):
    adj.pop(n)


update_safe(safe, adj)


def cost(node):
    return 60 + ord(node) - ord('A') + 1


workers = 5
time = 0
in_progress = {}
while todo:
    while workers > 0:
        safe_n = {n for n in safe if safe[n]}.intersection(todo)
        if not len(safe_n):
            break
        workers -= 1
        n = sorted(safe_n)[0]
        todo.remove(n)
        in_progress[n] = cost(n)
    step = min(in_progress.values())
    time += step
    for n in list(in_progress):
        in_progress[n] -= step
        if in_progress[n] == 0:
            in_progress.pop(n)
            workers += 1
            update_adj(n, adj)
            update_safe(safe, adj)
            done.add(n)
print(time)
