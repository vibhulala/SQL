class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # Store last occurrence of every character
        last_index = {}

        for i, char in enumerate(s):
            last_index[char] = i

        stack = []
        seen = set()

        for i, char in enumerate(s):

            # Skip if character already exists
            if char in seen:
                continue

            # Remove larger characters if they appear again later
            while (stack and
                   stack[-1] > char and
                   last_index[stack[-1]] > i):

                removed = stack.pop()
                seen.remove(removed)

            stack.append(char)
            seen.add(char)

        return "".join(stack)