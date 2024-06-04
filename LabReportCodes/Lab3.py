import random


class Node:

  def __init__(self, a, b, z):
    self.x = a
    self.y = b
    self.depth = z
    self.parent = None  # Add parent pointer


class DFS:

  def __init__(self):
    self.directions = 4
    self.x_move = [1, -1, 0, 0]
    self.y_move = [0, 0, 1, -1]
    self.found = False
    self.N = 0
    self.source = None
    self.goal = None
    self.goal_level = 999999
    self.state = 0

  def init(self, source_x, source_y, goal_x, goal_y):
    self.N = 3
    self.source = Node(source_x, source_y, 0)
    self.goal = Node(goal_x, goal_y, self.goal_level)

    graph = [[random.randint(0, 1) for _ in range(self.N)]
             for _ in range(self.N)]
    graph[source_x][source_y] = 0
    graph[goal_x][goal_y] = 0

    print("Generated Graph:")
    for row in graph:
      print(row)

    self.st_dfs(graph, self.source)

    if self.found:
      print("\nGoal found")
      print("Moves required =", self.goal.depth)
      self.print_path()  # Print the path to the goal
    else:
      print("\nGoal cannot be reached from the starting block")

  def print_direction(self, m, x, y):
    if m == 0:
      print("Moving Down ({}, {})".format(x, y))
    elif m == 1:
      print("Moving Up ({}, {})".format(x, y))
    elif m == 2:
      print("Moving Right ({}, {})".format(x, y))
    else:
      print("Moving Left ({}, {})".format(x, y))

  def st_dfs(self, graph, u):
    graph[u.x][u.y] = 0
    for j in range(self.directions):
      v_x = u.x + self.x_move[j]
      v_y = u.y + self.y_move[j]
      if (0 <= v_x < self.N) and (0 <= v_y < self.N) and graph[v_x][v_y] == 1:
        v_depth = u.depth + 1
        self.print_direction(j, v_x, v_y)
        if v_x == self.goal.x and v_y == self.goal.y:
          self.found = True
          self.goal.depth = v_depth
          return

        child = Node(v_x, v_y, v_depth)
        child.parent = u  # Set the parent of the child node
        self.st_dfs(graph, child)

      if self.found:
        return

  def print_path(self):
    print("\nPath to the goal:")
    current = self.goal
    path = []
    while current is not None:
      path.append((current.x, current.y))
      current = current.parent
    path.reverse()
    for position in path:
      print(position)


def main():
  source_x = int(input("Source x coordinate: "))
  source_y = int(input("Source y coordinate: "))
  goal_x = int(input("Enter goal x coordinate: "))
  goal_y = int(input("Enter goal y coordinate: "))

  d = DFS()
  d.init(source_x, source_y, goal_x, goal_y)


if __name__ == "__main__":
  main()
