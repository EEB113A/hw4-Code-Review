from ctypes import sizeof
from chardet import detect


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    matrix_size = len(Matrix)
    #判斷三角形矩陣類別
    matrix_type = detectMatrix(Matrix, matrix_size)
    oneDim_array = [] #1-Dimension array which will be returned
    #右下三角形矩陣壓縮
    if matrix_type=="downR" and Major=="r":
        [oneDim_array.extend(Matrix[y][-(1+y):]) for y in range(matrix_size)]
    elif matrix_type=="downR" and Major=="c":
        # for x in range(matrix_size):
        #     for y in range(-(x+1), 0):
        #         oneDim_array.append(Matrix[y][x])
        # 等同上方巢狀for loop
        [[oneDim_array.append(Matrix[y][x]) for y in range(-(x+1), 0)] for x in range(matrix_size)]
    #左下三角形矩陣壓縮
    elif matrix_type=="downL" and Major=="r":
        [oneDim_array.extend(Matrix[y][:y+1]) for y in range(matrix_size)]
    elif matrix_type=="downL" and Major=="c":
        [[oneDim_array.append(Matrix[y][x]) for y in range(-(matrix_size-x), 0)] for x in range(matrix_size)]
    #右上三角形矩陣壓縮
    elif matrix_type=="upR" and Major=="r":
        [oneDim_array.extend(Matrix[y][y:]) for y in range(matrix_size)]
    elif matrix_type=="upR" and Major=="c":
        [[oneDim_array.append(Matrix[y][x]) for y in range(x+1)] for x in range(matrix_size)]
    #左上三角形矩陣壓縮
    elif matrix_type=="upL" and Major=="r":
        [oneDim_array.extend(Matrix[y][:matrix_size-y]) for y in range(matrix_size)]
    else:
        [[oneDim_array.append(Matrix[y][x]) for y in range(matrix_size-x)] for x in range(matrix_size)]
    #回傳資料
    return  oneDim_array# 回傳值型態:list

########-detectMatrix-####################################################
def detectMatrix(Matrix, n):
    #檢查是否為右下三角形矩陣
    if [Matrix[y][:n-y-1] for y in range(n-1)] == [[0]*(n-y-1) for y in range(n-1)]:
        return "downR"
    #檢查是否為左下三角形矩陣
    elif [Matrix[y][y+1:] for y in range(n-1)] == [[0]*(n-y-1) for y in range(n-1)]:
        return "downL"
    #檢查是否為右上三角形矩陣
    elif [Matrix[y][:y] for y in range(1,n)] == [[0]*(y) for y in range(1,n)]:
        return "upR"
    else:  #如果不為前三種
        return "upL"

########-Main-###############################################################
if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    # test Data
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    # input_matrix = [[1,2,3,4],
    #                 [5,6,7,0],
    #                 [8,9,0,0],
    #                 [0,0,0,0]]
    # input_matrix = [[7,0,0,0,0],
    #                 [8,3,0,0,0],
    #                 [4,6,5,0,0],
    #                 [2,5,6,7,0],
    #                 [0,4,2,8,9]]
    # input_matrix = [[0,0,0,0,0,0],
    #                 [0,0,0,0,7,8],
    #                 [0,0,0,5,5,9],
    #                 [0,0,1,6,4,1],
    #                 [0,0,5,8,4,9],
    #                 [0,7,2,6,9,0]]
                    
    # input_matrix = [[0,5,2,0],
    #                 [0,0,3,1],
    #                 [0,0,0,7],
    #                 [0,0,0,0]]
    

    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板