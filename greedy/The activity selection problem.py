"""
We have a set of activities, that wish to use a resource, which
can only serve one activity at a time. each activity has a start
time and a finish time. We wish to select a maximum-size subset
of mutually compatible activities, that is the activities that
do not overlap.
"""
def get_timetable(start_times, finish_times):
    from operator import itemgetter
    activities = [(i, si, fi) for i, (si, fi) in enumerate(zip(start_times, finish_times))]
    result = []
    while activities:
        # Find the activity with minimum finish time
        t = min(activities, key=itemgetter(2))
        result.append(t)
        activities.remove(t)
        # Exclude non-compatible activities
        activities = [activity for activity in activities if activity[1] >= t[2]]
    return [activity[0] for activity in result]


def main():
    s = [1, 3, 0, 5, 3, 5,  6,  8,  8,  2,  12]  # start time
    f = [4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 15]  # finish time
    print(get_timetable(s,f))


if __name__ == '__main__':
    main()