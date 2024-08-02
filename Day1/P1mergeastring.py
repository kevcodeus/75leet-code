class Solution:
    def mergeAlternately( self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        i=0
        w3=[]
        while i<l1 or i<l2:
            if i<l1:
                w3.append(word1[i])
            if i<l2:
                w3.append(word2[i])
            i+=1
        return ''.join(w3)
word1=input("word1:").split()
word2=input("word2:").split()
w=Solution()
print(w.mergeAlternately( word1, word2))