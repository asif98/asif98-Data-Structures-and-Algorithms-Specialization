#Uses python3

import sys

def lcs2(seq1, seq2) :
    n1 = len(seq1)
    n2 = len(seq2)

    dp_matrix = [[None]*n2 for _ in range(n1)]

    def dp(i1, i2) :   ###### return lcs2(seq1[i1:], seq[i2:])

        if i1 == n1 or i2 == n2 :
            return 0
        elif dp_matrix[i1][i2] != None :
            return dp_matrix[i1][i2]
        else :
            if seq1[i1] == seq2[i2] :
                ans = 1 + dp(i1+1, i2+1)
            else :
                ans = max( dp(i1, i2+1), dp(i1+1, i2) )
            dp_matrix[i1][i2] = ans
            return ans

    return dp(0, 0)

# seq1 = [2, 7, 8, 3]
# seq2 = [5, 2, 8, 7]
# print(lcs2(seq1, seq2))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
