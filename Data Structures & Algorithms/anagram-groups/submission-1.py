class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for i in strs:
            curr = "".join(sorted(i))
            if curr not in res:
                res[curr] = [i]
            else:
                res[curr].append(i)
        
        return list(res.values())