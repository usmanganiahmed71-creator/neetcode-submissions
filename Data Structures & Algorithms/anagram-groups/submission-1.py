from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=dict()
        for st in strs:
            s="".join(sorted(st))
            if s in dic:
                dic[s].append(st)
            else:
                dic[s]=[]
                dic[s].append(st)
        return list(dic.values())