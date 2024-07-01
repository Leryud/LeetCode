class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        for i, word in enumerate(s_list):
            s_list[i] = word.strip()
        s_list = [s for s in s_list if s != ""]

        return " ".join(s_list[::-1])


solution = Solution()
print(solution.reverseWords("  hello world  "))
