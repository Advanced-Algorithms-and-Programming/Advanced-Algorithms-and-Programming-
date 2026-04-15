import math
import matplotlib.pyplot as plt
import numpy as np


def draw_triangle(ax, x, y, size):
    h = (math.sqrt(3) / 2) * size
    ax.plot([x, x + size/2, x + size, x],
            [y, y + h, y, y])


def draw_sierpinski(ax, x, y, size, depth):
    if depth == 0:
        draw_triangle(ax, x, y, size)
        return

    s = size / 2

    draw_sierpinski(ax, x, y, s, depth - 1)
    draw_sierpinski(ax, x + s, y, s, depth - 1)
    draw_sierpinski(ax, x + s/2, y + (math.sqrt(3)/4)*size, s, depth - 1)


def draw_tree(ax, x, y, length, angle, depth):
    x2 = x + length * math.cos(math.radians(angle))
    y2 = y + length * math.sin(math.radians(angle))

    ax.plot([x, x2], [y, y2])

    if depth == 0:
        return

    length = length * 0.67

    draw_tree(ax, x2, y2, length, angle + 30, depth - 1)
    draw_tree(ax, x2, y2, length, angle - 30, depth - 1)


def count_boxes(img, size):
    r, c = img.shape
    count = 0

    for i in range(0, r, size):
        for j in range(0, c, size):
            box = img[i:i+size, j:j+size]
            if np.any(box > 0):
                count += 1

    return count


def fractal_dimension(img, sizes):
    counts = []
    logs = []

    for s in sizes:
        n = count_boxes(img, s)
        if n > 0:
            counts.append(math.log(n))
            logs.append(math.log(1/s))

    m, _ = np.polyfit(logs, counts, 1)
    return m


def sample_image(n=256):
    img = np.zeros((n, n))
    img[:, n//2] = 1
    return img


print("1 - Sierpinski")
print("2 - Tree")
print("3 - Fractal Dimension")

ch = input("Enter choice: ")

if ch == "1":
    fig, ax = plt.subplots()
    draw_sierpinski(ax, 0, 0, 8, 5)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

elif ch == "2":
    fig, ax = plt.subplots()
    draw_tree(ax, 0, 0, 8, 90, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

elif ch == "3":
    img = sample_image()
    sizes = [2, 4, 8, 16, 32, 64]
    d = fractal_dimension(img, sizes)
    print("Fractal Dimension:", round(d, 3))

else:
    print("Invalid")