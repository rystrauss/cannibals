"""Implementations of uninformed search strategies.

Author: Ryan Strauss
"""

from cannibals.problems.base import AbstractProblem
from cannibals.search.base import Node, SearchStrategy
from cannibals.search.frontiers import FIFOFrontier, LIFOFrontier, Frontier
from cannibals.search.informed_search import AStarSearch


def _graph_search(frontier_type, problem):
    """Performs a graph search.

    Args:
        frontier_type: The type of frontier to use. Should be a subclass of `Frontier`.
        problem: The `AbstractProblem` instance that is to be solved.

    Returns:
        A 2-tuple with:
            solution: A list of actions that represents the solution to the problem.
            nodes_generated: The number of nodes that were generated during the search process.
    """
    assert isinstance(problem, AbstractProblem)
    assert issubclass(frontier_type, Frontier)
    node = Node(problem.initial_state, 0)
    generated_nodes = 1

    if problem.goal_test(node.state):
        return node.solution

    frontier = frontier_type([node])
    explored = set()
    solution = None

    while not frontier.empty():
        node = frontier.pop()
        explored.add(node)
        children = node.expand(problem)
        generated_nodes += len(children)
        for child in children:
            if not (child in explored or child in frontier):
                if problem.goal_test(child.state):
                    solution = child.solution
                    break
                frontier.push(child)
        else:
            continue
        break

    return solution, generated_nodes


class BreadthFirstSearch(SearchStrategy):
    """Implementation of breadth-first search."""

    @staticmethod
    def search(problem):
        return _graph_search(FIFOFrontier, problem)


class DepthFirstSearch(SearchStrategy):
    """Implementation of depth-first search."""

    @staticmethod
    def search(problem):
        return _graph_search(LIFOFrontier, problem)


class UniformCostSearch(SearchStrategy):
    """Implementation of uniform-cost search."""

    @staticmethod
    def search(problem):
        return AStarSearch.search(problem)
