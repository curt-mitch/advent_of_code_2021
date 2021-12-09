"""
--- Part Two ---

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin, although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.

The top-left basin, size 3:

2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:

2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:

2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?

"""

with open('input9.txt', 'r') as f:
  map = [line.strip('\n') for line in f.readlines()]

risk_points = []
basin_sizes = []
vertical_range = len(map) - 1
horizontal_range = len(map[0]) - 1

def recursive_basin(map, point, covered_points):
  # go left
  i = point[0]
  j = point[1]
  while i >= 0:
    if map[i][j] == '9':
      break
    if (i, j) not in covered_points:
      covered_points.append((i, j))
      covered_points = recursive_basin(map, [i, j], covered_points)
    i -= 1
  # go right
  i = point[0]
  while i < horizontal_range:
    if map[i][j] == '9':
      break
    if (i, j) not in covered_points:
      covered_points.append((i, j))
      covered_points = recursive_basin(map, [i, j], covered_points)
    i += 1
  # go up
  i = point[0]
  j = point[1]
  while j >= 0:
    if map[i][j] == '9':
      break
    if (i, j) not in covered_points:
      covered_points.append((i, j))
      covered_points = recursive_basin(map, [i, j], covered_points)
    j -= 1
  # go down
  j = point[1]
  while j < vertical_range:
    if map[i][j] == '9':
      break
    if (i, j) not in covered_points:
      covered_points.append((i, j))
      covered_points = recursive_basin(map, [i, j], covered_points)
    j += 1
  return covered_points

for i, row in enumerate(map):
  for j, val in enumerate(map[i]):
    current_val = int(map[i][j])
    # point above
    if i > 0 and current_val >= int(map[i-1][j]):
      continue
    # point left
    if j > 0 and current_val >= int(map[i][j-1]):
      continue
    # point right
    if j < horizontal_range and current_val >= int(map[i][j+1]):
      continue
    # point below
    if i < vertical_range and current_val >= int(map[i+1][j]):
      continue
    risk_points.append(current_val + 1)
    basin_sizes.append(recursive_basin(map, [i, j], []))

result = 1
for basin in sorted(basin_sizes, key=lambda basin: -len(basin))[:3]:
  result *= len(basin)

print(result)
