import numpy as np
from PIL import Image

with open('input/day10.txt', 'r') as f:
    inp = [l.strip() for l in f.readlines()]


def parse(inp):
    new_inp = [list(map(int, (line[10:16], line[18:24], line[36:38], line[40: 42]))) for line in inp]
    return new_inp


def bounding_box_area(points):
    min_x = min(points, key=lambda x: x[0])[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_x = max(points, key=lambda x: x[0])[0]
    max_y = max(points, key=lambda x: x[1])[1]
    return (max_y - min_y) + (max_x - min_x)


def vis(points):
    min_x = min(points, key=lambda x: x[0])[0]
    min_y = min(points, key=lambda x: x[1])[1]
    max_x = max(points, key=lambda x: x[0])[0]
    max_y = max(points, key=lambda x: x[1])[1]
    print(min_x, min_y)
    im = np.zeros((max_y - min_y + 1, max_x - min_x + 1), dtype=np.uint8)
    for x, y in points:
        im[y-min_y][x-min_x] = 255
    im = Image.fromarray(im)
    im.save('out.png')


def main():
    points = parse(inp)
    min_area = float('inf')
    min_points = None
    min_idx = None
    for i in range(15000):
        temp_points = tuple((x + i * vx, y + i * vy) for x, y, vx, vy in points)
        area = bounding_box_area(temp_points)
        if area < min_area:
            min_area = area
            min_points = temp_points
            min_idx = i
    print(min_area, min_idx)
    vis(min_points)


if __name__ == '__main__':
    main()
