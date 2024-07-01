from typing import List

# NOT FINISHED


class Solution:
    def product_recursive(self, numbers):
        if not numbers:
            return 1
        return numbers[0] * self.product_recursive(numbers[1:])

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_output = []

        for i, value in enumerate(nums):
            temp_nums = nums[: i - 1] + nums[: i + 1]
            output = self.product_recursive(temp_nums)

            if output != 0:
                output /= value
            nums_output.append(int(output))

        return nums_output


solution = Solution()
print(
    solution.productExceptSelf(
        [
            1,
            2,
            3,
            4,
        ]
    )
)
