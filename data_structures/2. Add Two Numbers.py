# https://www.programcreek.com/2012/12/add-two-numbers/


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def addTwoNumbers(self, l1, l2):
        carry = 0
        result = []
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            result.append(carry % 10)
            carry //= 10
        if carry:
            result.append(1)
        return result



def main():
	pass


if __name__ == '__main__':
	main()
