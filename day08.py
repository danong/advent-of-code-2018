with open('input/day08.txt', 'r') as f:
    inp = f.read()
    inp = [int(x) for x in inp.split(' ')]


def visit(start):
    meta_sum = 0
    num_nodes = inp[start]
    num_meta = inp[start + 1]
    next_start = start + 2
    for child_node in range(num_nodes):
        t_sum, next_start = visit(next_start)
        meta_sum += t_sum
    meta_sum += sum(inp[next_start:next_start+num_meta])
    return meta_sum, next_start+num_meta

def visit2(start):
    meta_sum = 0
    num_nodes = inp[start]
    num_meta = inp[start + 1]
    next_start = start + 2
    if num_nodes:
        meta_sums = []
        for child_node in range(num_nodes):
            t_sum, next_start = visit2(next_start)
            meta_sums.append(t_sum)
        for idx in inp[next_start:next_start+num_meta]:
            idx = idx - 1
            if idx < len(meta_sums):
                meta_sum += meta_sums[idx]
    else:
        meta_sum += sum(inp[next_start:next_start+num_meta])
    return meta_sum, next_start+num_meta


def main():
    print(visit2(0))


main()
