# Tic Tac Toe Game
def sum(a, b, c):
    return a + b + c

def printBoard(xState, oState):
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four = 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six = 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)
    
    print(f"  {zero}  |  {one}  |  {two}")
    print("-----|-----|-------")
    print(f"  {three}  |  {four}  |  {five}")
    print("-----|-----|-------")
    print(f"  {six}  |  {seven}  |  {eight}")
    
def checkWinner(xState, oState):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            printBoard(xState, oState)
            print("X wins!")
            return 1
        elif sum(oState[win[0]], oState[win[1]], oState[win[2]]) == 3:
            printBoard(xState, oState)
            print("O wins!")
            return 0
    
    return -1
            

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    oState = [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 is for X chance and 0 is for O chance
    print("---------Welcome to Tic Tac Toe Game-----------")
    
    while(True):
        printBoard(xState, oState)
        if turn == 1:
            print("X Turn:->>>>")
            val = int(input("Enter the value:- "))
            if xState[val] == 0 and oState[val] == 0:
                xState[val] = 1
            else:
                print("Cell already occupied, try a different move.")
                continue
        else:
            print("O Turn:->>>>")
            val = int(input("Enter the value:- "))
            if xState[val] == 0 and oState[val] == 0:
                oState[val] = 1
            else:
                print("Cell already occupied, try a different move.")
                continue
            
        # Check for Winner
        winner = checkWinner(xState, oState)
        if winner != -1:
            print("Game over!")
            break
    
        # check for draw
        if all(xState[i] == 1 or oState[i] == 1 for i in range(9)):
            printBoard(xState,oState)
            print("Both Loss, Game is Draw!")
            print("Game over!")
            break
        
        # switch turn
        turn = 1 - turn