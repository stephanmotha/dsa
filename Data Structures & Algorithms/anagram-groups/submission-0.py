from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = defaultdict(list)

        # for i in strs:
        #     print("".join(sorted(i)))
        #     d["".join(sorted(i))].append(i)

        # return list(d.values())

        d = defaultdict(list)

        for i in strs:
            temp = [0]*26
            for char in i:
                temp[ord(char) - ord('a')] += 1
            d[tuple(temp)].append(i)

        return list(d.values())


        