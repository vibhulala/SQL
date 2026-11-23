
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        MOD = 10**9 + 7

        pse = [-1] * n
        nse = [n] * n

        stack = []

        # Previous Smaller Element
        for i in range(n):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                pse[i] = stack[-1]

            stack.append(i)

        stack = []

        # Next Smaller or Equal Element
        for i in range(n - 1, -1, -1):

            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # Calculate contribution
        total = 0

        for i in range(n):

            left = i - pse[i]
            right = nse[i] - i

            contribution = arr[i] * left * right

            total = (total + contribution) % MOD

        return total
