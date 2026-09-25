class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for i in range(len(strs)):
            curr = "".join(sorted(strs[i]))
            if curr not in res:
                res[curr] = [strs[i]]
            else:
                res[curr].append(strs[i])
        
        return list(res.values())