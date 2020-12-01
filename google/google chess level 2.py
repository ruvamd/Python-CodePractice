'''
As a henchman on Commander Lambda's space station, you're expected to be resourceful,
smart, and a quick thinker. It's not easy building a doomsday device and capturing
bunnies at the same time, after all! In order to make sure that everyone working for 
her is sufficiently quick-witted, Commander Lambda has installed new flooring outside 
the henchman dormitories. It looks like a chessboard, and every morning and evening 
you have to solve a new movement puzzle in order to cross the floor. That would be 
fine if you got to be the rook or the queen, but instead, you have to be the knight. 
Worse, if you take too much time solving the puzzle, you get "volunteered" as a test 
subject for the LAMBCHOP doomsday device!
To help yourself get to and from your bunk every day, write a function called 
solution(src, dest) which takes in two parameters: the source square, on which you 
start, and the destination square, which is where you need to land to solve the puzzle.
  The function should return an integer representing the smallest number of moves it 
  will take for you to travel from the source square to the destination square using 
  a chess knight's moves (that is, two squares in any direction immediately followed 
  by one square perpendicular to that direction, or vice versa, in an "L" shape).  
  Both the source and destination squares will be an integer between 0 and 63, 
  inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
'''
#~ code
# sdRange=(0,64)

# def solution(src,dest):

#+ code
import heapq
from collections import defaultdict

# define chessboard parameters
BOARD_SIZE      = 8
BOARD_MOVEMENTS = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Node:
    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

    def __hash__(self):
        return hash(tuple(self))

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y

    def __lt__(self, other):
        return self.x < node.x or (self.x == node.x and self.y < node.y)

    def __str__(self):
        return "<Node (x=%d, y=%d, d=%.02f)>" % (self.x, self.y, self.distance)

    def __repr__(self):
        return self.__str__()

class Board:
    def __init__(self, size, movements):
        self.size = size
        self.movements = movements

    def node(self, position):
        """ Generate Node for given position """
        return Node(int(position % self.size) + 1, int(position / self.size) + 1)

    def valid(self, x, y):
        return True if x >= 0 < self.size and y >= 0 < self.size else False

    def distance(self, start, end):
        """ Find shortest distance using BFS """
        queue = []
        queue.append(start)
        visited = {}

        # run until queue is empty
        while queue:
            # grab first node in queue
            node = queue.pop(0)

            # return when destination is reached
            if node == end:
                return node.distance

            # process nodes that have not been visited
            if node not in visited:
                # mark node as visited
                visited[node] = True

                # validate piece movement
                for offset in self.movements:
                    x, y = list(tuple(x + y for x, y in zip(tuple(node), offset)))

                    # queue valid moves only
                    if self.valid(x, y):
                        queue.append(Node(x, y, node.distance + 1))

        return float('inf')

def solution(src, dest):
    # create chessboard graph
    chessboard = Board(size = BOARD_SIZE, movements = BOARD_MOVEMENTS)

    # create coordinates
    start = chessboard.node(src)
    end = chessboard.node(dest)

    # calculate distance between given positions
    distance = chessboard.distance(start, end)

    return distance

print(solution(0,1))