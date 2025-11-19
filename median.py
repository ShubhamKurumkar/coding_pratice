class Solution:
    def findMedianSortedArrays(self, nums1, nums2) :
        com=nums1+nums2
        com=sorted(com)
        if len(com)%2==0:
            r=(len(com)//2)-1
            l=len(com)//2
            return (com[r]+com[l])/2
        else:
            return com[len(com)//2]