def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size=len(Matrix) #size*size 二維陣列
    check=[0,0,0,0]  #用來檢查左上、左下、右上、右下這四種三角形矩陣,順序為上方第0行->左方第0行->下方第0行->右方第0行,[0,0,1,1]為左上三角形矩陣,[1,0,0,1]為左下三角形矩陣,[1,1,0,0]為右下三角形矩陣,[0,1,1,0]為右上三角形矩陣
    newMatrix=list()
    for i in range(1,size-1): #檢查三角形矩陣,可參考第三行註解,該行或列為0者,check=0
        if(Matrix[0][i]!=0):
            check[0]=1
    for i in range(1,size-1):
        if(Matrix[i][0]!=0):
            check[1]=1
    for i in range(1,size-1):
        if(Matrix[size-1][i]!=0):
            check[2]=1
    for i in range(1,size-1):
        if(Matrix[i][size-1]!=0):
            check[3]=1
    if(check[0]==0 and check[1]==0): #[0,0,1,1]為左上三角形矩陣
        if Major == 'c':
            for i in range(size): #i為列(橫),j為行(直)
                for j in range (size-i-1,size): #第0行第size-1個值->第1行第size-2個值 第size-1個值->第2行第size-3個值 第size-2個值 第size-1個值,以此類推到第size-1行第0個值到第size-1個值,排成一維陣列
                        newMatrix += [Matrix[j][i]]
        elif Major == 'r':
            for j in range(size): #i為列(橫),j為行(直)
                for i in range (size-j-1,size): #第0列第size-1個值->第1列第size-2個值 第size-1個值->第2列第size-3個值 第size-2個值 第size-1個值,以此類推到第size-1列第0個值到第size-1個值,排成一維陣列
                        newMatrix += [Matrix[j][i]]
    elif(check[1]==0 and check[2]==0): #[1,0,0,1]為左下三角形矩陣
        if Major == 'c':
            for i in range(size): #i為列(橫),j為行(直)
                for j in range (i+1): #第0行第0個值->第1行第0個值到第1個值->第2行第0個值到第2個值,以此類推到第size-1行第0個值到第size-1個值,排成一維陣列
                        newMatrix += [Matrix[j][i]]
        elif Major == 'r':
            for j in range(size): #i為列(橫),j為行(直)
                for i in range (j,size): #第0列第0個值到第size-1個值->第1列第1個值到第size-1個值 ->第2列第2個值到第size-1個值,以此類推到第size-1列第size-1個值,排成一維陣列
                        newMatrix += [Matrix[j][i]]
    elif(check[2]==0 and check[3]==0): #[1,1,0,0]為右下三角形矩陣
        if Major == 'c':
            for i in range(size): #i為列(橫),j為行(直)
                for j in range (size-i): #第0行第0個值到第size-1個值->第1行第0個值到第size-2個值->第2行第0個值到第size-3個值,以此類推到第size-1行第0個值,排成一維陣列
                    newMatrix += [Matrix[j][i]]
        elif Major == 'r':
            for j in range(size): #i為列(橫),j為行(直)
                for i in range (size-j): #第0列第0個值到第size-1個值->第1列第0個值到第size-2個值->第2列第0個值到第size-3個值,以此類推到第size-1列第0個值,排成一維陣列
                        newMatrix += [Matrix[j][i]]
    elif(check[3]==0 and check[0]==0): #[0,1,1,0]為右上三角形矩陣
        if Major == 'c':
            for i in range(size): #i為列(橫),j為行(直)
                for j in range (i,size): #第0行第0個值到第size-1個值->第1行第1個值到第size-1個值->第2行第2個值到第size-1個值,以此類推到第size-1行第size-1個值,排成一維陣列
                    newMatrix += [Matrix[j][i]]
        elif Major == 'r':
            for j in range(size): #i為列(橫),j為行(直)
                for i in range (j+1): #第0列第0個值->第1列第0個值到第1個值 ->第2列第0個值到第2個值,以此類推到第size-1列第0個值到第size-1個值,排成一維陣列
                        newMatrix += [Matrix[j][i]]
    return(newMatrix) # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板