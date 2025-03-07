class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmp = "" #  empty list to store the common prefix as we iterate through
        strs = sorted(strs) #  sorted the list lexicographically (alphabetical order)
        first = strs[0] # grab the first and last string in alphabetical order
        last = strs[-1]
        for i in range(min(len(first),len(last))): # iterate to the length of shorter string (cant be more than this)
            if(first[i]!=last[i]): #if the letters dont match end and return the list
                return cmp
            cmp+=first[i] # if they do match append them
        return cmp