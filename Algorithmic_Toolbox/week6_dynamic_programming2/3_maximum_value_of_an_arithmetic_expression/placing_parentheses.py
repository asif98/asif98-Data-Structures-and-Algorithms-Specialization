# Uses python3

def get_maximum_value(dataset):
    n = len(dataset)//2
    dp_matrix = [[None]*(n+1) for _ in range(n+1)]

    def dp(i, j) :  #### 0<= i <= j <= n

        if dp_matrix[i][j] != None :
            return dp_matrix[i][j]

        ans = [float("inf"), float("-inf")]
        if i == j :
            ans = [int(dataset[2*i]), int(dataset[2*i])]
        else :
            for k in range(2*i+1, 2*j, 2) :
                op = dataset[k]
                _i = (k-1)//2
                j_ = (k+1)//2

                left_min = dp(i, _i)[0]
                right_min = dp(j_, j)[0]
                left_max = dp(i, _i)[1]
                right_max = dp(j_, j)[1]

                if op == "+" :
                    ans[0] = min(ans[0], left_min + right_min)
                    ans[1] = max(ans[1], left_max + right_max)
                elif op == "-" :
                    ans[0] = min(ans[0], left_min - right_max)
                    ans[1] = max(ans[1], left_max - right_min)
                else :
                    ans[0] = min(ans[0], left_min*right_max, left_max*right_min, left_min*right_min, left_max*right_max)
                    ans[1] = max(ans[1], left_min*right_max, left_max*right_min, left_min*right_min, left_max*right_max)

        dp_matrix[i][j] = ans
        return ans
    return dp(0, n)[1]

# dataset = "5-8+7*4-8+9"
# print(get_maximum_value(dataset))

if __name__ == "__main__":
    print(get_maximum_value(input()))

# def evalt(a, b, op):
#     if op == '+':
#         return a + b
#     elif op == '-':
#         return a - b
#     elif op == '*':
#         return a * b
#     else:
#         assert False
