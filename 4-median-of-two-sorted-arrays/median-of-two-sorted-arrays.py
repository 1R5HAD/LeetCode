class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        '''nums3=sorted(nums1+nums2)
        n=len(nums3)
        if n%2!=0:
            return nums3[n//2]
        else:
            return (nums3[int(n/2)-1] + nums3[int(n/2)]) / 2'''


        A, B = nums1, nums2
        if len(A) > len(B):          # binary search on the smaller array
            A, B = B, A
        m, n = len(A), len(B)
        half = (m + n + 1) // 2      # size of the combined left half

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2       # take i elements from A
            j = half - i             # take j elements from B

            Aleft  = A[i-1] if i > 0 else float('-inf')
            Aright = A[i]   if i < m else float('inf')
            Bleft  = B[j-1] if j > 0 else float('-inf')
            Bright = B[j]   if j < n else float('inf')

            if Aleft <= Bright and Bleft <= Aright:   # valid split
                if (m + n) % 2:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:     # took too many from A
                hi = i - 1
            else:                    # took too few from A
                lo = i + 1