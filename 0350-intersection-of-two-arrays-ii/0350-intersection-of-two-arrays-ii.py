class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #so we have here two cases that if the given array is not sorted array ; in that case we will use "HASH MAP FREQUENCY TABLE " 
        '''
        hmap={}
        ans=[]
        for n in nums1:
            hmap[n]=hmap.get(n,0)+1
        for n in nums2:
            if n in hmap and hmap[n]>0:
                hmap[n]-=1
                ans.append(n)
        return ans
        '''
        # and if the given array will be sorted than we will use two pointer approach 
        ans=[]
        nums1,nums2=sorted(nums1),sorted(nums2)
        p1=p2=0
        n,m=len(nums1),len(nums2)
        while p1<n and p2<m:
            if nums1[p1]==nums2[p2]:
                ans.append(nums1[p1])
                p1+=1
                p2+=1
                continue
            if nums1[p1]>nums2[p2]:
                p2+=1
            else:
                p1+=1
        return ans
