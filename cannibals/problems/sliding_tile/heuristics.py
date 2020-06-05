"""Provides heuristic functions for the sliding tile puzzle.

Author: Ryan Strauss
"""

from cannibals.problems.sliding_tile import SlidingTilePuzzle


def make_heuristic_fn(problem, heuristic_fn):
    """Makes a heuristic function for the sliding tile puzzle.

    This function should be used to construct the function that will be passed to the search strategy.

    Args:
        problem: The `SlidingTilePuzzle` for which a heuristic function should be constructed.
        heuristic_fn: The heuristic function being used. E.g. `misplaced_tiles`.

    Returns:
        A function that accepts a single state as an argument and returns the estimated cost of that state, using the
        provided heuristic.
    """
    assert isinstance(problem, SlidingTilePuzzle)
    return lambda state: heuristic_fn(state, problem.goal_state)


def misplaced_tiles(state, goal):
    """Computes the misplaced tiles heuristic.

    This heuristic counts the number of tiles on the board that are not in their goal positions.
    It is admissible and consistent.

    Args:
        state: The current state being evaluated.
        goal: The goal state.

    Returns:
        The heuristic value, which is the number of tiles that are out of place.
    """
    count = 0
    for a, b in zip(state.tile_list, goal.tile_list):
        if a != b:
            count += 1
    return count
