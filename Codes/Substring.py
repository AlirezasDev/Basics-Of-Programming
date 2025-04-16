import re

def build_freq_dict(s):
    freq_dict = {}
    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def smallest_substring(ss, tt):
    n = len(ss)
    m = len(tt)
    if m > n:
        return ""
    
    tt_freq = build_freq_dict(tt)
    window_freq = {}
    required = len(tt_freq)
    formed = 0
    
    left = 0
    min_len = float('inf')
    min_substr = ""
    
    for right in range(n):
        char = ss[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        if char in tt_freq and window_freq[char] == tt_freq[char]:
            formed += 1
        
        while formed == required and left <= right:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_substr = ss[left:right + 1]
            
            window_freq[ss[left]] -= 1
            if ss[left] in tt_freq and window_freq[ss[left]] < tt_freq[ss[left]]:
                formed -= 1
            
            left += 1
    
    return min_substr if min_substr else ""

txt = input().split()
print(smallest_substring(txt[0],txt[1]))
