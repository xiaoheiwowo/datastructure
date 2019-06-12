t = ["flower", "flow", "floght"]
# hhhhh


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        length = len(strs)
        if length == 0:
            return ''
        elif length == 1:
            return strs[0]
        else:
            for i in strs:
                if len(i) == 0:
                    return ''
            max_len = 0
            for p in range(len(strs[0])):
                for i in range(length - 1):
                    try:
                        if strs[i][p] != strs[i + 1][p]:
                            return strs[0][:max_len]
                    except:
                        return strs[0][:max_len]
                max_len += 1
            return strs[0]

    def s2(self, strs):
        l_str = ''
        for i in list(zip(*[list(i) for i in strs])):
            if len(set(i)) == 1:
                l_str += i[0]
            else:
                break
        return l_str


# s = Solution()
# print(s.longestCommonPrefix(t))
# print(s.longestCommonPrefix([]))
# print(s.longestCommonPrefix(['a']))
# print(s.longestCommonPrefix(['c','c']))
# print(s.longestCommonPrefix(['a','c']))

# print(s.s2(t))
# print(s.s2([]))
# print(s.s2(['a']))
# print(s.s2(['c','c']))
# print(s.s2(['a','c']))


class Solution2:
    def isValid(self, s: str) -> bool:
        while ('[]' in s) or ('{}' in s) or ('()' in s):
            s = s.replace('[]', '')
            s = s.replace('{}', '')
            s = s.replace('()', '')

        return True if len(s) == 0 else False


class Solution3:
    def isValid(self, s: str) -> bool:
        stack = [0]
        mirror = {']': '[', '}': '{', ')': '('}
        for i in s:
            if i in '[{(':
                stack.append(i)
            else:
                if mirror[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(i)

        return True if len(stack) == 1 else False


# f = Solution3()

# print(f.isValid('[]'))
# print(f.isValid('[]{[()]}'))
# print(f.isValid(''))
# print(f.isValid('[]{'))
# print(f.isValid('}{'))


def foreach(l):
    ret = []
    while l is not None:
        ret.append(l.val)
        l = l.next
    print(ret)
    return ret

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution4:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_bak = l1
        while True:
            foreach(l1_bak)
            if l1.next is not None:
                if l1.val <= l2.val < l1.next.val:
                    if l2.next is not None:
                        tmp = l2
                        l2 = l2.next
                        tmp.next = l1.next
                        l1.next = tmp
                    else:
                        l2.next = l1.next
                        l1.next = l2
                        break
                if l1.next.next is not None:    
                    l1 = l1.next
                else:
                    if l2 is not None:
                        l1.next.next = l2
                    break
            else:
                if l1.val <= l2.val:
                    l1.next = l2
                    break
                else:
                    l1 = l2
                    l2.next = l1
                    break
        return l1_bak


class Solution5:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: 
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        mark = 0
        if l1.val <= l2.val:
            small, big = l1, l2
        else:
            small, big = l2, l1
        ret = small
        while True:
            if small.next is not None:
                if big.val < small.next.val:
                    # 插入
                    tmp = big
                    if big.next is not None:
                        big = big.next
                    else:
                        mark = 1
                    tmp.next = small.next
                    small.next = tmp
                    if mark:
                        break
                else:
                    pass
                    # 不插入
                        
                small = small.next
            else:
                small.next = big
                break
        return ret



# a = ListNode(1, ListNode(2, ListNode(4, ListNode(5))))
# b = ListNode(1, ListNode(3, ListNode(4)))
# a = ListNode(2)
# b = ListNode(1)
# a = None
# b = None
# # foreach(a)
# s = Solution5()
# l = s.mergeTwoLists(a, b)
# foreach(l)
    

class Solution6:
    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0:
            return 0
        i, j = 0, len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == val:
                if j == i:
                    break
                while nums[j] == val:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1

        return j + 1


print(Solution6().removeElement([1], 1))
print(Solution6().removeElement([1, 2, 3, 4, 1], 1))