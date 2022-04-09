def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size=len(Matrix)
    A = [None]*((1+size)*size//2)
    type=4 #將三角矩陣分為4種類型，type 1為右上三角矩陣，type 2為左上三角矩陣，type 3為右下三角矩陣，type 4為左下三角矩陣
    index=0
    least=0 
    for c in range(1,size):#計算n*n三角矩陣零至少的數量。
        least+=c

    least_0=least  
    for i in range (1,size):#判斷是否為右上三角矩陣，如果是則，左下角都為零，且左下一定有1+2+...+n-1個零。
        for j in range (i):
            if Matrix[i][j]==0:
                least_0-=1
            if least_0==0:
                type=1

    least_0=least #因為前面判斷類型時，可能有幾個位置為零，剛好符合別的類型的判斷，把least_0減掉，所以要重置零的最少數量。
    for i in range (1,size): #判斷是否為左上三角矩陣，如果是，則右下角都為零。        
        for j in range (size-i,size):
            if Matrix[i][j]==0:
                least_0-=1
            if least_0==0:
                type=2

    least_0=least
    for i in range (size-1): #判斷是否為右下三角矩陣，如果是，則左上角都為零。 
        for j in range (size-1-i):
            if Matrix[i][j]==0:
                 least_0-=1
            if least_0==0:
                type=3
    #因為前三個都判斷完，如果都不是，則必為type 4

    if type==1: #之後為將各類型的三角矩陣轉為一維陣列。
        for i in range (size):
            if Major=="r":
                for j in range(i,size):
                    A[index]=Matrix[i][j]
                    index+=1
            elif Major=="c":
                for j in range (i+1):
                    A[index]=Matrix[j][i]
                    index+=1        
                
    elif type==2:
        for i in range (size):
                for j in range(size-i):
                    if Major=="r":
                        A[index]=Matrix[i][j]
                    
                    elif Major=="c":                
                        A[index]=Matrix[j][i]
                    index+=1     
    
    elif type==3:
        for i in range (size):            
            for j in range(size-1-i,size):
                if Major=="r":
                    A[index]=Matrix[i][j]
                    
                elif Major=="c":
                    A[index]=Matrix[j][i]
                index+=1
    
    elif type==4:
        for i in range (size):
            if Major=="r":
                for j in range(i+1):
                    A[index]=Matrix[i][j]
                    index+=1
            elif Major=="c":
                for j in range(i,size):
                    A[index]=Matrix[j][i]
                    index+=1  

    return  A  # 回傳值型態:list

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