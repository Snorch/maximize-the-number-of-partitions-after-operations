'''
Count unique characters until k + 1, return index to the start of next k-partition
'''
def next_partition(s, start, k):
    uniq = 0
    chars = [0] * 26
    i = start
    while i < len(s):
        chid = ord(s[i]) - ord('a')
        if not chars[chid]:
            uniq += 1
            if uniq > k:
                return i;
        chars[chid] += 1
        i += 1;
    return len(s)


'''
Find the start of next k-partition and advance to it, while counting partitions
'''
def partitions(s, k, debug):
    parts = 0
    start = 0
    while start < len(s):
        n = next_partition(s, start, k)
        parts += 1
        if debug:
            print(f'{s[start:n]} ', end='')
        start = n
    if debug:
        print()
    return parts

'''
Counter-example to
https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/
problem 3003, correct answer should be 3, but system expects 4.

The idea of counter-example is based on the fact that in "Hint 3", authors
don't take into consideration that replacement of i-th character may exstend
the partition preceeding the partition where i resides.
'''

s = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxzyxwvutsrqponmlkjihgfedcba'
k = 25

'''
Bruteforce each posible single character replacement and find number of k-partitions for it
'''
m = 0
for i in range(len(s)):
    for c in range(26):
        tmp = s[:i] + chr(ord('a') + c) + s[i+1:]
        p = partitions(tmp, k, 0)
        if p > m:
            m = p
            print(f'i = {i}, m = {m}\n')
            partitions(tmp, k, 1)
