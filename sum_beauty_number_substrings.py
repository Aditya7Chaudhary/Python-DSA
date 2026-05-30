def sum_beauty_number_substrings(s):
    n = len(s)
    ans = 0

    for i in range(n):
        freq = {}
        left = i

        while left >= 0:
            freq[s[left]] = freq.get(s[left],0) + 1
            left -= 1
        
            ans += max(freq.values()) - min(freq.values())

    return ans

s = "aabcb"
print(sum_beauty_number_substrings(s))