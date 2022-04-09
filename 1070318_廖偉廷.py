def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    # 先設一個空list
    Matrix = []  
    size = len(Matrix)
    new_list = [None] * ((1 + size) * size // 2)
    Major = " "
    index = 0
    # 判斷為上三角形還是下三角形
    for i in range(size):
        for j in range(size):
            if i > j :
                if Major in "r" :
                    # 右上三角形
                    for i in range(size):
                        for j in range(i, size):
                            new_list[index] = Matrix[i][j]
                            index += 1
                elif Major in "c" :
                    # 左上三角形
                    for j in range(size):
                        for i in range(0, size-j):
                            new_list[index] = Matrix[i][j]
                            index += 1
            else:
                if Major in "r" :
                    # 左下三角形
                    for i in range(size):
                        for j in range(0, i+1):
                            new_list[index] = Matrix[i][j]
                            index += 1    
                elif Major in "c" :
                    # 右下三角形
                    for j in range(size):
                        for i in range(size-j-1, size):
                            new_list[index] = Matrix[i][j]
                            index += 1
    return Matrix # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板