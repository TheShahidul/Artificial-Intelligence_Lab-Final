from collections import deque

# directions
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_names = ['Up', 'Down', 'Left', 'Right']


def is_valid_move(grid, row, col):
  return 0 <= row < len(grid) and 0 <= col < len(
      grid[0]) and grid[row][col] == 0


def bfs(grid, start, dest):
  queue = deque([(start, [])])
  visited = set()

  while queue:
    (row, col), path = queue.popleft()

    if (row, col) == dest:
      return path + [(row, col)]

    if (row, col) in visited:
      continue

    visited.add((row, col))

    for i, (dr, dc) in enumerate(directions):
      new_row, new_col = row + dr, col + dc

      if is_valid_move(grid, new_row, new_col):
        queue.append(((new_row, new_col), path + [(row, col)]))

  return None


def print_path(path):
  if not path:
    print("No path found.")
    return

  print("Path from start to destination:")        #shahidul_213902017
  for i, (row, col) in enumerate(path):
    if i == 0:
      print(f"Start at ({row}, {col})")
    elif i == len(path) - 1:
      print(f"End at ({row}, {col})")
    else:
      print(
          f"Move {direction_names[path[i][0] - path[i-1][0] + 1]} from ({path[i-1][0]}, {path[i-1][1]}) to ({row}, {col})"
      )


# 0 is empty space, 1 is obstacles

grid = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]]

start = (0, 0)
destination = (4, 4)

path = bfs(grid, start, destination)
print_path(path)
