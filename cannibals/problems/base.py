"""Provides the base abstract problem class, which represents a search problem.

Author: Ryan Strauss
"""

from abc import ABC, abstractmethod


class AbstractProblem(ABC):
    """An abstract problem, from which all problem classes should inherit.

    A problem in this case is referring to a search problem that can be solved by a goal-based problem-solving
    agent. The problem's states are represented atomically -- that is, as a whole with no internal structure visible
    to the agent.

    A problem consists of an *initial state*, a description of *actions*, a *transition model*, a *goal test*, and a
    *path cost function*.

    States can take any form for a particular problem, so long as their `__hash__` and `__eq__` methods are
    implemented to reflect that logically equivalent states are determined to be equal and are mapped to the same
    location in a hash table.
    """

    def __init__(self, initial_state):
        """Constructs a new `AbstractProblem`.

        Args:
            initial_state: The problem's initial state.
        """
        self._initial_state = initial_state

    @property
    def initial_state(self):
        """The initial state of the problem."""
        return self._initial_state

    @abstractmethod
    def get_actions(self, state):
        """Given a particular state, this method returns the set of possible actions that can be executed in that state.

        Args:
            state: The state whose actions are to be retrieved.

        Returns:
            An iterable containing all actions that can be taken in `state`.
        """
        pass

    @abstractmethod
    def goal_test(self, state):
        """Tests whether or not a particular state is a goal state.

        Args:
            state: The state to be tested.

        Returns:
            True if `state` is a goal state and False otherwise.
        """
        pass

    @abstractmethod
    def transition(self, state, action):
        """This method defines the transition model of the problem.

        Given a state and an action, it will return the next state along with the step cost of that transition.

        Args:
            state: The current state.
            action: The action being taken in `state`.

        Returns:
            The tuple `(next_state, step_cost)` where `next_state` is the state that we transitioned to and `step_cost`
            is the cost associated with doing that transition.
        """
        pass
