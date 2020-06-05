"""Implementations of informed search strategies.

Author: Ryan Strauss
"""

from cannibals.problems import AbstractProblem
from cannibals.search.base import SearchStrategy, Node
from cannibals.search.frontiers import PriorityFrontier


class AStarSearch(SearchStrategy):
    """Implementation of A* search.

    A* is the most widely known form of best-first search. It evaluates nodes by combining g(n), the cost to reach the
    node, and h(n), the estimated cost to get from the node to the goal. Thus, if we are trying to find the cheapest
    solution, a reasonable thing to try first is the node with the lowest value of g(n)+ h(n).
    """

    @staticmethod
    def search(problem, heuristic_fn=None):
        """Attempts to solve the given problem by performing a search over the state space.

        Args:
            problem: The `AbstractProblem` instance that is to be solved.
            heuristic_fn: A function that accepts a state of `problem` as the single argument and returns an estimate
                of the cost to reach the goal from that state. If None, no heuristic is used and this becomes uniform
                cost search.

        Returns:
            A 2-tuple with:
                solution: A list of actions that represents the solution to the problem.
                nodes_generated: The number of nodes that were generated during the search process.
        """
        assert isinstance(problem, AbstractProblem)
        node = Node(problem.initial_state, 0)
        generated_nodes = 1

        if problem.goal_test(node.state):
            return node.solution

        frontier = PriorityFrontier([node])
        explored = set()
        solution = None

        while not frontier.empty():
            node = frontier.pop()
            if problem.goal_test(node.state):
                solution = node.solution
                break

            explored.add(node)
            children = node.expand(problem)
            generated_nodes += len(children)
            for child in node.expand(problem, heuristic_fn=heuristic_fn):
                if not (child in explored or child in frontier):
                    frontier.push(child)
                elif child in frontier:
                    frontier.maybe_update(child)

        return solution, generated_nodes
