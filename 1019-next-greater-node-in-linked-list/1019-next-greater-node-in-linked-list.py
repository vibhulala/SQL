class Solution:
    def nextLargerNodes(self, head):

        nums = []

        # Convert Linked List into Array
        while head:
            nums.append(head.val)
            head = head.next

        n = len(nums)
        result = [0] * n
        stack = []

        for i in range(n):

            # Find next greater element
            while stack and nums[i] > nums[stack[-1]]:

                index = stack.pop()
                result[index] = nums[i]

            # Store current index
            stack.append(i)

        return result