class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right < 2:
            return [-1, -1]

        primes = [True] * (right + 1)
        primes[0] = primes[1] = False  # 0 and 1 are not prime

        n = 2
        while n * n <= right:
            if primes[n]:
                for i in range(n * n, right + 1, n):  # Mark multiples of n as False
                    primes[i] = False
            n += 1

        new_arr = [i for i in range(left, right + 1) if primes[i]]

        # Edge case: If there are fewer than two primes, return [-1, -1]
        if len(new_arr) < 2:
            return [-1, -1]

        nums1, nums2 = -1, -1
        min_val = float('inf')

        for i in range(len(new_arr) - 1):
            curr = new_arr[i + 1] - new_arr[i]
            if curr < min_val:
                min_val = curr
                nums1, nums2 = new_arr[i], new_arr[i + 1]

        return [nums1, nums2]

