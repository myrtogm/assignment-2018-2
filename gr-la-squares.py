import csv
import timeit
import sys

def read_sq(input):
    with open(input) as file:
        reader = csv.reader(file)
        first_square = [r for r in reader]
        for i,rows in enumerate(first_square):
            first_square[i] = [
                int(x) for x in rows
            ]
    return first_square
first_square = read_sq("4x4.csv" )
print(first_square)


# ______STEP 1________
visited = [False for row in first_square]
all_transversals = []
transversal = []
#find all transversals of the latin square given
def findAllTrans(first_square, first_row, first_num, column):
    visited[first_row] = True
    transversal.append(first_num)
    if len(transversal) == len(first_square):
        all_transversals.append(transversal[:])
    else:
        next_row = first_row + 1
        # if next_row == len(first_square):
        #     next_row = 0
        # else:
        column += 1
        for next_row in range(len(first_square)):
            if not visited[next_row] and first_square[next_row][column] not in transversal:
                findAllTrans(first_square, next_row, first_square[next_row][column], column)
    transversal.pop()
    visited[first_row] = False
    return all_transversals

print("grammi1:", findAllTrans(first_square,1,1,0))
#Call findAllTrans function setting as first_num the first number of each row.
def call():
    for i in range(0,len(first_square)):
        #findAllTrans(first_square, i, i, 0)
        return print(findAllTrans(first_square, i, i, 0))
print(call())

# ______STEP 2________
trans = {}
def group_trans(): #group transversals by first number. Store them in a dictionary named trans.
    for t in all_transversals:
        if t[0] not in trans:
            trans[t[0]] = [t]
        trans[t[0]].append(t)

#check if there are duplicates in a list
def check_lists(array):
    for i in range(len(array)):
        if any(array[i] == array[j] for j in range(i+1,len(array))):
            return False

#Trying to combine transversals in a latin square i have to be sure that there are no duplicates in the same
#row and column. Nonetheless, I only need to check columns bcs transversal's row do not have duplicates.
def check_columns(new_array):
    for i in range(len(new_array[0])): #for each column
        if check_lists([column[i] for column in new_array]):
          return False
    return True

#Create an array of non disjoint transversals so that they create a latin square.
disjoint_array = []
disjoint = []
group_trans()

def disjoint_transversals(i):
    for j in range(len(trans[i])):
        disjoint.append(trans[i][j])
        if i == len(trans) - 1:
            if check_columns(disjoint):
                disjoint_array.append(disjoint[:])
            else:
                disjoint_transversals(i+1)
                if disjoint_array == True:
                    return disjoint_array
    disjoint.pop()
disjoint_transversals(0)

# ______STEP 3________

new_square= []
def replace_nums():
    for i in range(len(disjoint_transversals)):
        for j in range(len(disjoint_transversals[i])):
            row = disjoint_transversals[i][j]
            column = j
            new_square[row][column] = i
    return new_square
print(replace_nums)


# ______OUTPUT________
start = timeit.default_timer()

gr_la_square = []
for i in range(len(first_square)):
    gr_la_square.append([])
    for j in range(len(first_square[i])):
        gr_la_square[i].append((first_square[i][j], new_square[i][j]))

print("Greco_Latin square:", gr_la_square)


