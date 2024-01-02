from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def brute_force_closest_pair(points):
    min_distance_squared = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist_squared = distance_squared(points[i], points[j])
            min_distance_squared = min(min_distance_squared, dist_squared)

    return min_distance_squared

def strip_closest(points, strip, min_distance_squared):
    strip.sort(key=lambda point: point.y)

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j].y - strip[i].y) ** 2 < min_distance_squared:
            dist_squared = distance_squared(strip[i], strip[j])
            min_distance_squared = min(min_distance_squared, dist_squared)
            j += 1

    return min_distance_squared

def find_closest_pair(points):
    n = len(points)

    # Base case: if there are 2 or 3 points, use brute force
    if n <= 3:
        return brute_force_closest_pair(points)

    # Sort points by x-coordinate
    points.sort()

    # Divide the points into two halves
    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]

    # Recursively find the closest pairs in each half
    left_closest = find_closest_pair(left_half)
    right_closest = find_closest_pair(right_half)

    # Find the minimum distance between the two halves
    min_distance_squared = min(left_closest, right_closest)

    # Merge the two halves and find the closest pairs in the strip
    strip = [point for point in points if abs(point.x - points[mid].x) ** 2 < min_distance_squared]
    strip_min_distance_squared = strip_closest(points, strip, min_distance_squared)

    # Return the overall closest pair
    return min(strip_min_distance_squared, min_distance_squared)


if __name__ == '__main__':
    # input_n = int(input())
    # input_points = []
    # for _ in range(input_n):
    #     x, y = map(int, input().split())
    #     input_point = Point(x, y)
    #     input_points.append(input_point)
    input_points = [Point(x=4, y=4), Point(x=-2, y=-2), Point(x=-3, y=-4), Point(x=-1, y=3), Point(x=2, y=3), Point(x=-4, y=0), Point(x=1, y=1), Point(x=-1, y=-1), Point(x=3, y=-1), Point(x=-4, y=2), Point(x=-2, y=4)]


    result = sqrt(find_closest_pair(input_points))
    print("{0:.9f}".format(result))
