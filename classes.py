import time

stack = []

class cell:
    def __init__(self):
        self.rowValue = 0
        self.colValue = 0
        self.tick = 0
        self.available = True
        self.hValue = 0
        
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
    
    def get_available(self):
        return self.available

    def set_h_value(self,value):
        self.hValue = value

    def get_h_value(self):
        return self.hValue

    def ticked(self):
        self.tick = 1

class board:
    def __init__(self):
        self.size = 4
        self.board = [[cell() for i in range(4)] for j in range(4)]
        self.rowSum = [0 for i in range(4)]
        self.colSum = [0 for i in range(4)]
        self.curRowSum = [0 for i in range(4)]
        self.curColSum = [0 for i in range (4)]
        self.initRow = [0 for i in range(4)]
    
    def __init__(self, size):
        self.size = size
        self.board = [[cell() for i in range(size)] for j in range(size)]
        self.rowSum = [0 for i in range(size)]
        self.colSum = [0 for i in range(size)]
        self.curRowSum = [0 for i in range(size)]
        self.curColSum = [0 for i in range (size)]
        self.initRow = [0 for i in range(size)]
        self.valueRow = [i+1 for i in range(size)]
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
                self.board[i][j].set_value(rowValue= i+1, colValue= j+1)

    def ticked(self, index):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if count == index:
                    self.board[i][j].ticked()
                    return
                count += 1

    def print_board(self):
        # listboard=[n.get_tick() for a in self.board for n in a]
        listboard=[n.get_available() for a in self.board for n in a]
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

    def __update_heuristic_value(self, i, j):
        if(self.board[i][j].get_available()):
            if(self.colSum[j] - (self.curColSum[j]+self.board[i][j].get_row_value()) < 0):
                for x in range(i, len(self.board[i])):
                    self.board[x][j].un_available()
                    self.board[x][j].set_h_value(999999)
                    return
            if((self.rowSum[i] - (self.curRowSum[i]+self.board[i][j].get_col_value())) < 0):
                for x in range(j, len(self.board[j])):
                    self.board[i][x].un_available()
                    self.board[i][x].set_h_value(99999)
                    return
            value = abs(self.colSum[j] - (self.curColSum[j]+self.board[i][j].get_row_value()))*abs(self.rowSum[i] - (self.curRowSum[i]+self.board[i][j].get_col_value()))
            self.board[i][j].set_h_value(value)
            if(abs(self.colSum[j] - (self.curColSum[j]+self.board[i][j].get_row_value())) == 0):
                for x in range(i+1, len(self.board[i])):
                    self.board[x][j].un_available()
                    self.board[x][j].set_h_value(999999)
                for x in range(0, i):
                    self.board[x][j].un_available()
                    self.board[x][j].set_h_value(999999)
            if(abs(self.rowSum[i] - (self.curRowSum[i]+self.board[i][j].get_col_value())) == 0):
                for x in range(j+1, len(self.board[j])):
                    self.board[i][x].un_available()
                    self.board[i][x].set_h_value(99999)
                for x in range(0, j):
                    self.board[i][x].un_available()
                    self.board[i][x].set_h_value(99999)
            

    def dfs_solve(self):
        self.__backtrack(self.rowSum, self.colSum)

    def __backtrack(self, rowSum, colSum):
        candiRow = []
        for i in range (self.size):
            result = []
            self.__get_val(self.initRow, 0, 0, self.rowSum[i], result)
            candiRow.append(result)
        print(candiRow)
        caseList = self.__RecursionFunc(candiRow[0], candiRow[1:])
        answ = []
        for ele in caseList:
            answ = ele
            if self.__checkCase(ele) == True:
                break
        if answ != []:
            count = 0
            for index in answ:
                if index == 1:
                    self.ticked(count)
                count += 1 

    def __get_val(self, x, i, has, val, result):
        if i > len(x) - 1 :
            return
        if has + self.valueRow[i] > val: 
            return
        if has + self.valueRow[i] == val:
            x[i] = 1
            result.append([])
            for j in range(len(x)):
                result[len(result) - 1].append(x[j])
            x[i] = 0
        x[i] = 1
        self.__get_val(x, i+1, has + self.valueRow[i], val, result)
        x[i] = 0
        self.__get_val(x, i+1, has, val, result)


    def __RecursionFunc(self, arr1, arrList):
        if (arrList):
            string = []
            for x in arr1:
                for y in arrList[0]:
                    string.append(x + y)
            result = self.__RecursionFunc(string, arrList[1:])
            return result
        else:
            return arr1
        
    def __checkCase(self, arr):
        listSumRow = [0 for i in range(self.size)]
        listSumCol = [0 for i in range(self.size)]
        point = 0
        for i in range(self.size):
            for j in range(self.size):
                if arr[point] == 1:
                    listSumRow[i] += j+1
                    listSumCol[j] += i+1
                point += 1
        if (listSumCol == self.colSum) & (listSumRow == self.rowSum):
            return True
        else: 
            return False
    
    def heuristic_solve(self):
        while(not self.__check_solve_board()):
            for i in range(self.size):
                for j in range(self.size):
                    self.__update_heuristic_value(i, j)
            self.__next_state()
            print(self.__check_solve_board())
            self.print_board()
        
    def __next_state(self):
        tickCell = self.__find_min_cell()
        tickCell.ticked()
        print()
        print(tickCell.get_row_value())
        print(tickCell.get_col_value())
        self.curColSum[tickCell.get_col_value()-1] += tickCell.get_row_value()
        self.curRowSum[tickCell.get_row_value()-1] += tickCell.get_col_value()
        tickCell.un_available()
        print(self.curColSum)
        print(self.curRowSum)
        return
    
    def __find_min_cell(self):
        ret_address = None
        min = 999999
        for i in self.board:
            for cell in i:
                if cell.get_available():
                    if cell.get_h_value() < min:
                        min = cell.get_h_value()
                        ret_address = cell
        if(ret_address != None):
            return ret_address
        else:
            return
        
    def __check_solve_board(self):
        if(self.curColSum == self.colSum) & (self.curRowSum == self.curRowSum):
            return True
        else:
            return False