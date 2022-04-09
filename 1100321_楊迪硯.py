def to_1D_array(Matrix, Major): 
    
    size = len(Matrix)
    B=[None]*((1+size)*size//2)#創造新的矩陣

    ld=0
    for i in range(1,size):
        for j in range(0,i):
            ld += Matrix[i][j]
#判斷是否為左下三角矩陣
    rd=0
    for i in range(1,size):
        for j in range(size-i,size):
            rd += Matrix[i][j]
#判斷是否為右下三角矩陣
    ru=0
    for i in range(size):
        for j in range(i+1,size):
            ru += Matrix[i][j]
#判斷是否為左上三角矩陣
    lu=0
    for i in range(size):
        for j in range(0,size-i-1):
            lu += Matrix[i][j]
#判斷是否為右上三角矩陣
#壓縮
    if Major == "r":
        #右上
        if ld==0:
            index = 0
            for i in range(size):
                for j in range(i,size):
                    B[index]=Matrix[i][j]
                    index+=1
            return B
        #左上
        if rd==0:
            index = 0
            for i in range(size):
                for j in range(0,size-1):
                    B[index]=Matrix[i][j]
                    index+=1
            return B
        #左下
        if ru==0:
            index = 0
            for i in range(size):
                for j in range(0,i+1):
                    B[index]=Matrix[i][j]
                    index+=1
                    
            return B
        #右下
        if lu==0:
            index = 0
            for i in range(size):
                for j in range(size-1-i,size):
                    B[index]=Matrix[i][j]
                    index+=1
            return B
#壓縮
    if Major == "c":
        #右上
        if ld==0:
            index = 0
            for i in range(size):
                for j in range(0,i+1):
                    B[index]=Matrix[j][i]
                    index+=1
            return B
        #左上
        if rd==0:
            index = 0
            for i in range(size):
                for j in range(0,size-1):
                    B[index]=Matrix[j][i]
                    index+=1
            return B
        #左下
        if lu==0:
            index = 0
            for i in range(size):
                for j in range(i,size):
                    B[index]=Matrix[j][i]
                    index+=1
            return B
        #右下
        if ru==0:
            index = 0
            for i in range(size):
                for j in range(size-1-i,size):
                    B[index]=Matrix[j][i]
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