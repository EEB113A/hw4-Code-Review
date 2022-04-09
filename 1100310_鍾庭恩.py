def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    size = len(Matrix)
    B=[None]*((1+size)*size//2)
    #判斷三角形矩陣為左下三角形，左上三角形，右下三角形，右上三角形哪一個
    
    #左下三角形
    o=0
    for i in range(1,size):
        for j in range(0,i):
            o += Matrix[i][j]
    #右下三角形
    a=0
    for i in range(1,size):
        for j in range(size-i,size):
            a += Matrix[i][j]
    #右上三角形
    b=0
    for i in range(size):
        for j in range(i+1,size):
            b += Matrix[i][j]
    #左上三角形
    c=0
    for i in range(size):
        for j in range(0,size-i-1):
            c += Matrix[i][j]
    #Major 為r進行壓縮
    if Major == "r":
        #右上三角形
        if o==0:
            index = 0
            for i in range(size):
                for j in range(i,size):
                    B[index]=Matrix[i][j]
                    index+=1
            return B
        #左上三角形
        if a==0:
            index = 0
            for i in range(size):
                for j in range(0,size-1):
                    B[index]=Matrix[i][j]
                    index+=1
            return B
        #左下三角形
        if b==0:
            index = 0
            for i in range(size):
                for j in range(0,i+1):
                    B[index]=Matrix[i][j]
                    index+=1
            return B
        #右下三角形
        if c==0:
            index = 0
            for i in range(size):
                for j in range(size-1-i,size):
                    b[index]=Matrix[i][j]
                    index+=1
            return B
    #Major 為C進行壓縮
    if Major == "c":
        #右上三角形
        if o==0:
            index = 0
            for i in range(size):
                for j in range(0,i+1):
                    B[index]=Matrix[j][i]
                    index+=1
            return B
        #左上三角形
        if a==0:
            index = 0
            for i in range(size):
                for j in range(0,size-1):
                    B[index]=Matrix[j][i]
                    index+=1
            return B
        #左下三角形
        if b==0:
            index = 0
            for i in range(size):
                for j in range(i,size):
                    b[index]=Matrix[j][i]
                    index+=1
            return B
        #右下三角形
        if c==0:
            index = 0
            for i in range(size):
                for j in range(size-1-i,size):
                    b[index]=Matrix[j][i]
                    index+=1
            return B
    
    

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