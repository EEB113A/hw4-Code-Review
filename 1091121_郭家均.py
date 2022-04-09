def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    Matrix=input_matrix #傳入矩陣
    size=len(Matrix) #計算矩陣長度
    A=[None]*((1+size)*size//2) #設定A矩陣的長度
    index=0 



    if Major=="r": #如果是 row-major
        if  Matrix[0][0]==0 and Matrix[0][1]==0 and Matrix[1][0]==0:    #右下三角矩陣的判斷式
            a=size-1
            for i in range(size): #利用迴圈把右下三角矩陣處理成row-major的形式
                for j in range(a,size):
                    A[index]=Matrix[i][j]
                    index+=1
                a-=1
                
    
    
        if  Matrix[size-1][0]==0 and Matrix[size-1][1]==0 and Matrix[size-2][0]==0: #右上三角矩陣的判斷式
            for i in range(size):#利用迴圈把右上三角矩陣處理成row-major的形式
                for j in range(i,size):
                    A[index]=Matrix[i][j]
                    index+=1
   

        if  Matrix[size-1][size-1]==0 and Matrix[size-1][size-2]==0 and Matrix[size-2][size-1]==0: #左上三角矩陣的判斷式
            for i in range(size): #利用迴圈把左上三角矩陣處理成row-major的形式
                for j in range(0,size):
                    A[index]=Matrix[i][j]
                    index+=1
                size-=1


        if  Matrix[0][size-1]==0 and Matrix[0][size-2]==0 and Matrix[1][size-1]==0: #左下三角矩陣的判斷式
            for i in range(size):   #利用迴圈把左下三角矩陣處理成row-major的形式
                for j in range(0, i+1):
                    A[index]=Matrix[i][j]
                    index += 1


    if Major=="c": #如果式 column-major
        if  Matrix[size-1][size-1]==0 and Matrix[size-1][size-2]==0 and Matrix[size-2][size-1]==0:  #左上三角矩陣的判斷式             
            for i in range(size):   #利用迴圈把左上三角矩陣處理成column-major的形式
                for j in range(size):
                    A[index]=Matrix[j][i]
                    index += 1
                size-=1

    
        if  Matrix[0][size-1]==0 and Matrix[0][size-2]==0 and Matrix[1][size-1]==0: #左下三角矩陣的判斷式
            a=0
            for i in range(size): #利用迴圈把左下三角矩陣處理成column-major的形式
                for j in range(a,size):
                    A[index]=Matrix[j][i]
                    index += 1
                a+=1


        if  Matrix[0][0]==0 and Matrix[0][1]==0 and Matrix[1][0]==0:  #右下三角矩陣的判斷式
            b=size-1
            for i in range(size): #利用迴圈把右下三角矩陣處理成column-major的形式
                for j in range(b,size):
                    A[index]=Matrix[j][i]
                    index += 1
                b-=1


        if  Matrix[size-1][0]==0 and Matrix[size-1][1]==0 and Matrix[size-2][0]==0:  #右上三角矩陣的判斷式
            c=1
            for i in range(size): #利用迴圈把右上三角矩陣處理成column-major的形式
                for j in range(c):
                    A[index]=Matrix[j][i]
                    index += 1
                c+=1

      

    return A # 回傳值型態:list #回傳A矩陣

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