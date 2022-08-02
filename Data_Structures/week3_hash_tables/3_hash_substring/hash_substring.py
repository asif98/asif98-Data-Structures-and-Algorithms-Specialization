# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def exp(prime, x, n) :
    if n == 0 :
        return 1
    elif n%2 == 0 :
        return (exp(prime, x, n//2)**2) % prime
    else :
        return ((exp(prime, x, n//2)**2)*x) % prime

def get_occurrences(pattern, text):
    prime = 1000000007
    x = 263
    n = len(pattern)

    pattern_hash = 0
    for i in range(n) :
        pattern_hash = x*pattern_hash + ord(pattern[i])
        pattern_hash = pattern_hash % prime
    #print(pattern_hash)
    exp_x_n = exp(prime, x, n)
    res = []
    cur_hash = 0
    for i in range(len(text)) :
        cur_hash = x*cur_hash + ord(text[i])
        cur_hash = cur_hash % prime
        if i >= n :
            cur_hash -= exp_x_n*ord(text[i-n])
            cur_hash = cur_hash % prime
        #print(i, cur_hash)
        if i >= n-1 and cur_hash == pattern_hash  and pattern == text[i-n+1:i+1] :
            res.append(i-n+1)
    return res

# pattern = "est"
# text = "sTest"
# print(get_occurrences(pattern, text ))


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
