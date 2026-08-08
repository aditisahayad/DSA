class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:


        n = len(word1)
        m = len(word2)

        # next_pos[i] = earliest position in word1
        # where word2[i:] can be matched exactly
        next_pos = [-1] * m

        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                next_pos[j] = i
                j -= 1

        ans = []
        pos = 0
        used = False

        for j in range(m):
            found = False

            while pos < n:

                # Exact match
                if word1[pos] == word2[j]:
                    ans.append(pos)
                    pos += 1
                    found = True
                    break

                # Use one mismatch
                if not used:
                    if j == m - 1:
                        ans.append(pos)
                        pos += 1
                        used = True
                        found = True
                        break

                    if next_pos[j + 1] != -1 and next_pos[j + 1] > pos:
                        ans.append(pos)
                        pos += 1
                        used = True
                        found = True
                        break

                pos += 1

            if not found:
                return []

        return ans