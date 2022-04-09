def to_1D_array(Matrix, Major):
    Major = Major # Matrix型態:list[list]，Major型態:str
    a = len(Matrix)
    c = 0
    aa = True
    bb = True
    cc = True
    dd = True
    B = [None] * ((1 + a) * a // 2)
    while c<a-1:
        if list(set(Matrix[c][c+1:a]))==[0]:
            c+=1
        else:
            aa = False
            c+=1
    c =0
    while c<a-1:
        if list(set(Matrix[c][0:a-1-c]))==[0]:
            c+=1
        else:
            bb = False
            c+=1
    d = a-1
    c=0
    while d>1:
        
        if list(set(Matrix[d][c+1:a]))==[0]:
            c+=1
            d-=1
        else:
            d-=1
            cc = False
    d =a-1
    c=0
    while d>1:
        
        if list(set(Matrix[d][0:c+1]))==[0]:
            c+=1
            d-=1
        else:
            d-=1
            dd = False
    if aa:
        if Major =="r":
            index = 0
            for i in range(a):
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index += 1
        if Major =="c":
            index=0
            for j in range(a):
                for i in range(j,a):
                    B[index] = Matrix[i][j]
                    index +=1
    if bb:
        if Major =="r":
            index = 0
            for i in range(a):
                for j in range(a-1-i,a):
                    B[index] = Matrix[i][j]
                    index +=1
        if Major =="c":
            index = 0
            for j in range(a):
                for i in range(a-1-j,a):
                    B[index] = Matrix[i][j]
                    index +=1
    if cc:
        if Major == "r":
            index = 0
            for i in range(a):
                for j in range(0,a-i):
                    B[index] = Matrix[i][j]
                    index+=1
        if Major == "c":
            index = 0
            for j  in range(a):
                for i in range(0,a-j):
                    B[index] = Matrix[i][j]
                    index+=1
    if dd:
        index = 0
        if Major == "r":
            for i in range(a):
                for j in range(i,a):
                    B[index] = Matrix[i][j]
                    index+=1
        if Major =="c":
            for j in range(a):
                for i in range(0,j+1):
                    B[index] = Matrix[i][j]
                    index+=1
                    
        
            

            



    
    
    
        

                
            

        
    
    return B

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]
                    
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板