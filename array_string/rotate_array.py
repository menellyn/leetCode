class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = len(nums)

        if k == l or k == 0 or l == 1:
            return

        if k > l:
            n = k // l
            k = k - n*l

        tmp_arr = nums[-k:]
        idx, tmp_idx = l - 1, l -1 -k
        while tmp_idx >= 0:
            nums[idx] = nums[tmp_idx]
            idx -= 1
            tmp_idx -=1

        nums[:k] = tmp_arr