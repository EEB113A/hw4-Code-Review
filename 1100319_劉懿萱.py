def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    size = len(Matrix)
    B = [None] * ((1 + size) * size // 2)      
    
    
    flag=1                                      #先假設輸入之三角形矩陣為此方向
    for i in range (size-1) :                   #檢查應全為0的小三角形是否全為0
        for j in range (size-i-1 ):
            if Matrix[i][j]!=0:                 #若有不為0的數 
                flag=0
                break                           #則不是此方向的三角形矩陣
        
        if  flag==0 : 
            break    
                  
        if Major=="r":                          #右下三角 列
            index = 0
            for i in range(size):
                for j in range(size-i-1,size):
                    B[index] = Matrix[i][j]
                    index += 1                                        
            return list(B)                      #回傳值為list型態
            
        if Major=="c":                          #右下三角 行
            index = 0
            for j in range(size):
                for i in range(size-j-1,size):        
                    B[index] = Matrix[i][j]
                    index += 1                        
            return list(B)
    
    flag=1
    for i in range (size):
        for j in range (i+1,size):
            if Matrix[i][j]!=0: 
                flag=0 
                break
        
        if  flag==0 : 
            break
                                    
        if Major=="r":                          #左下三角 列
            index = 0
            for i in range(size):         
                for j in range(i+1):
                    B[index] = Matrix[i][j]
                    index += 1                                    
            return list(B)                   

        if Major=="c":                          #左下三角 行
            index = 0
            for j in range(size):
                for i in range(j,size):        
                    B[index] = Matrix[i][j]
                    index += 1                        
            return list(B)

    
    flag=1
    for i in range (1,size)  :         
        for j in range (i):             
            if Matrix[i][j]!=0: 
                flag=0
                break
          
        if  flag==0 : 
            break
                     
        if Major=="r":                          #右上三角 列
            index = 0
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[i][j]
                    index += 1                        
            return list(B)
        
        if Major=="c":                          #右上三角 行
            index = 0
            for j in range(size):
                for i in range(j+1):        
                    B[index] = Matrix[i][j]
                    index += 1                       
            return list(B)
   
    flag=1
    for i in range (1,size)  :        
        for j in range (size-i,size):                            
            if Matrix[i][j]!=0: 
                flag=0
                break
        
        if  flag==0 : 
            break
                   
        if Major=="r":                          #左上三角 列
            index = 0
            for i in range(size):
                for j in range(size-i):
                    B[index] = Matrix[i][j]
                    index += 1                        
            return list(B)                  
        
        if Major=="c":                          #左上三角 行
            index = 0
            for j in range(size):
                for i in range(size-j):        
                    B[index] = Matrix[i][j]
                    index += 1                         
            return list(B)                                 

               
   
     
if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =   [[0,5,2,0],
                      [0,0,3,1],
                      [0,0,0,7],
                      [0,0,0,0]]





    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板