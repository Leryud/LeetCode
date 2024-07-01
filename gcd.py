class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Max length of the smallest string is the maxwe need to check
        max_len = max(len(str1), len(str2))

        # The GCD of both string's length
        a = len(str1)
        b = len(str2)
        print(a, b)
        while b:
            a, b = b, a % b
            print(a, b)

        gcd_int = a

        # What is the string sequence length of the gdc exisiting in both strings
        str1_gcd = [str1[i : i + gcd_int] for i in range(max_len // a)]
        str2_gcd = [str2[i : i + gcd_int] for i in range(max_len // a)]
        print(str1_gcd)
        print(str2_gcd)

        gcd_str = list(set(str1_gcd).intersection(str2_gcd))

        if gcd_str == []:
            return ""

        return gcd_str[0]


test_cases = {
    "case_2": {
        "str1": "ABABAB",
        "str2": "ABAB",
    }
}
solution = Solution()
print(solution.gcdOfStrings(**test_cases["case_2"]))
