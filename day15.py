import itertools
from dataclasses import dataclass
from typing import Tuple

import numpy as np


@dataclass
class Agent:
    team: str
    location: Tuple[int, int]
    hp: int
    attack: int

    def __repr__(self):
        return 'Char("{}", {}, {}, {})'.format(self.team, self.location, self.hp, self.attack)

    def find_path(self):
        pass


class Game:
    wall = '#'
    free = '.'
    goblin = 'G'
    elf = 'E'

    def __init__(self, board):
        self.board = board
        self.turns = 0

        self.chars = {self.elf: [], self.goblin: []}
        for index, val in np.ndenumerate(board):
            if val == self.goblin or val == self.elf:
                self.chars[val].append(Agent(val, index, 200, 3))

    def play(self):
        while not self.won:
            self.turn()
            print(self.scores)
            self.turns += 1

    def turn(self):
        sorted_agents = sorted(itertools.chain.from_iterable(self.chars.values()), key=lambda a: a.location)
        for agent in sorted_agents:
            agent.move(self.board)

    @property
    def won(self) -> bool:
        return not all(self.chars.values())

    @property
    def scores(self):
        return self.team_score(self.elf), self.team_score(self.goblin)

    def team_score(self, team):
        return sum(agent.hp for agent in self.chars[team])


def main():
    with open('input/day15.txt', 'r') as f_in:
        board = [list(x.strip()) for x in f_in.readlines()]

    board = np.array(board, dtype=str)
    game = Game(board)
    game.play()


if __name__ == '__main__':
    main()
