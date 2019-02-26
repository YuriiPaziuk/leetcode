"""
Suppose you are starting a radio show. You want to reach listeners
in all 50 states. You have to decide what stations to play on to reach
all those listeners. It costs money to be on each station, so you are
trying to minimize the number of stations you play on. Each station
covers a region and they overlap. Find the smallest set of stations
you can play on to cover all 50 states.

Greedy algorithm.
1. Pick the station that covers the most states that haven't been
   covered yet. It's OK if the station covers some states that has
   been covered already.
2. Repeat until all states are covered.
"""
def choose_stations(stations, states_to_cover):
    from operator import itemgetter
    result = []
    not_covered_states = states_to_cover.copy()
    while not_covered_states:
        covers_most = max([(station, len(not_covered_states.intersection(stations[station]))) for station in stations], key=itemgetter(1))
        result.append(covers_most[0])
        not_covered_states -= stations[covers_most[0]]
    return result


def main():
    stations = {
        'KONE':   {'ID', 'NV', 'UT'},
        'KTWO':   {'WA', 'ID', 'MT'},
        'KTHREE': {'OR', 'NV', 'CA'},
        'KFOUR':  {'NV', 'UT'},
        'KFIVE':  {'CA', 'AZ'}
    }
    states_to_cover = {station for station_list in stations.values() for station in station_list}
    print(choose_stations(stations, states_to_cover))


if __name__ == '__main__':
    main()