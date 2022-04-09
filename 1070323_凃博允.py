from re import I



def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    flag=0 #判斷三角矩陣類型所需
    key=0  #將四種矩陣分類
    A=[]   
    for i in range(size):
        for j in range(size):
            if i>j:  #當列>行
                for x in range(size):
                    for y in range(size):
                    
                        if x>y and Matrix[x][y]!=0: #當列>行且有非0值
                            flag=1  #表示非右上三角矩陣
                                     
                if flag==0: #若flag仍是0，代表為右上三角矩陣
                    key=1   #將右上三角分類為第1種
                          
                else:
                    flag=0#將flag初始化，因為for loop會重複偵測，到最後的偵測結果才是真的，所以每次做完都要初始化
            elif i<j:   #當列<行
                for x in range(size):
                    for y in range(size):
                        if x<y and Matrix[x][y]!=0: #當列<行且有非0值
                            flag=1   #表示非左下三角矩陣
                if flag==0:          #若flag仍是0，代表為左下三角矩陣
                    key=2            #將左下三角分類為第2種
                else:
                    flag=0#將flag初始化，因為for loop會重複偵測，到最後的偵測結果才是真的，所以每次做完都要初始化
            elif (i+j)>(size-1): #當列與行的和小於size
                for x in range(i+1):
                    for y in range(j+1):
                        if (x+y)>(size-1)and Matrix[x][y]!=0: #當列與行的和小於size且有非0值
                            flag=1        #表示非左上三角矩陣
                if flag==0:#若flag仍是0，代表為左上三角矩陣
                    key=3  #將左下三角分類為第3種
                else:
                    flag=0#將flag初始化，因為for loop會重複偵測，到最後的偵測結果才是真的，所以每次做完都要初始化
            elif (i+j)<(size-1):
                for x in range(i+1):
                    for y in range(j+1):
                        if (x+y)<(size-1)and Matrix[x][y]!=0:
                            flag=1
                if flag==0:#若flag仍是0，代表為右下三角矩陣
                    key=4  #將左下三角分類為第4種
                else:
                    flag=0#將flag初始化，因為for loop會重複偵測，到最後的偵測結果才是真的，所以每次做完都要初始化  
    if key==1:
        print("右上三角矩陣")
    elif key==2:
        print("左下三角矩陣")
    elif key==3:
        print("左上三角矩陣")
    elif key==4:
        print("右下三角矩陣")
    if Major=="r": #要求Row Major
        if key==1: #代表為右上三角矩陣
            for i in range(size):
                for j in range(i,size):                                         
                    A.append(Matrix[i][j])    #2D Array to 1D Array      
        elif key==2:#代表為左下三角矩陣
            for i in range(size):
                for j in range(i+1):
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        elif key==3:#代表為左上三角矩陣
            for i in range(size):
                for j in range(size-i):
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        elif key==4:#代表為右下三角矩陣
            for i in range(size):
                for j in range(size-i-1,size):
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        print("Row Major")

                          
    if Major=="c": #要求Column Major
        if key==1:#代表為右上三角矩陣
            for j in range(size):
                for i in range(j+1):                                         
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        elif key==2:#代表為左下三角矩陣
            for j in range(size):
                for i in range(j,size):
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        elif key==3:#代表為左上三角矩陣
            for j in range(size):
                for i in range(size-j):
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        elif key==4:#代表為右下三角矩陣
            for j in range(size):
                for i in range(size-j-1,size):
                    A.append(Matrix[i][j])    #2D Array to 1D Array  
        print("Column Major")
               
                
    return A
            
        
        





                        
    
    


    
    return # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,1],
                    [0,0,2,0],
                    [0,3,4,3],
                    [9,0,6,1]]
    size=len(input_matrix)
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板