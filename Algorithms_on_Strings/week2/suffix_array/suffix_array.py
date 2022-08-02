# python3
import sys
from functools import cmp_to_key

def build_suffix_array(text):
    n = len(text)
    # def compare(i, j) :
    #     for l in range(n) :
    #         if text[(i+l)%n] > text[(j+l)%n] :
    #             return 1
    #         elif text[(i+l)%n] < text[(j+l)%n] :
    #             return -1
    #suffix_sorted = sorted(list(range(n)), key = cmp_to_key(compare))
    suffix_sorted = sorted(list(range(n)), key = lambda i : text[i:])
    return suffix_sorted

  # """
  # Build suffix array of the string text and
  # return a list result of the same length as the text
  # such that the value result[i] is the index (0-based)
  # in text where the i-th lexicographically smallest
  # suffix of text starts.
  # """




if __name__ == '__main__':

    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
