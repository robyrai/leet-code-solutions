"""
1512. Number of Good Pairs

Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for ind, i in enumerate(nums):
            if ind == len(nums)-1:
                break
            inter = [x == i for x in nums[ind+1:]]
            [ans.append(x) for x in inter]
        return sum(ans)


if __name__ == "__main__":
    sol = Solution()
    n = [1,2,3,1,1,3]
    print(sol.numIdenticalPairs(n))
