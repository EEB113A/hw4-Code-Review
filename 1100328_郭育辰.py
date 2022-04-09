def to_1D_array(Matrix, Major):
    if len(Matrix) != len(Matrix[0]):
        return None
    n=len(Matrix)
    flag_LU=True
    flag_RD=True
    flag_RU=True
    flag_LD=True
    for y in range(1,n):
        for x in range(y):
            if Matrix[y][n-1-x]!=0:  
                flag_LU=False #not a 左上 triangle matrix
                break
        if not flag_LU:
            break
        
    for y in range(n-1):
        for x in range(n-1-y):
            if Matrix[y][x]!=0:
                flag_RD=False #not a 右下 triangle matrix
                break
        if not flag_RD:
            break
        
    for y in range(1,n):
        for x in range(y):
            if Matrix[y][x]!=0:  
                flag_RU=False #not a 右上 triangle matrix
                break
        if not flag_RU:
            break
        
    for y in range(n-1):
        for x in range(n-1-y):
            if Matrix[y][n-1-x]!=0:  
                flag_LD=False #not a 左下 triangle matrix
                break
        if not flag_LD:
            break
    
    if (flag_LU and flag_RD) or (flag_RU and flag_LD):#如果以上皆非
        return None #not a triangle matrix
    if not flag_LU and not flag_RU and not flag_LD and not flag_RD:
        return None #not a triangle matrix
    A=[]
    
 
    
    
    if flag_LU:#左上
        if Major=="c":
            for x in range(n):
                for y in range(n-x):
                    A.append(Matrix[y][x])
        else:
            for y in range(n):
                for x in range(n-y):
                    A.append(Matrix[y][x])
        return A
    elif flag_RU:#右上
        if Major=="c":
            for x in range(n):
                for y in range(x+1):
                    A.append(Matrix[y][x])
        else:
            for y in range(n):
                for x in range(y,n):
                    A.append(Matrix[y][x])
        return A
    elif flag_LD:#左下
        if Major=="c":
            for x in range(n):
                for y in range(x,n):
                    A.append(Matrix[y][x])
        else:
            for y in range(n):
                for x in range(y+1):
                    A.append(Matrix[y][x])
        return A
    else:#右下
        if Major=="c":
            for x in range(n):
                for y in range(n-x-1,n):
                    A.append(Matrix[y][x])
        else:
            for y in range(n):
                for x in range(n-y-1,n):
                    A.append(Matrix[y][x])
        return A

A=[[1,0,0,0,0],#左下三的實驗
   [0,1,0,0,0],
   [0,0,1,0,0],
   [0,0,0,1,0],
   [3,0,0,0,1]]



print(to_1D_array(A,"c"))
print(to_1D_array(A,"r"))



if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,1,1,1],
                    [8,3,2,0],
                    [4,4,0,0],
                    [9,0,0,0]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)



#留言板