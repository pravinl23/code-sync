class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        res = []
        idx = 0
        for s in strs:
            c = "".join(sorted(s))
            if c in seen:
                res[seen[c]].append(s)
            else:
                res.append([s])
                seen[c] = idx
                idx += 1

        return res