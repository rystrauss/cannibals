"""Contains implementations of various data structures which are to be used as frontiers.

Author: Ryan Strauss
"""

import heapq
from abc import ABC, abstractmethod
from collections import deque


class Frontier(ABC):
    """The abstract base class representing a frontier.

    A frontier is the collection of nodes that are currently under consideration for being visited next by the
    search algorithm.
    """

    def __init__(self, data):
        self._data = data
        self._hash_table = set(data)

    def __contains__(self, item):
        return self._hash_table.__contains__(item)

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    @abstractmethod
    def push(self, element):
        """Adds an element to the frontier.

        Args:
            element: The element being added.

        Returns:
            None.
        """
        pass

    @abstractmethod
    def pop(self):
        """Retrieves the next node to visit from the frontier.

        Returns:
            The next node to be visited.
        """
        pass

    def empty(self):
        """Determines whether or not the frontier is empty.

        Returns:
            True iff the frontier is empty and False otherwise.
        """
        return len(self._data) == 0


class FIFOFrontier(Frontier):
    """A frontier that follows First-In-First-Out ordering.

    Using a FIFO frontier results in the breadth-first search algorithm.
    """

    def __init__(self, data):
        super().__init__(deque(data))

    def push(self, element):
        self._data.append(element)
        self._hash_table.add(element)

    def pop(self):
        removed = self._data.popleft()
        self._hash_table.remove(removed)
        return removed


class LIFOFrontier(Frontier):
    """A frontier that follows Last-In-First-Out ordering.

    Using a LIFO frontier results in the depth-first search algorithm.
    """

    def __init__(self, data):
        super().__init__(deque(data))

    def push(self, element):
        self._data.append(element)
        self._hash_table.add(element)

    def pop(self):
        removed = self._data.pop()
        self._hash_table.remove(removed)
        return removed


class PriorityFrontier(Frontier):
    """A frontier that used a priority queue to determine ordering.

    This type of frontier is used by uniform cost search as well as A* search.
    """

    def __init__(self, data):
        super().__init__(data)
        heapq.heapify(self._data)

    def push(self, element):
        heapq.heappush(self._data, element)
        self._hash_table.add(element)

    def pop(self):
        removed = heapq.heappop(self._data)
        self._hash_table.remove(removed)
        return removed

    def maybe_update(self, element):
        """Possibly updates the priority of a given node in the queue.

        It is possible for two nodes to contain the same state but have different estimated solution costs (which
        correspond to the priority in the queue). This method accepts a node whose state is also represented by
        a node that is already in the frontier. The method will then check to see if the new node has a higher
        priority (i.e. lower estimated solution cost). If so, it will replace the preexisting node in the frontier with
        the better one. If not, the frontier will remain unchanged.

        Args:
            element: The node that might get updated. It is assumed that a node containing this node's state is
                already in the frontier.

        Returns:
            None.
        """
        # Get index for outdated version of element in the queue
        index = self._data.index(element)
        # The the version already in the queue has a lower priority, we can stop
        if self._data[index] < element:
            return
        # Remove the outdated version from the hash table
        self._hash_table.remove(self._data[index])
        # Update element in the queue
        self._data[index] = element
        # Add it back to the hash table
        self._hash_table.add(element)
        # Restore the heap property
        heapq.heapify(self._data)
