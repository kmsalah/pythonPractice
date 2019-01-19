def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        sequence = ''
        while i <= n:
            if i == 1:
                sequence = '1'
                i+=1
                continue
            else:
                count = 0
                curr = sequence[0]
                newSequence = ''
                for j in range(len(sequence)):
                    if sequence[j] == curr:
                        count+=1
                    else:
                        newSequence += str(count)
                        newSequence +=(str(curr)) 
                        curr = sequence[j]
                        count = 1
                newSequence += str(count)
                newSequence += str(curr)    
                sequence = newSequence
                i+=1
        return sequence

        