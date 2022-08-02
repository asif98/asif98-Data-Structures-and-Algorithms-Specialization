# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print(self) :
        for idx in range(len(self.a)) :
            print(self.a[idx], self.b[idx])

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

# def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    # pivot_element = Position(0, 0)
    # while used_rows[pivot_element.row]:
    #     pivot_element.row += 1
    # while used_columns[pivot_element.column]:
    #     pivot_element.column += 1
    # return pivot_element

def SwapLines(row1, row2):
    a = equation.a
    b = equation.b

    a[row1], a[row2] = a[row2], a[row1]
    b[row1], b[row2] = b[row2], b[row1]
    # used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    # pivot_element.row = pivot_element.column;

def ProcessPivotElement(cur_row, cur_col):
    a = equation.a
    b = equation.b
    size = len(a)

    pivot_val = a[cur_row][cur_col]
    # a[cur_row] = [num/pivot_val for num in a[cur_row]]
    for col in range(size) :
        a[cur_row][col] /= pivot_val
    b[cur_row] /= pivot_val

    for row in range(size) :
        if row != cur_row :
            num = a[row][cur_col]
            for col in range(size) :
                a[row][col] -= num*a[cur_row][col]
            b[row] -= num*b[cur_row]
            # a[row] = [a[row][col] - a[row][cur_col]*a[cur_row][col] for col in range(size)]
    print("-----------")
    for idx in range(len(a)) :
        print(a[idx], b[idx])
    print("||||||||||||")

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    cur_row = 0
    for cur_col in range(size):
        for row in range(cur_row, size) :
            if a[row][cur_col] :
                SwapLines(row, cur_row)
                ProcessPivotElement(cur_row, cur_col)
                cur_row += 1
                break
        equation.print()

    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])

if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
