# recursion
# at each stair check what options we have and branch into those options
# when we are at the top - return 1 as we've reached the end and can add this
# steps combo to the final list
# O(n^2) time, O(n) space for the call stack

# need a faster approach
# a 1d dp could be used as we have a problem of repeating smaller size problems the solutions
# to which are additive in solving of the bigger problem
# we start from one stair and then move along the array filling it using the previous values
# when we have no stairs we have 0 ways to climb them
# for 1 stair we have only one way - 1 step
# for 2 stairs we have 2 ways - 1 step and 2 steps
# for 3 stairs we can make 1 step, get to the 2 and from there have 2 ways; or we could make 2 steps, get to the 1 and from there have
# only 1 way, in total having 

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if not n:
#             return 1
#         one = self.climbStairs(n-1)
#         two = self.climbStairs(n-2) if n >= 2 else 0
#         return one + two
        
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        i = 1
        while i < n:
            i += 1
            dp.append((dp[i-1] or 1) + (dp[i-2] or 1))
                        
        
        return dp[i]

