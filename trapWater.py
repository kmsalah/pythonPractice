class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0 
        stack = []
        totalA = 0
        while i<len(height):
            currHeight = height[i]
            if i == 0 and currHeight == 0:
                continue
            j = i+1
            while j < len(height) and currHeight != height[j]:
                stack.append(height[j])
                j+=1
            totalStackArea = 0
            for h in stack:
                totalStackArea += h
            stack = []
            currArea = (currHeight * (j-i-1)) - totalStackArea
            totalA += currArea
            i = j
        return totalA

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
        