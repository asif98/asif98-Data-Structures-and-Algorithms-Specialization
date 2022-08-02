#Uses python3

import sys

def lcs3(seq1, seq2, seq3):
    n1 = len(seq1)
    n2 = len(seq2)
    n3 = len(seq3)

    dp_matrix = [[[None]*n3 for _ in range(n2)] for ll in range(n1)]

    def dp(i1, i2, i3) :   ###### return lcs2(seq1[i1:], seq[i2:])

        if i1 == n1 or i2 == n2 or i3 == n3:
            return 0
        elif dp_matrix[i1][i2][i3] != None :
            return dp_matrix[i1][i2][i3]
        else :
            if seq1[i1] == seq2[i2]  == seq3[i3] :
                ans = 1 + dp(i1+1, i2+1, i3+1)
            elif seq1[i1] == seq2[i2] :
                ans = max( dp(i1, i2, i3+1), dp(i1+1, i2+1, i3) )
            elif seq2[i2]  == seq3[i3] :
                ans = max( dp(i1, i2+1, i3+1), dp(i1+1, i2, i3) )
            elif seq1[i1] == seq3[i3] :
                ans = max( dp(i1, i2+1, i3), dp(i1+1, i2, i3+1) )
            else :
                ans = max( dp(i1, i2+1, i3+1), dp(i1+1, i2, i3+1), dp(i1+1, i2+1, i3) )
            dp_matrix[i1][i2][i3] = ans
            return ans

    return dp(0, 0, 0)

# seq1 = [1, 2, 3]
#
# seq2 = [4, 5, 6]
#
# seq3 = [1, 3, 5]
# print(lcs3(seq1, seq2, seq3))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
