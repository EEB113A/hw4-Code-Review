def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix) #size是Matriz的長度
    B = [None] * ((1 + size) * size // 2) #先定義一個空的B矩陣

    if Major=='c':  #先判斷Major為'c'還是'r'
        if Matrix[0][size-1]==0 and Matrix[1][size-1]==0:  #這邊再做判斷為下左三角形矩陣
            index = 0   #先將index初始化
            for i in range(size):   #這邊將原先的Matrix的row從0到size,column從i到size放入B矩陣內
                for j in range(i,size):
                    B[index] = Matrix[j][i]
                    index += 1
        
        elif Matrix[0][0]==0 and Matrix[0][1]==0:          #這邊再做判斷為下右三角形矩陣
             index = 0  #先將index初始化
             for i in range(size):  #這邊將原先的Matrix的row從0到size,column從0到size-i-1放入B矩陣內    
                 for j in range(-(i+1),0):
                     B[index] = Matrix[j][i]
                     index += 1
        
        elif Matrix[size-1][size-1]==0 and Matrix[size-2][size-1]==0 and Matrix[0][0]!=0:   #這邊再做判斷為上左三角形矩陣
             index = 0  #先將index初始化
             for i in range(size):  #這邊將原先的Matrix的row從0到size,column從0到size-i放入B矩陣內
                 for j in range(0, size-i):
                     B[index] = Matrix[j][i]
                     index += 1

        elif Matrix[size-1][0]==0 and Matrix[size-1][1]==0 and Matrix[size-2][0]==0:        #這邊再做判斷為上右三角形矩陣
             index = 0  #先將index初始化
             for i in range(size):  #這邊將原先的Matrix的row從0到size,column從0到i+1放入B矩陣內
                 for j in range(0, i+1):
                     B[index] = Matrix[j][i]
                     index += 1


    elif Major=='r':
        if Matrix[0][size-1]==0 and Matrix[1][size-1]==0:       #這邊再做判斷為下左三角形矩陣
            index = 0   #先將index初始化
            for i in range(size):   #這邊將原先的Matrix的row從0到size,column從0到i+1放入B矩陣內
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index += 1
        
        elif Matrix[0][0]==0 and Matrix[0][1]==0:               #這邊再做判斷為下右三角形矩陣
             index = 0  #先將index初始化
             for i in range(size):  #這邊將原先的Matrix的row從0到size,column從0到size-i放入B矩陣內
                 for j in range(0,size-i):
                     B[-index] = Matrix[i][j]
                     index += 1

        
        elif Matrix[size-1][size-1]==0 and Matrix[size-2][size-1]==0 and Matrix[0][0]!=0:   #這邊再做判斷為上左三角形矩陣
             index = 0  #先將index初始化
             for i in range(size):  #這邊將原先的Matrix的row從0到size,column從0到size-i放入B矩陣內
                 for j in range(0, size-i):
                     B[index] = Matrix[i][j]
                     index += 1

            
        elif Matrix[size-1][0]==0 and Matrix[size-1][1]==0 and Matrix[size-2][0]==0:        #這邊再做判斷為上右三角形矩陣
             index = 0  #先將index初始化
             for i in range(size):  #這邊將原先的Matrix的row從0到size,column從i到size放入B矩陣內
                 for j in range(i, size):
                     B[index] = Matrix[i][j]
                     index += 1

    return B # 回傳值型態:list



if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0],
                    [0,0,8,9],
                    [0,5,6,7],
                    [1,2,3,4]]


    output_array = to_1D_array(input_matrix, "c")
    print(output_array)
                    

#留言板