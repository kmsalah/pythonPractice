def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')
        
        if len(digits) == 0:
            return []
        
        def helper(digit):
            if digit == len(digits):
                #all digits processed, so add partial_mnemoic to mnemonic
                #we add a copy since subsequent calls modify partial_mnemonic
                mnemonics.append(''.join(partial_mnemonic))
            else:
                #try all possible chars for this digit
                for c in MAPPING[int(digits[digit])]:
                    partial_mnemonic[digit] = c.lower()
                    helper(digit + 1)
        
        mnemonics = []
        partial_mnemonic = [0] * len(digits)
        helper(0)
        return mnemonics

print(letterCombinations('233'))
