from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Dictionary to store the numbers by their digit sum
        ds = defaultdict(list)

        # Calculate the digit sum for each number and store it in the dictionary
        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))
            ds[digit_sum].append(num)

        # Initialize the maximum sum to -1
        max_sum = -1

        # Iterate through the dictionary to find the maximum sum of pairs
        for num_list in ds.values():
            if len(num_list) > 1:
                # Sort the list and take the two largest numbers
                num_list.sort(reverse=True)
                max_sum = max(max_sum, num_list[0] + num_list[1])

        return max_sum
