class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        c = []
        result=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    ans.append(list1[i])
                    c.append(i+j)
        m = min(c)
        for i in range(len(c)):
            if c[i] == m:
                result.append(ans[i])
        return result

        