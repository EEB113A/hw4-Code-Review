def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    flat_list = []

    for row in range(0, len(Matrix)): #判定左下
        for col in range(row + 1, len(Matrix)):
            if(Matrix[row][col] != 0):
                break
            else:                  
                if Major == "r":
                    for row in range(0, len(Matrix)):
                        for col in range(0, row+1):
                            flat_list.append(Matrix[row][col])
                    return flat_list

    for row in range(1, len(Matrix)): #判定右上
        for col in range(0, row):
            if(Matrix[row][col] != 0): 
                break
            else:
                if (Major == "r"):
                    for row in range(0, len(Matrix)):
                        for col in range(row , len(Matrix)):
                            flat_list.append(Matrix[row][col])
                    return flat_list

    for row in range(1, len(Matrix)): #判定右下
        for col in range(0, row):
            if(Matrix[len(Matrix)-row-1][col] != 0):
                break
            else:
                if (Major == "c"):
                    for col in range(0, len(Matrix)):
                         for row in range(col+1, 0, -1):
                            flat_list.append(Matrix[len(Matrix)-row][col])
                    return flat_list

    for row in range(0, len(Matrix)): #判定左上
        for col in range(row+1, len(Matrix)):
            if(Matrix[len(Matrix)-row-1][col] != 0):
                break
            else:
                if (Major == "c"):
                    for row in range(0, 4):
                        for col in range(0, len(Matrix)-row):
                            flat_list.append(Matrix[col][row])   
                    return flat_list 
if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]





    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板