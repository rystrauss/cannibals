"""Contains a class representing the board for the sliding tile puzzle.

Author: Ryan Strauss
"""

import math
import re
from copy import copy


class Board:
    """A board of a sliding tile puzzle.

    This class constitutes a state of the sliding tile puzzle search problem."""

    def __init__(self, tile_list):
        self.board_size = int(math.sqrt(len(tile_list)))
        self.tile_list = list(tile_list)
        self.blank_pos = self._convert_index(tile_list.index('0'))

    def __eq__(self, other):
        return isinstance(other, Board) and self.tile_list == other.tile_list

    def __hash__(self):
        return tuple(self.tile_list).__hash__()

    def __str__(self):
        s = ''.join(self.tile_list).replace('0', '_')
        lines = re.findall('.' * self.board_size, s)
        return '\n'.join(lines)

    def _convert_index(self, index):
        if isinstance(index, int):
            row = index // self.board_size
            col = index % self.board_size
            return row, col
        else:
            row, col = index
            return row * self.board_size + col

    def move(self, action):
        """Returns the board that results from taking a given action in this board.

        Args:
            action: The action to be taken. Either 'U', 'D', 'L', or 'R'.

        Returns:
            A board that reflects the transition from the given action.
        """
        if action == 'U':
            swap_pos = self.blank_pos[0] - 1, self.blank_pos[1]
        elif action == 'D':
            swap_pos = self.blank_pos[0] + 1, self.blank_pos[1]
        elif action == 'L':
            swap_pos = self.blank_pos[0], self.blank_pos[1] - 1
        elif action == 'R':
            swap_pos = self.blank_pos[0], self.blank_pos[1] + 1
        else:
            raise ValueError(f'{action} is not a valid action')

        new_tile_list = copy(self.tile_list)
        temp = new_tile_list[self._convert_index(swap_pos)]
        new_tile_list[self._convert_index(swap_pos)] = '0'
        new_tile_list[self._convert_index(self.blank_pos)] = temp
        return Board(new_tile_list)
