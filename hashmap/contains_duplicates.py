class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}

        for i in range(len(nums)):
            if nums[i] in visited and abs(visited[nums[i]] - i) <= k:
                return True
            else:
                visited[nums[i]] = i

        return False