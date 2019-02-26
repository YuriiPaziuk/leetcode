"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {restaurant: i for i, restaurant in enumerate(list1)}
        d2 = {restaurant: i for i, restaurant in enumerate(list2)}
        common_restaurants = d1.keys() & d2.keys()

        from collections import defaultdict
        choices = defaultdict(list)

        for restaurant in common_restaurants:
            choices[d1[restaurant] + d2[restaurant]].append(restaurant)

        return choices[min(choices)] if choices else []


def main():
    from pprint import pprint

    tests = [

        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"],
         ["Shogun"]),

        (["Shogun", "Tapioca Express", "Burger King", "KFC"],
         ["KFC", "Shogun", "Burger King"],
         ["Shogun"]),

        (["KFC", "Shogun",],
         ["Shogun", "KFC"],
         [])
    ]

    for list1, list2, result in tests:
        pprint(Solution().findRestaurant(list1, list2))


if __name__ == '__main__':
    main()
