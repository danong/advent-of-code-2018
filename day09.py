with open('input/day09.txt', 'r') as f:
    inp = f.read()
    players = int(inp.split(' ')[0])
    points = int(inp.split(' ')[-2])
    # inp = [l.strip() for l in f.readlines()]


def main(players, points):
    scores = [0] * players
    l = [0]
    cur = 0
    for i in range(1, points+1):
        # if i == points:
        #     print('hi')
        #     i *= 100
        if i % 23 == 0:
            scores[i % players] += i
            rem_idx = cur - 7
            rem_val = l[rem_idx]
            cur = l.index(l[rem_idx])
            scores[i % players] += rem_val
            l.remove(rem_val)

        else:
            next_idx = cur + 2
            if next_idx == len(l):
                l.append(i)
                cur = next_idx

            elif next_idx > len(l):
                l.insert(1, i)
                cur = 1
            else:
                l.insert(next_idx, i)
                cur = next_idx

    return max(scores)


if __name__ == '__main__':
    # print(main(13, 7999))
    print(main(players, points * 100))
