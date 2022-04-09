def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    Inputmatrix=Matrix # 先建立變數
    checkmajor=Major
    size =len(Inputmatrix) # 抓個長度
    a=0 # 判斷值=>右下
    b=0 # 判斷值=>右上
    c=0 # 判斷值=>左下
    d=0 # 判斷值=>右下

    New_matrix=[None]*((1+size)*size//2)
    for i in range(size): # 把a設為右下三角
        for j in range(size-i-1):
            a=a+Inputmatrix[i][j] 
    for i in range(size): # 把b設為左下三角
        for j in range(i+1,size):
            b=b+Inputmatrix[i][j] 
    for j in range(1,size): # 把c設為左上三角
        for i in range(size-1,size-j-1,-1):
            c=c+Inputmatrix[i][j] 
    for j in range(0,size): # 把d設為右上三角
        for i in range(size-1,j):
            d=d+Inputmatrix[i][j] 
    
    #判斷三角
    if a==0:
        mod=1 
    elif b==0:
        mod=2 
    elif c==0:
        mod=3 
    else:
        mod=4 
    
    #判別如果是哪種三角，且是row or column時，來處理: 'r'=>看列，'c'=>看行
    if mod ==1 and checkmajor=='r': #右下
        index=0
        for i in range(size):
            for j in range(size-1-i,size):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==2 and checkmajor=='r': #左下
        index=0
        for i in range(size):
            for j in range(0,i+1):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==3 and checkmajor=='r': #左上
        index=0
        for i in range(size):
            for j in range(0,size-i):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==4 and checkmajor=='r': #右上
        index=0
        for i in range(size):
            for j in range(i,size):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==1 and checkmajor=='c': #右下
        index=0
        for j in range(size):
            for i in range(size-1-j,size):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==2 and checkmajor=='c': #左下
        index=0
        for j in range(size):
            for i in range(j,size):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==3 and checkmajor=='c': #左上
        index=0
        for j in range(size):
            for i in range(0,size-j):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
    if mod ==4 and checkmajor=='c': #右上
        index=0
        for j in range(size):
            for i in range(0,j+1):
                New_matrix[index]=Inputmatrix[i][j]
                index+=1
       
    return  New_matrix# 回傳值型態:list

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