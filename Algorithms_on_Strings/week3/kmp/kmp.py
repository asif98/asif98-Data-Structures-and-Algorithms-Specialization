# python3
import sys

def find_s(pattern, text):
    res = []
    s = pattern + "$" + text
    prefix_func = [None]*len(s)
    prefix_func[0] = 0
    cur_border = 0
    count = 0
    for i in range(1, len(s)) :
        while cur_border > 0 :
            count += 1
            if s[i] == s[cur_border] :
                cur_border += 1
                prefix_func[i] = cur_border
                break
            else :
                cur_border = prefix_func[cur_border-1]
        else :
            ###### cur_border = 0
            if s[0] == s[i] :
                cur_border = 1
            prefix_func[i] = cur_border
        if cur_border == len(pattern) :
            res.append(i-2*len(pattern))
    print(prefix_func)
    print(count)
    return res

pattern = "ACATACATACACA"
print(find_s(pattern, ""))

# if __name__ == '__main__':
#     s = sys.stdin.readline().strip()
#     text = sys.stdin.readline().strip()
#     result = find_s(s, text)
#     print(" ".join(map(str, result)))
