def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    output_list = []
    size = len(Matrix)
    if Major == "r":    #判斷為"r"
        if Matrix[0][:-1] == [0] * (size - 1) and Matrix[1][:-2] == [0] * (size - 2):    #判斷為右下三角形矩陣
            for i in range(size):
                output_list += Matrix[i][-1-i:]
        elif Matrix[0][1:] == [0] * (size - 1) and Matrix[1][2:] == [0] * (size - 2):    #判斷為左下三角形矩陣
            for i in range(size):
                output_list += Matrix[i][:i+1]
        elif Matrix[-1][:-1] == [0] * (size - 1) and Matrix[-2][:-2] == [0] * (size - 2):    #判斷為右上三角形矩陣
            for i in range(size):
                output_list += Matrix[i][i:]
        elif Matrix[-1][1:] == [0] * (size - 1) and Matrix[-2][2:] == [0] * (size - 2):    #判斷為左上三角形矩陣
            for i in range(size):
                output_list += Matrix[i][:size-i]
    elif Major == "c":    #判斷為"c"
        if Matrix[0][:-1] == [0] * (size - 1) and Matrix[1][:-2] == [0] * (size - 2):    #判斷為右下三角形矩陣
            for i in range(size):
                for j in range(size-i-1,size):
                    output_list.append(Matrix[j][i])
        elif Matrix[0][1:] == [0] * (size - 1) and Matrix[1][2:] == [0] * (size - 2):    #判斷為左下三角形矩陣
            for i in range(size):
                for j in range(i,size):
                    output_list.append(Matrix[j][i])
        elif Matrix[-1][:-1] == [0] * (size - 1) and Matrix[-2][:-2] == [0] * (size - 2):    #判斷為右上三角形矩陣
            for i in range(size):
                for j in range(i+1):
                    output_list.append(Matrix[j][i])
        elif Matrix[-1][1:] == [0] * (size - 1) and Matrix[-2][2:] == [0] * (size - 2):    #判斷為左上三角形矩陣
            for i in range(size):
                for j in range(size-i):
                    output_list.append(Matrix[j][i])
    return output_list# 回傳值型態:list

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