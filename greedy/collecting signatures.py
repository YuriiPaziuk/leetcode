"""
Problem Introduction
You are responsible for collecting signatures from all tenants of a certain building.
For each tenant, you know a period of time when he or she is at home.
You would like to collect all signatures by visiting the building as few times as
possible.

The mathematical model for this problem is the following. You are given a set
of segments on a line and your goal is to mark as few points on a line as possible
so that each segment contains at least one marked point.

Problem Description
Task. Given a set of 𝑛 segments {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} with integer coordinates on a line, find
the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a
set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖
, 𝑏𝑖
] there is a point 𝑥 ∈ 𝑋 such
that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖
.
Input Format. The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines
contains two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th
segment.
Constraints. 1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 109
for all 0 ≤ 𝑖 < 𝑛.
Output Format. Output the minimum number 𝑚 of points on the first line and the integer coordinates
of 𝑚 points (separated by spaces) on the second line. You can output the points in any order. If there
are many such sets of points, you can output any set. (It is not difficult to see that there always exist
a set of points of the minimum size such that all the coordinates of the points are integers.)
"""
def foo(time_intervals):
    from operator import itemgetter
    result = dict()
    while time_intervals:
        m = min(time_intervals, key=itemgetter(1))
        result[m[1]] = {time_interval for time_interval in time_intervals if time_interval[0] < m[1]}
        time_intervals -= result[m[1]]
    return result


def main():
    from operator import itemgetter
    s = [1, 3, 0, 5, 3, 5,  6,  8,  8,  2,  12]  # start time
    f = [4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 15]  # finish time
    time_intervals = set(zip(s, f))
    print(foo(time_intervals))


if __name__ == '__main__':
    main()