import heapq

class Solution:
    def medianSlidingWindow(self, nums, k):
        def add_num(num, max_heap, min_heap):
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            balance_heaps(max_heap, min_heap)

        def remove_num(num, max_heap, min_heap):
            if num <= -max_heap[0]:
                max_heap.remove(-num)
                heapq.heapify(max_heap)
            else:
                min_heap.remove(num)
                heapq.heapify(min_heap)
            balance_heaps(max_heap, min_heap)

        def balance_heaps(max_heap, min_heap):
            while len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            while len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

        def get_median(max_heap, min_heap):
            if len(max_heap) > len(min_heap):
                return -max_heap[0]
            return (-max_heap[0] + min_heap[0]) / 2.0

        max_heap, min_heap = [], []
        medians = []

        for i in range(len(nums)):
            add_num(nums[i], max_heap, min_heap)

            if i >= k - 1:
                medians.append(get_median(max_heap, min_heap))
                remove_num(nums[i - k + 1], max_heap, min_heap)

        return medians





from bisect import bisect_left, insort

class Solution:
    def medianSlidingWindow(self, nums, k):
        medians = []
        window = []

        for i in range(len(nums)):
            insort(window, nums[i])

            if len(window) > k:
                window.pop(bisect_left(window, nums[i - k]))

            if len(window) == k:
                if k % 2 == 1:
                    medians.append(float(window[k // 2]))
                else:
                    medians.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

        return medians
