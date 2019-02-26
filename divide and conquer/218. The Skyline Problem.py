"""
https://leetcode.com/problems/the-skyline-problem/description/
https://briangordon.github.io/2014/08/the-skyline-problem.html
"""
def critical_points(buildings):
    import heapq
    xi = [building[0] for building in buildings]
    xi += [building[1] for building in buildings]
    heapq.heapify(xi)
    return xi


def main():
    buildings = [
        [2, 9, 10],
        [3, 7, 15],
        [5, 12, 12],
        [15, 20, 10],
        [19, 24, 8]
    ]  # [left, right, height], sorted by left
    key_points_result = [
        [2, 10],
        [3, 15],
        [7, 12],
        [12, 0],
        [15, 10],
        [20, 8],
        [24, 0]
    ]  # [left, height], must be sorted by left

    #buildings = [[1,2,1],[1,2,2],[1,2,3]]

    x = [building[0] for building in buildings]
    x += [building[1] for building in buildings]
    x = list(set(x))
    x.sort()

    current_buildings = set()
    current_building_index = 0
    key_points = []
    for xi in x:
        # Add all buildings that start at xi
        while current_building_index < len(buildings) and buildings[current_building_index][0] == xi:
            current_buildings.add(tuple(buildings[current_building_index]))
            current_building_index += 1
        # Remove all buildings that stop at xi
        current_buildings = {building for building in current_buildings if building[1] != xi}
        # If max height at xi != max height at xi-1,
        # new key point is found
        current_max_height = max(current_buildings, key=lambda x: x[2]) if current_buildings else (0,0,0)
        if not key_points or key_points[-1][1] != current_max_height[2]:
            key_points.append([xi, current_max_height[2]])
    print(key_points)


if __name__ == '__main__':
    main()