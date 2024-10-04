#162. find peak element (leetcode)
'''class Solution(object):
    def findPeakElement(self, nums):
        l,r = 0, len(nums) = 1

        while l <=r:
            m =l +((r-1) // 2)
            #left neighbour geater
            if m >0 and num[m] < nums[m-1]:
                r = m-1
            #right neighbour
            elif m < len(nums) - 1 and nums[m] < nums[m+1]:
                l = m+1
            else:
                return m'''
