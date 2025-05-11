class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        """Return the length of the longest Fib-like subsequence of arr."""
        li = len(arr)-1
        tarr = {}
        for i in range(0, li+1):
            tarr[i] = arr[i]
        index_by_value = {}
        for i in range(0, li+1):
            index_by_value[tarr[i]] = i
        longest_fib_like_subs = 0
        current_fib_ss_l = 0
        max_value = arr[li]
        i = 0
        while (i <= (li-2)) and (i < li - longest_fib_like_subs+1):
            j = i+1
            while (j <= (li - 1)) and tarr[i]+tarr[j] <= max_value:
                if (tarr[i] + tarr[j]) in index_by_value:
                    k = index_by_value[tarr[i] + tarr[j]]
                    current_fib_ss_l = 3
                    if current_fib_ss_l > longest_fib_like_subs:
                        longest_fib_like_subs = current_fib_ss_l
                    x_i = j
                    x_i_1 = k
                    while (tarr[x_i] + tarr[x_i_1]) in index_by_value:
                        new_index = index_by_value[tarr[x_i] + tarr[x_i_1]]
                        x_i = x_i_1
                        x_i_1 = new_index
                        current_fib_ss_l += 1
                        if current_fib_ss_l > longest_fib_like_subs:
                            longest_fib_like_subs = current_fib_ss_l
                j += 1
            i += 1
        return longest_fib_like_subs


s = Solution()
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(s.lenLongestFibSubseq(arr))
