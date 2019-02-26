"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.
Example 2:
Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:
Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""
class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        from collections import deque
        tokens = deque(self.parse_formula(formula))
        result = []
        tmp_stack = []

        while tokens:
            current = tokens.popleft()
            if current == ')':
                k = tokens.popleft()
                x = result.pop()
                while x != '(':
                    tmp_stack.append(x)
                    x = result.pop()
                while tmp_stack:
                    x = tmp_stack.pop()
                    result.append((x[0], x[1] * k))
            else:
                result.append(current)

        d = dict()
        for element, count in result:
            d[element] = d.get(element, 0) + count

        return ''.join(a + (str(d[a]) if d[a] > 1 else '') for a in sorted(d))

    def parse_formula(self, formula):
        """
        formula = 'Mg(OH)2'
        tokens = ['Mg', '(', 'O', 'H', ')', '2']
        return: [('Mg', 1), '(', ('O', 1), ('H', 1), ')', 2]
        """
        import re
        tokens = re.findall('[A-Z]{1}[a-z]?|\(|\)|\d+', formula)
        result = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '(' or tokens[i] == ')':
                result.append(tokens[i])
            elif tokens[i].isdigit():
                result.append(int(tokens[i]))
            else:
                if i == len(tokens) - 1:
                    result.append((tokens[i], 1))
                elif tokens[i + 1].isdigit():
                    result.append((tokens[i], int(tokens[i + 1])))
                    i += 1
                else:
                    result.append((tokens[i], 1))
            i += 1

        return result


def main():
    tests = [
        ("H2O", "H2O"),
        ("Mg(OH)2", "H2MgO2"),
        ("K4(ON(SO3)2)2", "K4N2O14S4")
    ]
    for formula, result in tests:
        #print(Solution().parse_formula(formula))
        print(Solution().countOfAtoms(formula))

    import re
    for formula, result in tests:
        print(re.findall('[A-Z][a-z]*\d*|\(|\)|\d+', formula))
        for t in re.findall('[A-Z][a-z]*\d*|\(|\)|\d+', formula):
            if t == '(' or t == ')' or t.isdigit():
                print(t)
            else:
                x = (re.findall('[A-Z][a-z]*|\d+', t))
                if len(x) == 1: x.append('1')
                print(x)

if __name__ == '__main__':
    main()
