from classes import *
import time

timeM = time.time()

if __name__ == "__main__":
    matrix = board(5)
    rowSum = [7, 9, 10, 9, 9]
    colSum = [5, 8, 12, 6, 11]
    matrix.set_sum(rowSum= rowSum, colSum= colSum)
    # matrix.dfs_solve()
    # matrix.print_board()
    # print("__________", time.time() - timeM)
    matrix.heuristic_solve()