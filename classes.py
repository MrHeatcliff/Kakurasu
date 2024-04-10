class cell:
    def __init__(self):
        self.rowValue = 0
        self.colValue = 0
        self.tick = 0
        self.available = True
        
    def set_value(self, rowValue, colValue):
        self.rowValue = rowValue
        self.colValue = colValue
    
    def get_tick(self):
        return self.tick
    
    def get_row_value(self):
        return self.rowValue

    def get_col_value(self):
        return self.colValue
    
    def un_available(self):
        self.available = False

    def ticked(self):
        self.tick = 1

class board:
    def __init__(self):
        self.board = [[cell() for i in range(4)] for j in range(4)]
        self.rowSum = [0 for i in range(4)]
        self.colSum = [0 for i in range(4)]
        self.curRowSum = [0 for i in range(4)]
        self.curColSum = [0 for i in range (4)]
    
    def __init__(self, size):
        self.board = [[cell() for i in range(size)] for j in range(size)]
        self.rowSum = [0 for i in range(size)]
        self.colSum = [0 for i in range(size)]
        self.curRowSum = [0 for i in range(size)]
        self.curColSum = [0 for i in range (size)]
        # self.set_sum(size)
        self.set_cell_value(size)

    def set_sum(self, size):
        str = (input("nhap cac gia tri cua hang: ")).split(" ")
        self.rowSum = [int(a) for a in str]
        str = (input("nhap cac gia tri cua cot: ")).split(" ")
        self.colSum = [int(a) for a in str]

    def set_sum(self, rowSum, colSum):
        self.rowSum = rowSum
        self.colSum = colSum

    def set_cell_value(self, size):
        for i in range(size):
            for j in range(size):
                self.board[i][j].set_value(rowValue= j+1, colValue= i+1)

    def print_board(self):
        listboard=[n.get_tick() for a in self.board for n in a]
        print(" ", end="")
        for i in range(len(self.board)):
            print(" |", i + 1, end='')
        print(" | ")
        for i in range(len(self.board)):
            self.printLine(len(self.board))
            print(i+1, "|", end="")
            for j in range(len(self.board)):
                print("", listboard[i * len(self.board)+j], "|", end='')
            print("",self.rowSum[i],end='')
            print()
        self.printLine(len(self.board))
        print("  |", end='')
        for i in range(len(self.board)):
            print("", self.colSum[i], "|", end='')

    def printLine(self, n):
        for i in range((n+4)*3):
            print("-", end='')
        print()
