[1]: https://en.wikipedia.org/wiki/Missionaries_and_cannibals_problem

# Cannibals

Cannibals is a Python package containing implementations of search strategies for problem-solving agents. The name is
a reference to the [missionaries and cannibals problem][1], a classic problem in AI.

Cannibals provides an easy interface for creating and solving such problems. Any proper instance of an `AbstractProblem`
can be solved by any subclass of a `SearchStrategy`. The currently implemented search strategies are depth-first search,
breadth-first search, uniform-cost search, and A-star search. The classic sliding-tile-puzzle is provided as an example
problem. See [`8puzzle.py`](examples/8puzzle.py) for an example of how to use this package to solve the 8-puzzle.