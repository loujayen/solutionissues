# solution issues
1-Buildings
In a grid of 4 by 4 squares you want to place
a building in each square with only some
clues:
The height of the buildings is between 1 and
4 floors.
No two buildings in a row or column may
have the same number of floors.
A clue is the number of buildings that you
can see in a row or column from the
outside.
Higher buildings block the view of lower
buildings located behind them.
def solve_puzzle(clues):
Pass the clues in a list of 16 items. This list
contains the clues around the clock, index:
  0 1 2 3
15       4
14       5
13       6
12       7
11 10 9 8
If no clue is available, add value `0`
Each puzzle has only one possible solution.
`solve_puzzle()` returns a list of 4 lists, each
of 4 integers. The first indexer is for the row,
the second indexer for the column.

2-Words in a graph
There is an undirected graph with letters in
the nodes. The same letter can be in
several nodes.
There is a function is_word which accepts
a string and returns the boolean value of
True in case the string is a word. So for the
graph depicted above, the function returns
True for the following strings: pop, rom,
corn, popcorn, rock, mock, ok.
