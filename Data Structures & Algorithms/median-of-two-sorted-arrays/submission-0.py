import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        def find_median(k, start1, end1, start2, end2):
            if start1 > end1:
                return nums2[k-start1]
            
            if start2 > end2:
                return nums1[k-start2]
            
            id1, id2 = (start1 + end1) // 2, (start2 + end2) // 2
            m1, m2 = nums1[id1], nums2[id2]

            if id1 + id2 < k:
                if m1 > m2:
                    return find_median(k, start1, end1, id2 + 1, end2)
                else:
                    return find_median(k, id1 + 1, end1, start2, end2)
            else:
                if m1 > m2:
                    return find_median(k, start1, id1 - 1, start2, end2)
                else:
                    return find_median(k, start1, end1, start2, id2 - 1)
        if (m + n) % 2 == 0:
            return (find_median((m + n) // 2, 0, m-1, 0, n-1) + find_median((m + n) // 2 - 1, 0, m-1, 0, n-1)) / 2
        else:
            return find_median((m + n) // 2, 0, m-1, 0, n-1)
        