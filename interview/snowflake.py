def numWays(words, target):
    mod = int(1e9 + 7)
    n = len(target)
    m = len(words[0])
    dp = [[0] * len(words) for _ in range(n)]
    
    # Count the frequency of each character in each position of words
    freq = [[0] * 26 for _ in range(m)]
    for w in words:
        for i in range(m):
            freq[i][ord(w[i]) - ord('a')] += 1
    
    # Fill the dynamic programming array
    for i in range(n):
        for j in range(len(words)):
            if target[i] != words[j][i]:
                continue
            if i == 0:
                dp[i][j] = freq[i][ord(target[i]) - ord('a')]
            else:
                for k in range(j+1):  # Include words[j] in the calculations
                    dp[i][j] += dp[i-1][k] * freq[i][ord(target[i]) - ord('a')]
                    dp[i][j] %= mod

    # Calculate the total number of ways to construct the target string
    total_ways = sum(dp[-1]) % mod

    return total_ways

# Test case
words = ['valya', 'lyglb', 'vldoh']
target = 'val'
result = numWays(words, target)
print(result)
