# Breadth-first search: find a shortest route

Constructed teaching fixture. This is not an actual course or student record.

In a maze, each square is a vertex and each legal move is an edge. With one unit per move, breadth-first search (BFS) finds a route with the fewest moves. BFS uses a first-in, first-out queue. Mark a vertex discovered when enqueueing it so a second parent cannot enqueue it again.

Graph for this lesson: neighbors of A are B then C; B reaches D; C reaches D; D reaches E. Start at A. Before consulting any tool, predict the queue after expanding B and write one reason. In this fixed ordering, the queue after B is [C, D]. The shortest A to E path uses three edges.

## Optional comparison
You may ask an AI assistant to produce BFS pseudocode for this graph. Do not ask it for your initial prediction. Before checking its result, flag one likely error, then hand-trace the queue as an independent check. Note which step you changed, why, and what you did not verify. If you used AI, disclose the tool and what you kept. No use of AI is required.

## Self-check
Without AI, explain why marking D only when dequeued could put D into the queue twice. Then give an example where the fewest moves need not be the lowest cost.
