class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        answer = 0
        leng = 0
        dic = dict()
        st = 0
        end = 0
        if size == 1 or size == 0:
            return size
        while(True):
            if st == size - 1:
                break
            if end == size:
                st += 1
                end = st + 1
                continue
            if s[end] in dic.keys():
                del dic[s[st]]
                leng -= 1
                st += 1
            else:
                dic[s[end]] = 1
                leng += 1
                end += 1
            answer = max(answer, leng)

        return answer