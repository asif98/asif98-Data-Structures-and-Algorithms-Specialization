# Uses python3
def edit_distance(word1, word2):

    m = len(word1)
    n = len(word2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    ### dp[i][j] = #steps to go from word1[:i] to word2[:j]
    for i in range(n+1) :
        dp[0][i] = i
    for j in range(m+1) :
        dp[j][0] = j
    for i in range(1,m+1) :
        for j in range(1,n+1) :
            if word1[i-1] == word2[j-1] :
                dp[i][j] = dp[i-1][j-1]
            else :
                mn = min(1 + dp[i-1][j-1], 1 + dp[i-1][j])
                for idx in range(j,0,-1) :
                    if word2[idx-1] == word1[i-1] :
                        mn = min(mn, j-idx + dp[i-1][idx-1] )
                        break
                dp[i][j] = mn
    return dp[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
