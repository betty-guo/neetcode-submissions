class Solution:

    def encode(self, strs: List[str]) -> str:
        # can be any encoding, as long as the result fits in a string
        # another way is to store each string in the string as length#string
        output = [] # create string out of this later
        for s in strs:
            str_len = len(s)
            output.append(str(str_len) + "#")
            output.append(s)
        return "".join(output) # are there other ways to build strings? this joins them with no separator, if every item is a string

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        # first get the number (iterate until you hit #, then convert sublist)
        # then get string (iterate for rest)

        # use two pointers for start and end of length, word
        
        while i < len(s):
            j = i # start two pointers at the same place
            # increase j until hit #
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # convert substring up until #
            i = j + 1 # jump over #
            j = i + length # end of the string
            output.append(s[i:j]) # takes substring from i up until j (not including)
            i = j

        return output
