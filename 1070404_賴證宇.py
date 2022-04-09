def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    inputmatrix=Matrix
    checkmajor=Major
    size =len(inputmatrix)
    a=0 #右下判斷值
    b=0 #右上判斷
    c=0 #左下判斷
    d=0 #右下判斷

    New_matrix=[None]*((1+size)*size//2)
    for i in range(size):
        for j in range(size-i-1):
            a=a+inputmatrix[i][j] #a=右下三角
    for i in range(size):
        for j in range(i+1,size):
            b=b+inputmatrix[i][j] #b=0左下三角
    for j in range(1,size):
        for i in range(size-1,size-j-1,-1):
            c=c+inputmatrix[i][j] #c=0左上三角
    for j in range(0,size):
        for i in range(size-1,j):
            d=d+inputmatrix[i][j] #d=0右上三角
    
    if a==0:
        mod=1 #右下
    elif b==0:
        mod=2 #左下
    elif c==0:
        mod=3 #左上
    else:
        mod=4 #右上
    

    if mod ==1 and checkmajor=='r': #右下三角 且水平壓縮
        index=0
        for i in range(size):
            for j in range(size-1-i,size):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==2 and checkmajor=='r': #左下三角 且水平壓縮
        index=0
        for i in range(size):
            for j in range(0,i+1):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==3 and checkmajor=='r': #左上三角 且水平壓縮
        index=0
        for i in range(size):
            for j in range(0,size-i):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==4 and checkmajor=='r': #右上三角 且水平壓縮
        index=0
        for i in range(size):
            for j in range(i,size):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==1 and checkmajor=='c': #右下三角 且垂直壓縮
        index=0
        for j in range(size):
            for i in range(size-1-j,size):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==2 and checkmajor=='c': #左下三角 且垂直壓縮
        index=0
        for j in range(size):
            for i in range(j,size):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==3 and checkmajor=='c': #左上三角 且垂直壓縮
        index=0
        for j in range(size):
            for i in range(0,size-j):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
    if mod ==4 and checkmajor=='c': #右上三角 且垂直壓縮
        index=0
        for j in range(size):
            for i in range(0,j+1):
                New_matrix[index]=inputmatrix[i][j]
                index+=1
       
       



    

            


    
    return  New_matrix# 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =  [[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,4,0],
[0,0,3,0,0],
[0,0,0,0,0]]


    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板