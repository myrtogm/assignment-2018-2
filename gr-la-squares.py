import csv
def read_sq(input):
    with open(input) as file:
        reader = csv.reader(file)
        rows = [r for r in reader]
    return rows
rows = read_sq("5x5.csv")
#print(rows)

visited = [False for row in rows]
all_transversals = []
transversal = []
#find all transversals of the latin square given
def findAllTrans(rows, first_row, first_num, column):
    visited[first_row] = True
    transversal.append(first_num)
    if len(transversal) == len(rows):
        all_transversals.append(transversal[:])
    else:
        next_row = first_row + 1
        # if next_row == len(rows):
        #     next_row = 0
        # else:
        column += 1
        for next_row in range(len(rows)):
            if not visited[next_row] and rows[next_row][column] not in transversal:
                findAllTrans(rows, next_row, rows[next_row][column], column)
    transversal.pop()
    visited[first_row] = False
    return all_transversals


def call():
    for i in range(0,len(rows)):
        findAllTrans(rows, i, i, 0)
        result = list(set(all_transversals))
    return result
print(call())

trans = {}
for t in all_transversals:
    if t[0] not in trans:
        [t[0]] = []
    trans[t[0]].append(t)
print(trans)

