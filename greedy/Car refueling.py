"""
You have a car such that if you fill it up to full tank, you
can travel with it up to 400 kilometers without refilling it.
You need to get from point A to point B, the distance between
these points is 950 km. Of course, you need to refill on your
way, and luckily, there are a few gas stations on your way
from A to B. The distances from A to the corresponding gas
stations are 200, 375, 550, 750 km. You need to find the minimum
number of refills to get from A to B.

Greedy strategy. You first make some greedy choice, then you
reduce your problem to a smaller subproblem, and then you iterate
until there are no problems left.

There are a few different ways to make a greedy choice in this
particular problem:
1) refill at the closest gas station to you;
2) refill at the farthest reachable gas station - the station
   you can reach from your current position without refills;
3) go until there is no fuel and hope there will be a gas station
   in there.

Algorithm.
1. Start at A.
2. Refill at the farthest reachable gas station G.
3. Make G the new A.
"""
def stations(gas_stations, total_distance, tank_capacity):
    """
    Find where to refill. Greedy choice: refill at the farthest
    reachable gas station. Destination point should be reachable
    after the last refill, but not included in the result.

    :param gas_stations: list(int), distances to gas stations
    :param total_distance: int
    :param tank_capacity: int
    :return: list(int), stations where we need to refuel
    """
    stations_ahead = gas_stations + [total_distance]
    """refueling_stations = [0]
    while refueling_stations[-1] < total_distance - tank_capacity:
        # Go ahead until we pass a gas station
        station_we_pass, stations_ahead = stations_ahead[0], stations_ahead[1:]
        # If we do not have enough gas left to reach the next gas station
        if refueling_stations[-1] < refueling_stations[-1] + tank_capacity <= stations_ahead[0]:
            # Refuel
            refueling_stations.append(station_we_pass)
    """
    refueling_stations = [0]
    for i in range(len(stations_ahead) - 1):
        if stations_ahead[i] < refueling_stations[-1] + tank_capacity <= stations_ahead[i+1]:
            refueling_stations.append(stations_ahead[i])

    return refueling_stations


def main():
    tests = [
        ([200, 375, 550, 750], 950, 400, [0, 375, 750])
    ]
    for gas_stations, total_distance, tank_capacity, result in tests:
        print(gas_stations, total_distance, tank_capacity, result,
              stations(gas_stations, total_distance, tank_capacity))


if __name__ == '__main__':
    main()