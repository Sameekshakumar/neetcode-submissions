class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        count1 = dict()
        for i in s1:
            count1[i] = count1.get(i, 0) + 1
        count2 = {}
        for j in s2[:length]:
            count2[j] = count2.get(j, 0) + 1
        
        if count1 == count2:
            return True

        for k in range(length, len(s2)):
            count2[s2[k]] = count2.get(s2[k], 0) + 1
            count2[s2[k-length]] -= 1
            if count2[s2[k-length]] == 0:
                del count2[s2[k-length]]

            if count1 == count2:
                return True
        return False


        