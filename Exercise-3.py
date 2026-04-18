import random

def midpoint_displacement(x1, y1, x2, y2, roughness, depth):
if depth == 0:
return []
mid_x = (x1 + x2) / 2.0
mid_y = (y1 + y2) / 2.0
mid_y += roughness * random.uniform(-1, 1)
left = midpoint_displacement(x1, y1, mid_x, mid_y, roughness, depth - 1)
right = midpoint_displacement(mid_x, mid_y, x2, y2, roughness, depth - 1)
return left + [(mid_x, mid_y)] + right
def generate_terrain(width, height, roughness, depth):
grid = [[0.0 for _ in range(width)] for _ in range(height)]
def diamond_square(x1, y1, x2, y2, current_roughness, current_depth):
if current_depth == 0 or (x2 - x1 < 2 and y2 - y1 < 2):
return
mid_x = (x1 + x2) // 2
mid_y = (y1 + y2) // 2
avg = (grid[y1][x1] + grid[y1][x2] + grid[y2][x1] + grid[y2][x2]) / 4.0
grid[mid_y][mid_x] = avg + current_roughness * random.uniform(-1, 1)
grid[y1][mid_x] = (grid[y1][x1] + grid[y1][x2]) / 2.0 + current_roughness * random.uniform(-1, 1)
grid[y2][mid_x] = (grid[y2][x1] + grid[y2][x2]) / 2.0 + current_roughness * random.uniform(-1, 1)
grid[mid_y][x1] = (grid[y1][x1] + grid[y2][x1]) / 2.0 + current_roughness * random.uniform(-1, 1)
grid[mid_y][x2] = (grid[y1][x2] + grid[y2][x2]) / 2.0 + current_roughness * random.uniform(-1, 1)
next_roughness = current_roughness / 2.0
diamond_square(x1, y1, mid_x, mid_y, next_roughness, current_depth - 1)
diamond_square(mid_x, y1, x2, mid_y, next_roughness, current_depth - 1)
diamond_square(x1, mid_y, mid_x, y2, next_roughness, current_depth - 1)
diamond_square(mid_x, mid_y, x2, y2, next_roughness, current_depth - 1)
diamond_square(0, 0, width - 1, height - 1, roughness, depth)
return grid

def detect_artifacts(terrain_grid, threshold):
suspicious_coords = set()
rows = len(terrain_grid)
cols = len(terrain_grid[0])

for i in range(rows):
for j in range(cols):
current = terrain_grid[i][j]

if j + 1 < cols and abs(current - terrain_grid[i][j + 1]) > threshold:
suspicious_coords.add((i, j))

if i + 1 < rows and abs(current - terrain_grid[i + 1][j]) > threshold:
suspicious_coords.add((i, j))

return list(suspicious_coords)

if __name__ == "__main__":
print("Midpoint Displacement Output (depth 2) ")
line_points = midpoint_displacement(0, 0, 10, 0, 2.0, 2)
for point in line_points:
print(f"({point[0]}, {point[1]:.2f})")

print("\nGenerate Terrain Output (3x3 grid, depth 1)")
terrain = generate_terrain(3, 3, 1.0, 1)
for row in terrain:
print([round(val, 2) for val in row])

print("\nDetect Artifacts Output (threshold 0.5) ")
artifacts = detect_artifacts(terrain, 0.5)
print(artifacts if artifacts else "No artifacts detected.")
