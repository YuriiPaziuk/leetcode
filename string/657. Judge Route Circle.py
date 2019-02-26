# https://leetcode.com/problems/judge-route-circle/description/


def judgeCircle(moves):
    dxy = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    x = y = 0
    for move in moves:
        dx, dy = dxy[move]
        x += dx
        y += dy
    return x == 0 and y == 0
