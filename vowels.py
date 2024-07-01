class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

            elif s_list[left] in vowels:
                right -= 1

            elif s_list[right] in vowels:
                left += 1

            else:
                left += 1
                right -= 1

        hello = "hello"
        hello.strip()

        return "".join(s_list)


solution = Solution()
print(solution.reverseVowels("hello"))
