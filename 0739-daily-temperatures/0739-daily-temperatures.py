class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []#pair:[temp,index]
        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                l = stack.pop()
                answer[l] = r - l

            stack.append(r)

        return answer
