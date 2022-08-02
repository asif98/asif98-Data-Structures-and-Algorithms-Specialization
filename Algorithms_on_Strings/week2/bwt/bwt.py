# python3
import sys
from functools import cmp_to_key

def BWT(text):
    #text = [char for char in ]
    n = len(text)
    def compare(i, j) :
        for l in range(n) :
            if text[(i+l)%n] > text[(j+l)%n] :
                return 1
            elif text[(i+l)%n] < text[(j+l)%n] :
                return -1
    suffix_sorted = sorted(list(range(n)), key = cmp_to_key(compare))
    result = ""
    for idx in suffix_sorted :
        result += text[idx-1]
    return result

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
