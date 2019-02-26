"""
Many children came to a celebration. Organize them into the minimum
possible number of groups such that the age of any two children in
the same group differ by at most one year.
"""
def valid_subgroups(ages):
    """
    Return a list of all valid subgroups of children: age difference
    between children within a group is less then one year. Group
    size is [1...len(ages)].
    :param ages: dict(str: int), name -> age
    :return: list(tuple(str)), tuples of names
    """
    import itertools
    subgroups = []
    for group_size in range(len(ages), 0, -1):
        for group in itertools.combinations(ages, group_size):
            if max((ages[name] for name in group)) - min((ages[name] for name in group)) <= 1:
                subgroups.append(group)
    return subgroups


def subgroups_brute_force(ages, valid_subgroups):
    """
    All solutions, brute force approach.
    :param ages: dict(str: int), name -> age
    :param valid_subgroups:  list(tuple(str)), tuples of names
    :return: list(tuple(str))
    """
    import itertools
    result = []
    for nof_subgroups in range(1, len(valid_subgroups) + 1):
        for groups in itertools.combinations(valid_subgroups, nof_subgroups):
            children_in_groups = [x for group in groups for x in group]
            # Check if all children are in children_in_groups
            if len(set(children_in_groups)) == len(children_in_groups) == len(ages):
                result.append(groups)
    return result


def best_subgroups_brute_force(kids):
    return subgroups_brute_force(kids, valid_subgroups(kids))[0]


def best_subgroups_greedy(kids):
    groups = []
    group_min_age = -100
    for name in sorted(kids, key=lambda x: kids[x]):
        if kids[name] - group_min_age > 1:
            groups.append([])
            group_min_age = kids[name]
        groups[-1].append(name)
    return groups


def main():
    tests = [
        ({'a':2, 'b':3, 'c': 4, 'd': 4, 'e': 5}, 2),
        ({'a':2, 'b':4, 'c': 6, 'd': 8, 'e': 10}, 5),
        ({'a':2, 'b':2, 'c': 3, 'd': 3}, 1)
    ]
    for kids, nof_groups in tests:
        #print(valid_subgroups(kids))
        #print(subgroups_brute_force(kids, valid_subgroups(kids)))
        print(best_subgroups_brute_force(kids))
        print(best_subgroups_greedy(kids))


if __name__ == '__main__':
    main()