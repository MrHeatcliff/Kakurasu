import time

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
                self.board[i][j].set_value(rowValue= j+1, colValue= i+1)

    def ticked(self, index):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if count == index:
                    self.board[i][j].ticked()
                    return
                count += 1

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

    def dfs_solve(self):
        self.__backtrack(self.rowSum, self.colSum)

    def __backtrack(self, rowSum, colSum):
        candiRow = []
        for i in range (self.size):
            result = []
            self.__get_val(self.initRow, 0, 0, self.rowSum[i], result)
            candiRow.append(result)
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
