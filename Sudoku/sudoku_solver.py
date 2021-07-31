board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]



def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo, num, pos):

    #Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #Check columnn
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def print_board(bo):

    for i in range(len(bo)):
        #After 3 rows will put an "-"
        if i % 3  == 0 and i != 0:
            print("- - - - - - - - - - -")

        #This will get the lenght of the row
        for j in range(len(bo[0])):
            #After 3 collumns will put an "|"
            if j % 3 == 0 and j != 0:
                #The end="" makes so that it doesn't end with a \n so it doesn't change line (that would interfer in our code)
                print("| ", end="")

            #If we are in the last position, it will print a "\n" after the element and will change row for us
            if j == 8:
                print(bo[i][j])
            #This will print the elements
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i,j) #row, collumn

    return None

answer = input("Hi there! You need some help solving your sudoku? ")

if answer.lower() == "yes":
    print("Glad you came looking for me then!\nHere I'll show you the look of our sudoku table.\n")
    print_board(board)
elif answer.lower() =="no":
    print("Goodbye then!")
    k=input("press any key to exit") 
    quit()

def replace_board(bo,r,c,n):

    bo[r-1][c-1]=n
    #print_board(board)
    return None


print("\nPlease enter the row, the column and the number you want to be in that spot(or 0 0 0 to solve it):")
while True:

    r, c, n = input("").split()
    r = int(r)
    c = int(c)
    n = int(n)

    if r == 0 and c == 0 and n == 0:
        break
    else:
        replace_board(board, r, c, n)
    
    
print_board(board)
user_input = input("\nYou want me to solve it for you? ")
if user_input.lower() == "yes":
    solve(board)
    print_board(board)
'''print_board(board)
solve(board)
print("_____________________")
print_board(board)'''

#This keeps the program open to see the output
k=input("\npress any key to exit") 