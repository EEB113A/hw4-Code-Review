def to_1D_array(Matrix, Major): #Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    B = [None] * ((1 + size) * size // 2)

    sum = 0 
    for x in range(1,size):#計算右上三角形的總和
        for y in range(x-1):
            sum += Matrix[y][x]
    if sum == 0:  #如果右上三角形的總和=零，此為左下三角形
        if Major == 'r':
            index = 0
            for i in range(size):
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(j,size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B

    sum = 0
    for x in range(size-1):#計算左上三角形的總和
        for y in range(size-x-1):
            sum += Matrix[y][x]
    if sum==0:  #如果左上三角形的總和=零，此為右下三角形
        if Major == 'r':
            index = 0
            for i in range(size):
                for j in range(size-1-i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(size-j-1,size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B 

    sum = 0
    for y in range(1,size):#計算左下三角形的總和
        for x in range(y):
            sum += Matrix[y][x]
    if sum==0: #如果左下三角形的總和=零，此為右上三角形
        if Major == 'r':
            index = 0
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(j+1):
                    B[index] = Matrix[i][j]
                    index += 1
            return B 

    sum = 0
    for y in range(1,size):#計算右下三角形的總和
        for x in range(size-y,size):
            sum += Matrix[y][x]
    if sum==0: #如果右下三角形的總和=零，此為左上三角形
        if Major == 'r':
            index = 0
            for i in range(size):
                for j in range(size-i):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
        if Major == "c":
            index = 0
            for j in range(size):
                for i in range(size-j):
                    B[index] = Matrix[i][j]
                    index += 1
            return B
# 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0,0],
                    [8,3,0,0,0],
                    [4,6,5,0,0],
                    [2,5,6,7,0],
                    [0,4,2,8,9]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板