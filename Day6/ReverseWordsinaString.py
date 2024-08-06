class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, handles multiple spaces and trims leading/trailing spaces
        words = s.split()[::-1]  # Split and reverse the list of words
        result = " ".join(words)  # Join the reversed list with a single space
        return result
 
s = input("Enter the string: ")
solution = Solution()
result = solution.reverseWords(s)
print(result)