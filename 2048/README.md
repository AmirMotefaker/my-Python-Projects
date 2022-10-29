# 2048 game

>> xplanation:

 We have defined two classes in the code:

## 1. Board:

  Variables:

    Bg_color: It is a dictionary that stores background color for every cell.

    Color: It is a dictionary that stores foreground color for every cell.
    
    Window: It is the main tkinter window.
    
    gameArea: It is a tkinter frame widget.
    
    gridCell: It is a 4×4 integer matrix which stores the actual integer value of all the cells.
    
    Board: It is a 4×4 grid of tkinter label widget which displays the value of the cell on tkinter window. It is also used to configure the background and foreground     of the cell according to its gridCell value.
    
    Score: It stores the current score of the player.
    
    Rest are just flag variables.

  Functions:

    __init__(self): It is the constructor function. It initializes all the variables with appropriate default values like ‘0’ for gridCell, False for moved, merge and     so on.
    
    Reverse: It reverse the gridCell matrix.
    
    Transpose: It uses zip function and takes transpose of the gridCell matrix.
    
    CompressGrid: It moves all not empty cells to the left, so that merging can be done easily.
    
    mergeGrid: It adds the gridCell value of two adjacent cells if they have same gridCell values.
    
    Random_cell: It first stores all the empty cells in a list and then picks a random cell from the created list and make its gridCell value 2
    
    Can_merge: It returns a boolean value denoting we can merge any two cells or not. We can merge two cells if and only if they hold the same gridCell value.
    
    paintGrid: It assigns foreground and background color to each cell of the 4×4 grid corresponding to its gridCell value.
    


## 2. Game:

 This class doesn’t have many variables, it only has some Boolean variables indicating game status.

  Functions:

    __init__(self): It is the constructor function. It initializes all the variables with appropriate default values.
    
    start: It calls random_cell twice to assign ‘2’ to gridCell value of two random cells and then it paints the grid and after that, it calls link_keys to link up, down, left, and right keys.
    
    Link_keys: First of all it checks if the game is already won or lost, and if it is, it executes a return statement without doing anything. Otherwise, it continues its execution.
    
# Approach:

    1- For left swipe, we will just compress and then merge the gridCell matrix and then if compress or merge is true (indicating the values of the matrix is affected by previous two functions), then we need to compress the grid again.
    
    2- For moving up, we will take transpose then swipe left and again take transpose to return to the original order.
    
    3- Moving down is same as moving up but we need to reverse the matrix.
    
    4- Similarly, right is same as moving left+reverse.
    
    5- After every operation, we need to check the game status, if all cells are occupied and we cannot even merge any two cells i.e. the state where no movement can change the matrix, then the game is over.
    
    6- If any cell value has reached 2048, then the player is won and a message box is flashed on the screen announcing the winner.
