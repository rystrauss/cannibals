"""This script provides an example of how to use `cannibals` on the 8-puzzle.

Author: Ryan Strauss
"""

from cannibals.problems.sliding_tile.heuristics import misplaced_tiles, make_heuristic_fn
from cannibals.problems.sliding_tile.puzzle import SlidingTilePuzzle
from cannibals.search.informed_search import AStarSearch
from cannibals.search.uninformed_search import BreadthFirstSearch, UniformCostSearch


def main():
    # Define the problem we want to solve
    # This instance of the 8-puzzle is solvable in 10 moves
    problem = SlidingTilePuzzle('635841027', '865317024')

    # Solve the problem using three different algorithms
    _, bfs_nodes = BreadthFirstSearch.search(problem)
    _, uc_nodes = UniformCostSearch.search(problem)
    # For A*, we specify that the misplaced tiles heuristic should be used
    solution, astar_nodes = AStarSearch.search(problem, heuristic_fn=make_heuristic_fn(problem, misplaced_tiles))

    print(f'Solution: {solution}')
    print(f'\nNodes generated by BFS:\t{bfs_nodes}')
    print(f'Nodes generated by UC:\t{uc_nodes}')
    print(f'Nodes generated by A*:\t{astar_nodes}')


if __name__ == '__main__':
    main()
