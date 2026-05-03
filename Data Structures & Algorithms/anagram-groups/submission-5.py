class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list)
        # loop over strs
        for w in strs:
            #sort it then join the result to get the actual sorted word
            # example cat  wil be act instead of ['a','c','t']
            sortedw = ''.join(sorted(w))
            #since its a list we can search/access by strings instead of index
            result[sortedw].append(w)
        return list(result.values())
