import random

def generate_points(n, max_x, max_y):
    points = []
    for _ in range(n):
        x = random.randint(0, max_x)
        y = random.randint(0, max_y)
        points.append((x, y))
    return points

def count_points_in_region(points, region):
    x, y, width, height = region
    count = 0

    for px, py in points:
        if x <= px < x + width and y <= py < y + height:
            count += 1

    return count

def split_region(x, y, width, height, min_size):
    if width <= min_size or height <= min_size:
        print("Final Region:", (x, y, width, height))
        return

    half_w = width // 2
    half_h = height // 2

    split_region(x, y, half_w, half_h, min_size)
    split_region(x + half_w, y, half_w, half_h, min_size)
    split_region(x, y + half_h, half_w, half_h, min_size)
    split_region(x + half_w, y + half_h, half_w, half_h, min_size)



def find_dense_regions(points, x, y, width, height, min_size, density_threshold):
    region = (x, y, width, height)

    count = count_points_in_region(points, region)
    area = width * height
    density = count / area

    if density > density_threshold:
        print("Dense Region:", region, "Points:", count)

    if width <= min_size or height <= min_size:
        return

    half_w = width // 2
    half_h = height // 2


    find_dense_regions(points, x, y, half_w, half_h, min_size, density_threshold)
    find_dense_regions(points, x + half_w, y, half_w, half_h, min_size, density_threshold)
    find_dense_regions(points, x, y + half_h, half_w, half_h, min_size, density_threshold)
    find_dense_regions(points, x + half_w, y + half_h, half_w, half_h, min_size, density_threshold)


points = generate_points(100, 100, 100)

print("All Points:")
print(points)

print("\nSplit Regions:")
split_region(0, 0, 100, 100, 10)

print("\nDense Regions:")
find_dense_regions(points, 0, 0, 100, 100, 10, 0.02)