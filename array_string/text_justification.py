class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = [[]]

        for word in words:
            current_len = sum(len(w)+1 for w in ans[-1]) - 1
            if current_len + len(word) + 1 <= maxWidth:
                ans[-1].append(word)
            else:
                ans.append([word])

        res = []

        for line in ans[:-1]:
            chars = sum(len(w) for w in line)
            spaces = maxWidth - chars
            j = 0

            for _ in range(spaces):
                line[j] += " "
                if len(line) != 1:
                    j = (j + 1)%(len(line) - 1)
            
            res.append("".join(line))
        
        res.append(" ".join(ans[-1]).ljust(maxWidth))
        return res