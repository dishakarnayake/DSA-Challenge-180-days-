

#Approach 1: Using the sorted function
class Solution(object):
    def merge(self, nums1, m, nums2, n):
       
        nums1[:] = sorted(nums1[:m] + nums2[:n])

       

#Approach 2: Using Two - Pointer

class solution(object):
    def merge(self, nums1, m, nums2, n):
            i, j, k = m - 1, n - 1, m + n - 1
            while i >= 0 and j >= 0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1



#Approach 2: Using Single - Pointer

class So_lution(object):
    def merge(self, nums1, m, nums2, n):
            k = m + n - 1
            i, j = m - 1, n - 1
            while k >= 0:
                if i >= 0 and j >= 0:
                    if nums1[i] > nums2[j]:
                        nums1[k] = nums1[i]
                        i -= 1
                    else:
                        nums1[k] = nums2[j]
                        j -= 1
                elif i >= 0:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1