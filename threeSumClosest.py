class Solution:
    def threeSumClosest(self, nums, target):
        length = len(nums)
        if(length < 3):
            return []

        nums = sorted(nums)

        ans = sum(nums[0:3])

        for i in range(length - 2):
            y = i + 1
            m = length - 1

            while(y < m):
                temporary = nums[i] + nums[y] + nums[m]
                v = temporary - target

                if(abs(v) < abs(ans - target)):
                    ans = temporary

                if(v == 0):
                    return target
                elif(v > 0):
                    m -= 1
                else:
                    y += 1

        return ans
