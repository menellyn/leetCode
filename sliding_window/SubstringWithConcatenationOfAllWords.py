def findSubstring(s: str, words: list[str]) -> list[int]:
    words.sort()
    ans = []
    word_len = len(words[0])
    left = 0
    n = len(s)
    tmp = []

    for right in range(0, n, word_len):
        print(right)
        tmp.append(s[right:right+word_len])
        print(tmp)
        if len(tmp) == len(words):
            print(tmp)
            if sorted(tmp) == words:
                ans.append(left)
            
            tmp.remove(s[left:left+word_len])
            left += word_len

    return ans


print(findSubstring("barfoothefoobarman", ["foo","bar"]))