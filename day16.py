def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]
    return reg


def addi(reg, a, b, c):
    reg[c] = reg[a] + b
    return reg


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]
    return reg


def muli(reg, a, b, c):
    reg[c] = reg[a] * b
    return reg


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]
    return reg


def bani(reg, a, b, c):
    reg[c] = reg[a] & b
    return reg


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]
    return reg


def bori(reg, a, b, c):
    reg[c] = reg[a] | b
    return reg


def setr(reg, a, b, c):
    reg[c] = reg[a]
    return reg


def seti(reg, a, b, c):
    reg[c] = a
    return reg


def gtir(reg, a, b, c):
    reg[c] = int(a > reg[b])
    return reg


def gtri(reg, a, b, c):
    reg[c] = int(reg[a] > b)
    return reg


def gtrr(reg, a, b, c):
    reg[c] = int(reg[a] > reg[b])
    return reg


def eqir(reg, a, b, c):
    reg[c] = int(a == reg[b])
    return reg


def eqri(reg, a, b, c):
    reg[c] = int(reg[a] == b)
    return reg


def eqrr(reg, a, b, c):
    reg[c] = int(reg[a] == reg[b])
    return reg


def check(before, after, a, b, c, potential_ops):
    matches = set()
    for op in potential_ops:
        ans = op(list(before), a, b, c)
        if ans == after:
            matches.add(op)
    return matches


def main():
    # parse input
    ops_mapping = {i: {addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr}
                   for i in range(16)}
    instructions = []
    with open('input/day16p1.txt', 'r') as f_in:
        lines = [f.strip() for f in f_in.readlines()]
    for i in range(0, len(lines), 4):
        instructions.append(lines[i: i + 3])
    for instruction in instructions:
        before = eval(instruction[0].split(': ')[1])
        ops, a, b, c = [int(x) for x in instruction[1].split(' ')]
        after = eval(instruction[2].split(': ')[1])
        potential_ops = ops_mapping[ops]
        matches = check(before, after, a, b, c, potential_ops)
        ops_mapping[ops] = matches
        if len(ops_mapping[ops]) == 1:
            for k, v in ops_mapping.items():
                if k == ops:
                    continue
                v.discard(next(iter(ops_mapping[ops])))

    ops_mapping = {
        op_code: next(iter(op)) for op_code, op in ops_mapping.items()
    }

    register = [0, 0, 0, 0]
    with open('input/day16p2.txt', 'r') as f_in:
        lines = [f.strip() for f in f_in.readlines()]
    for instruction in lines:
        ops, a, b, c = [int(x) for x in instruction.split(' ')]
        ops_mapping[ops](register, a, b, c)
    print(register[0])


if __name__ == '__main__':
    main()
