Explain the heuristics:

Heuristic 1:

We can evaluate how good the state is by looking at the stones in the mancala relative to the other player. If a state has a score of positive for player1 who is the maximizing player (let's say), this means that maximizing player has more stones than the opponent. So you want to make sure that the score is as high as possible. Higher the score is, higher the difference in captured stones is which means the state is a better state than previous states with low scores. 

This is the best heuristics as it is the way how humans think. Before making a move, we draw the minmax graph in our brain and analyse which state gets us the highest reward (number of captured stones in our mancala).

Heuristic 2:
Another way of judging if a state is a better state than other states is by checking number of empty cups. More empty cups means more chances for you to place a last stone in an empty cup and capture your opponent's horizontal and vertical stones
Note that this heursitic is already included in heurstic 1.

Does one player always win? No

How does node count change: In one experiment, node count using alpha beta pruning was 40806 while than using normal minimax algorithm without pruning was 4067338
