from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        idx=0
        res=[]
        while idx<len(chars)-1:
            c=1
            while idx+1<len(chars) and chars[idx]==chars[idx+1]:
                c+=1
                idx+=1
            if c==1:
                res.append(chars[idx])
            else:
                res.append(chars[idx])
                res+=list(str(c))
            idx+=1
        if idx==len(chars)-1:
            res.append(chars[idx])
        chars.clear()
        for i in res:
            chars.append(i)

chars = list(input("Enter the characters separated by spaces: ").split())
solution = Solution()
length = solution.compress(chars)
print(f"Compressed array: {chars}")
print(f"New length: {length}")