def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size =len (Matrix)
    matrix=[None]*((1+size)*size//2)

    right_up =True                                          #判斷是否為由右上三角形
    for i in range (1,size):
        for j in range(0,i):
            if Matrix[i][j]!=0:
                right_up=False
            else:
                right_up=True
    if right_up==True:
        if Major =="r":                                      #右上r
            index=0
            for i in range (size):
                for j in range(i,size):
                    matrix[index]=Matrix[i][j]
                    index += 1
        if Major =="c":                                      #右上 c
            index=0
            for j in range(size):
                for i in range (0,j+1):
                    matrix[index]=Matrix[i][j]
                    index += 1
        return matrix
    
    right_down =True                                          #判斷是否為由右下三角形
    for i in range (size):
        for j in range(0,size-1-i):
            if Matrix[i][j]!=0:
                right_down=False
            else:
                right_down=True
    if right_down==True:
        if Major =="r":                                      #右下r
            index=0
            for i in range (size):
                for j in range(size-1-i,size):
                    matrix[index]=Matrix[i][j]
                    index += 1
        if Major =="c":                                      #右下 c
            index=0
            for j in range(size):
                for i in range (size-1-j,size):
                    matrix[index]=Matrix[i][j]
                    index += 1
        return matrix
    
    left_up =True                                          #判斷是否為由左上三角形
    for i in range (1,size):
        for j in range(size-i,size):
            if Matrix[i][j]!=0:
                left_up=False
            else:
                left_up=True
    if left_up==True:
        if Major =="r":                                      #左上r
            index=0
            for i in range (size):
                for j in range(0,size-i):
                    matrix[index]=Matrix[i][j]
                    index += 1
        if Major =="c":                                      #左上 c
            index=0
            for j in range(size):
                for i in range (0,size-j):
                    matrix[index]=Matrix[i][j]
                    index += 1
        return matrix
    
    left_down =True                                          #判斷是否為由左下三角形
    for i in range (size):
        for j in range(i+1,size):
            if Matrix[i][j]!=0:
                left_down=False
            else:
                left_down=True
    if left_down==True:
        if Major =="r":                                      #左下r
            index=0
            for i in range (size):
                for j in range(0,i+1):
                    matrix[index]=Matrix[i][j]
                    index += 1
        if Major =="c":                                      #左下 c
            index=0
            for j in range(size):
                for i in range (j,size):
                    matrix[index]=Matrix[i][j]
                    index += 1
        return matrix
    

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