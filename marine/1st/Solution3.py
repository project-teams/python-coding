"""
3. Longest Substring Without Repeating Characters
"""
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        result = 0
        
        for i in s:
            if(i in temp):
                #특정 문자열이 포함되어 있으면 그 문자열 다음부터 마지막까지 잘라냄
                temp = temp[temp.index(i)+1:]
                
            temp.append(i)
            result = max(result, len(temp))
                
        return result