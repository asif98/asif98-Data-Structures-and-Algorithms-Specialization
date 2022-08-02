# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((next, i))
            # Process opening bracket, write your code here
        elif next in ")]}":
            if opening_brackets_stack and are_matching(opening_brackets_stack[-1][0], next) :
                opening_brackets_stack.pop()
            else :
                return i+1
    if opening_brackets_stack :
        return opening_brackets_stack[0][1] + 1
    else :
        return "Success"

# print(find_mismatch("[{ab}"))

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
