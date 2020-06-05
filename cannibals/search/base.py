"""This module contains the base components of search methods.

Author: Ryan Strauss
"""

from abc import ABC, abstractmethod


class Node:
    """A node represents a single state in a search problem and is used by the graph-based search methods."""

    def __init__(self, state, path_cost, estimated_cost=0.0, solution=None):
        """Constructs a new node.

        Args:
            state: The state associated with this node.
            path_cost: The cost of the path leading to this node.
            estimated_cost: The estimated cost from this node to the solution. This is only relevant to informed
                search methods. Default to 0.0, for when doing uninformed search.
            solution: A list of actions that represent the solution for reaching this node. Defaults to None.
        """
        self.state = state
        self.path_cost = path_cost
        self.estimated_cost = estimated_cost
        self.estimated_solution_cost = self.path_cost + self.estimated_cost
        self.solution = solution or []

    def __eq__(self, other):
        return self.state.__eq__(other.state)

    def __lt__(self, other):
        return self.estimated_solution_cost < other.estimated_solution_cost

    def __hash__(self):
        return self.state.__hash__()

    def expand(self, problem, heuristic_fn=None):
        """Expands this node by returning a list of its successors.

        Each successor node contains a state that can be reached by taking an action in the current node's state.

        Args:
            problem: The `AbstractProblem` that is under consideration.
            heuristic_fn: The optional heuristic function being used.

        Returns:
            A list of this node's successors.
        """
        successors = []
        for action in problem.get_actions(self.state):
            next_state, step_cost = problem.transition(self.state, action)
            estimated_cost = 0.0 if heuristic_fn is None else heuristic_fn(next_state)
            successors.append(Node(next_state, self.path_cost + step_cost, estimated_cost, self.solution + [action]))

        return successors


class SearchStrategy(ABC):
    """The abstract base class that all search strategies inherit from."""

    @staticmethod
    @abstractmethod
    def search(problem):
        """Attempts to solve the given problem by performing a search over the state space.

        Args:
            problem: The `AbstractProblem` instance that is to be solved.

        Returns:
            A 2-tuple with:
                solution: A list of actions that represents the solution to the problem.
                nodes_generated: The number of nodes that were generated during the search process.
        """
        pass
