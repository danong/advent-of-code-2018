from collections import deque


if __name__ == '__main__':
    with open('input/day09.txt', 'r') as f:
        inp = f.read()
        players = int(inp.split(' ')[0])
        points = int(inp.split(' ')[-2])
        points *= 100
    import time

    start = time.time()
    scores = [0] * players
    circle = deque([0])
    for i in range(1, points + 1):
        if i % 23:
            circle.append(circle.popleft())
            circle.append(i)
        else:
            scores[i % players] += i
            for _ in range(7):
                circle.appendleft(circle.pop())
            scores[i % players] += circle.pop()
            circle.append(circle.popleft())
    print(time.time() - start)

    print(max(scores))
