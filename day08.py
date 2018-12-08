with open('input/day08.txt', 'r') as f:
    inp = f.read()
    inp = [int(x) for x in inp.split(' ')]


def visit(start):
    meta_sum = 0
    num_nodes, num_meta = inp[start: start + 2]
    next_start = start + 2
    for child_node in range(num_nodes):
        t_sum, next_start = visit(next_start)
        meta_sum += t_sum
    meta_sum += sum(inp[next_start:next_start + num_meta])
    return meta_sum, next_start + num_meta


def visit2(start):
    node_sum = 0
    num_nodes, num_meta = inp[start: start + 2]
    next_start = start + 2
    if num_nodes:
        node_vals = []
        for child_node in range(num_nodes):
            t_sum, next_start = visit2(next_start)
            node_vals.append(t_sum)
        for idx in inp[next_start:next_start + num_meta]:
            if idx - 1 < len(node_vals):
                node_sum += node_vals[idx - 1]
    else:
        node_sum += sum(inp[next_start:next_start + num_meta])
    return node_sum, next_start + num_meta


def main():
    print(visit(0))
    print(visit2(0))


main()
