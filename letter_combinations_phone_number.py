from string import ascii_lowercase
import itertools

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        else:
        
            letters_map = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}
        
            op = [str.lower (letters_map[each_key]) for each_key in digits]
            op = list(map(lambda x: ''.join (x),list(itertools.product(*op))))
            return op