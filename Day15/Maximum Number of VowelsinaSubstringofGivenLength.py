class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        cur_v = max_v = sum([1 for x in s[:k] if x in vowels])
        for i in range(0, len(s) - k):
            cur_v += (s[i + k] in vowels) - (s[i] in vowels)
            if cur_v > max_v:
                max_v = cur_v
        return max_v
s = "abciiidef"
k = 3
solution = Solution()
result = solution.maxVowels(s, k)
print(result)