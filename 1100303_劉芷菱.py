def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    size = len(Matrix) 
    B = [None] * ((1 + size) * size // 2)
    index = 0
    ans = 0 #設一變數為0
            
    total = 0    #設一變數為0
    for i in range(size):
        for j in range(size-i-1): 
            if Matrix[i][j]!=0:  #判斷上左三角形是否皆為0
                total += 1   #若有任何一個數不為0，total加一
    if total == 0: 
        ans = 1   #若total為0，表示此matrix為下右三角形矩陣

    total = 0 #設一變數為0
    for i in range(size):
        for j in range(i+1,size): 
            if Matrix[i][j]!=0: #判斷上右三角形是否皆為0
                total += 1  #若有任何一個數不為0，total加一
    if total == 0:
        ans = 2   #若total為0，表示此matrix為下左三角形矩陣
         
    total = 0 #設一變數為0
    for i in range(size):
        for j in range(0,i):  
            if Matrix[i][j]!=0:  #判斷下左三角形是否皆為0
                total += 1  #若有任何一個數不為0，total加一
    if total == 0:
        ans = 3   #若total為0，表示此matrix為上右三角形矩陣

    total = 0 #設一變數為0
    for i in range(size):
        for j in range(-(i-size),size):  
            if Matrix[i][j]!=0:  #判斷下右三角形是否皆為0
                total += 1  #若有任何一個數不為0，total加一
    if total == 0:
        ans = 4   #若total為0，表示此matrix為上左三角形矩陣
    
    if ans == 1 and Major == "r": #若此matrix為下右三角形矩陣且為row-major
        for i in range(size):
            for j in range(-(i-size+1),size): #下右三角形矩陣
                B[index] = Matrix[i][j]
                index += 1
    elif ans == 2 and Major == "r":  #若此matrix為下左三角形矩陣且為row-major      
        for i in range(size):
            for j in range(0, i+1): #下左三角形矩陣
                B[index] = Matrix[i][j]
                index += 1
    elif ans == 3 and Major == "r":  #若此matrix為上右三角形矩陣且為row-major               
        for i in range(size):
            for j in range(i,size): #上右三角形矩陣
                B[index] = Matrix[i][j]
                index += 1
    elif ans == 4 and Major == "r":  #若此matrix為上左三角形矩陣且為row-major            
        for i in range(size):
            for j in range(size-i): #上左三角形矩陣
                B[index] = Matrix[i][j]
                index += 1
   

    if ans == 1 and Major == "c": #若此matrix為下右三角形矩陣且為column-major
        for i in range(size):
            for j in range(size-i-1,size): #下右三角形矩陣
                B[index] = Matrix[j][i]
                index += 1
    elif ans == 2 and Major == "c": #若此matrix為下左三角形矩陣且為column-major 
        for i in range(size):
            for j in range(i,size): #下左三角形矩陣
                B[index] = Matrix[j][i]
                index += 1
        
    elif ans == 3 and Major == "c": #若此matrix為上右三角形矩陣且為column-major              
        for i in range(size):
            for j in range(i+1): #上右三角形矩陣
                B[index] = Matrix[j][i]
                index += 1 
            
    elif ans == 4 and Major == "c": #若此matrix為上左三角形矩陣且為column-major         
        for i in range(size):
            for j in range(size-i): #上左三角形矩陣
                B[index] = Matrix[j][i]
                index += 1
    return B  #回傳壓縮完的一維陣列

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =  [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板