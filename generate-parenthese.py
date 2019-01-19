def swapChars(string, i, j):
    chars = list(string)
    chars[i],chars[j] = chars[j],chars[i]
    string = ''.join(chars)
    return string

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        start = ''
        for i in range(n):
            start += "()"
        
        permutations = self.getPerms(start)
        return permutations
        
        
    def getPerms(self, n):
        def directed_perms(i):
            if i == len(n) -1:
                copy = n
                result.append(copy)
                return
            for j in range(i, len(n)):
                n = swapChars(n, i, j)
                directed_perms(i + 1)
                n = swapChars(n, i, j)
        
        result = []
        directed_perms(0)
        return result
   

x = Solution();
myPerms = x.generateParenthesis(3)
print(myPerms)
        
        
        
        
        
        
        
        
        
        
        