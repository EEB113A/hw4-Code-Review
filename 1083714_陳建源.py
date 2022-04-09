def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    Matrix_length = len(Matrix) # 2D matrix 的長度
    tri_flat = [None] * ((1 + Matrix_length) * Matrix_length // 2) 
    index = 0
    for row in range(0,Matrix_length): # lower left triangle判斷
        for col in range(row + 1, Matrix_length):
            if(Matrix[row][col] != 0):
                break
            else:                  
                if Major == "r":#左右壓縮
                    for r in range(0, Matrix_length):
                        for c in range(0, r+1):
                             tri_flat[index] = Matrix[r][c]
                             index += 1
                    return  tri_flat

    for row in range(1, Matrix_length): # upper right triangle判斷
        for col in range(0, row):
            if(Matrix[row][col] != 0): 
                break
            else:
                if (Major == "r"):#左右壓縮
                    for r in range(0, Matrix_length):
                        for c in range(r , len(Matrix)):
                            tri_flat[index] = Matrix[r][c]
                            index += 1
                    return  tri_flat

    for row in range(1, Matrix_length): #lower right triangle判斷
        for col in range(0, row):
            if(Matrix[len(Matrix)-row-1][col] != 0):
                break
            else:
                if (Major == "c"):#上下壓縮
                    for c in range(0, Matrix_length):
                         for r in range(c+1, 0, -1):
                             tri_flat[index] = Matrix[Matrix_length-r][c]
                             index += 1
                    return  tri_flat

    for row in range(0, Matrix_length): #upper left triangle判斷
        for col in range(row+1, Matrix_length):
            if(Matrix[Matrix_length-row-1][col] != 0):
                break
            else:
                if (Major == "c"):#上下壓縮
                    for r in range(0, 4):
                        for c in range(0,Matrix_length-r):
                            tri_flat[index] = Matrix[c][r]
                            index += 1   
                    return  tri_flat

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[1,0,0,0],
                    [1,0,0,0],
                    [0,6,5,0],
                    [9,5,2,3]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板