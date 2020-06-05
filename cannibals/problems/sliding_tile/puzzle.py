"""This module defines the sliding tile puzzle problem.

Author: Ryan Strauss
"""

from copy import copy

from cannibals.problems.base import AbstractProblem
from cannibals.problems.sliding_tile.board import Board


class SlidingTilePuzzle(AbstractProblem):
    """Implementation of the sliding tile puzzle.

    The sliding tile puzzle, or n-puzzle, consists of an n by n board with n^2 - 1 numbered tiles and a blank space.
    A tile adjacent to the blank space can slide into the space. The object is to reach a specified goal state.

    In this implementation, we think of an action as moving the blank tile either up, down, left, or right.

    The 8-puzzle has 9!/2=181, 440 reachable states and is easily solved. The 15-puzzle (on a 4×4 board) has around
    1.3 trillion states, and random instances can be solved optimally in a few milliseconds by the best search
    algorithms. The 24-puzzle (on a 5 × 5 board) has around 1025 states, and random instances take several hours to
    solve optimally.
    """

    VALID_ACTIONS = ['U', 'D', 'L', 'R']

    def __init__(self, initial_state, goal_state='123456780'):
        if isinstance(initial_state, str):
            initial_state = Board(initial_state)
        assert isinstance(initial_state, Board)
        if isinstance(goal_state, str):
            goal_state = Board(goal_state)
        assert isinstance(goal_state, Board)

        super().__init__(initial_state)
        self.goal_state = goal_state

    def get_actions(self, state):
        actions = copy(self.VALID_ACTIONS)
        if state.blank_pos[0] == 0:
            actions.remove('U')
        if state.blank_pos[0] == state.board_size - 1:
            actions.remove('D')
        if state.blank_pos[1] == 0:
            actions.remove('L')
        if state.blank_pos[1] == state.board_size - 1:
            actions.remove('R')
        return actions

    def goal_test(self, state):
        return state.tile_list == self.goal_state.tile_list

    def transition(self, state, action):
        return state.move(action), 1.0
