def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    lst = []
    Matrix_x1_sum = sum(Matrix[0])
    Matrix_x2_sum = sum(Matrix[len(Matrix)-1])
    Matrix_y1_sum = 0
    Matrix_y2_sum = 0
    for i in range(len(Matrix)):
        Matrix_y1_sum += Matrix[i][0]
    for i in range(len(Matrix)):
        Matrix_y2_sum += Matrix[i][len(Matrix)-1]
    if  Matrix[0][0] == Matrix_x1_sum and  Matrix[0][len(Matrix)-1] == 0 and Matrix[len(Matrix)-1][len(Matrix)-1] == Matrix_y2_sum: #左下
        if Major == "c":
            for j in range(len(Matrix)):
                for i in range(j, len(Matrix)):
                    lst.append(Matrix[i][j])
        elif Major == "r":
            for i in range(len(Matrix)):
                for j in range(i+1):
                    lst.append(Matrix[i][j])
    elif Matrix[0][0] == 0 and Matrix[0][len(Matrix)-1] == Matrix_x2_sum and Matrix[len(Matrix)-1][0] == Matrix_y1_sum: #右下
        if Major == "c":
            for j in range(len(Matrix)):
                for i in range(len(Matrix)-j-1, len(Matrix)):
                    lst.append(Matrix[i][j])
        elif Major == "r":
            for i in range(len(Matrix)):
                for j in range(len(Matrix)-i-1, len(Matrix)):
                    lst.append(Matrix[i][j])
    elif Matrix[len(Matrix)-1][len(Matrix)-1] == 0 and Matrix[0][len(Matrix)-1] == Matrix_y2_sum and Matrix[0][len(Matrix)-1] == Matrix_x2_sum: #左上
        if Major == "c":
            for j in range(len(Matrix)):
                for i in range(len(Matrix)-j):
                    lst.append(Matrix[i][j])
        elif Major == "r":
            for i in range(len(Matrix)):
                for j in range(len(Matrix)-i):
                    lst.append(Matrix[i][j])
    elif Matrix[len(Matrix)-1][0] == 0 and Matrix[0][0] == Matrix_y1_sum and Matrix[len(Matrix)-1][len(Matrix)-1] == Matrix_x2_sum: #右上
        if Major == "c":
            for j in range(len(Matrix)):
                for i in range(j+1):
                    lst.append(Matrix[i][j])
        elif Major == "r":
            for i in range(len(Matrix)):
                for j in range(i,len(Matrix)):
                    lst.append(Matrix[i][j])

    #Matrix[0][0]     Matrix[0][len(Matrix)-1]     Matrix[len(Matrix)-1][0]          Matrix[len(Matrix)-1][len(Matrix)-1]
    # if Major == "c":
    #     Matrix = sort_by_column(Matrix)
    # elif Major == "r":
    #     Matrix = sort_by_row(Matrix)
    return lst# 回傳值型態:list

def sort_by_column(list):
    ret_lst = []
    for i in range(len(list)):
        ret_lst.append(list)

def sort_by_row(list):
    ret_lst = []
    for i in range(len(list)):
        ret_lst.append(list)

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