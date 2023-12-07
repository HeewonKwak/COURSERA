from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    now = 0
    stops.append(distance)
    stop = 0
    for i in range(len(stops)):
        if now + tank < stops[i]:
            now = stops[i-1]
            stop += 1
            if now + tank < stops[i]:
                return -1
        
    return stop


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
    # print(min_refills(950, 400, [200, 375, 550, 750]))
    # print(min_refills(200, 250, [100, 150]))
