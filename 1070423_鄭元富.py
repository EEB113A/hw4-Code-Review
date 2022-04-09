def to_1D_array(Matrix, Major):  # Matrix型態:list[list]，Major型態:str
    output_list = []
    size = len(Matrix)

    # 以 row 去壓縮
    if Major == "r":

        # 右下三角形矩陣情況
        if Matrix[0][:-1] == [0] * (size - 1) and Matrix[1][:-2] == [0] * (size - 2):
            for i in range(size):
                output_list.append(Matrix[i][-1-i:])  # 新增第一列最後一個 data ，第二列最後兩個 data ...以次類推
        
        # 左下三角形矩陣情況
        elif Matrix[0][1:] == [0] * (size - 1) and Matrix[1][2:] == [0] * (size - 2):
            for i in range(size):
                output_list.append(Matrix[i][:i+1])  # 新增第一列第一個 data ，第二列第二個 data ...以次類推 

        # 右上三角形矩陣情況
        elif Matrix[-1][:-1] == [0] * (size - 1) and Matrix[-2][:-2] == [0] * (size - 2):
            for i in range(size):
                output_list.append(Matrix[i][i:])  # 新增第一列全部 data ，第二列除了第一個外全部 data ...以次類推 

        # 左上三角形矩陣情況
        elif Matrix[-1][1:] == [0] * (size - 1) and Matrix[-2][2:] == [0] * (size - 2):
            for i in range(size):
                output_list.append(Matrix[i][:size-i])  # 新增第一列全部 data ，第二列除了最後一個 data ...以次類推 
    
    # 以 column 去壓縮，因為 len 為矩陣 row 的維數，如果用 colume 去壓縮的話還需要去多一個迴圈去跑
    elif Major == "c":

        # 右下三角形矩陣情況
        if Matrix[0][:-1] == [0] * (size - 1) and Matrix[1][:-2] == [0] * (size - 2):
            for i in range(size):
                for j in range(size-i-1,size):
                    output_list.append(Matrix[j][i])

        # 左下三角形矩陣情況
        elif Matrix[0][1:] == [0] * (size - 1) and Matrix[1][2:] == [0] * (size - 2):
            for i in range(size):
                for j in range(i,size):
                    output_list.append(Matrix[j][i])

        # 右上三角形矩陣情況
        elif Matrix[-1][:-1] == [0] * (size - 1) and Matrix[-2][:-2] == [0] * (size - 2):
            for i in range(size):
                for j in range(i+1):
                    output_list.append(Matrix[j][i])

        # 左上三角形矩陣情況
        elif Matrix[-1][1:] == [0] * (size - 1) and Matrix[-2][2:] == [0] * (size - 2):
            for i in range(size):
                for j in range(size-i):
                    output_list.append(Matrix[j][i])
    return output_list  # 回傳值型態:list

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