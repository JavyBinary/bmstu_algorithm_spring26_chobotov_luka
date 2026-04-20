import heapq


def find_k_largest_element(nums: list[int], k: int) -> int:
    if not nums or k > len(nums):
        return -1

    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]
