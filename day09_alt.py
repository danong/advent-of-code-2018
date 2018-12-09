class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.first = Node(0)
        self.first.next = self.first
        self.first.prev = self.first
        self.cur = self.first

    def insert(self, val):
        if val % 23 == 0:
            score = val
            rem = self.cur.prev.prev.prev.prev.prev.prev.prev
            self.cur = self.cur.prev.prev.prev.prev.prev.prev
            score += rem.val
            self.remove(rem)
            return score

        else:
            new_node = Node(val)
            prev = self.cur.next
            nex = prev.next
            prev.next = new_node
            new_node.prev = prev
            new_node.next = nex
            nex.prev = new_node
            self.cur = new_node
            return 0

    def remove(self, node):
        prev, nex = node.prev, node.next
        prev.next, nex.prev = nex, prev
        del node


if __name__ == '__main__':
    with open('input/day09.txt', 'r') as f:
        inp = f.read()
        players = int(inp.split(' ')[0])
        points = int(inp.split(' ')[-2])
        points *= 100
        # inp = [l.strip() for l in f.readlines()]
    scores = [0] * players
    lis = CircularDoublyLinkedList()
    for i in range(1, points + 1):
        score = lis.insert(i)
        scores[i % players] += score
    print(max(scores))
