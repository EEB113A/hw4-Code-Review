import numpy as np

def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    leftuptri = leftlowtri=rightuptri=rightlowtri = False#一開始先預設4種情況等於False
    #for i in range(len(Matrix)):
    #    for j in range(len(Matrix)):
    #        print(f'{Matrix[i][j]}', end='\t')
    #    print()
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            if i>j and Matrix[i][j]!=0 and (Matrix[j][i]==0) :#左上到右下的對角線以下有數字，以上等於0，則leftlowtri=True
                leftlowtri=True
            elif i>j and Matrix[j][i]!=0 and(Matrix[i][j]==0) :#左上到右下的對角線以上有數字，以下等於0，則rightuptri=True
                rightuptri=True
    #print('-------------------------')
    A=np.flip(Matrix,axis=1)#令A矩陣為Matrix的左右相反矩陣
    #for i in range(len(A)):
    #    for j in range(len(A)):
     #       print(f'{A[i][j]}', end='\t')
      #  print()
    for i in range(len(A)):
        for j in range(len(A)):
            if i>j and (A[i][j]!=0) and (A[j][i]==0) :#在A矩陣來看是左上到右下的對角線以下有數字，以上等於0，但以原Matrix矩陣來看是右上到左下的對角線以下有數字，以上等於0
                rightlowtri=True
            elif i>j and (A[j][i]!=0) and (A[i][j]==0) :#以原Matrix矩陣的角度來看是右上到左下的對角線以上有數字，以下等於0
                leftuptri=True
    #print('leftlowtri :', leftlowtri)
    #print('rightuptri :',rightuptri)
    #print('leftuptri :',leftuptri)
    #print('rightlowtri :',rightlowtri)
    output=[None] * ((1 + size) * size // 2)
    if(Major=='r'):
        if(leftuptri==True):#左上三角(R)
            index = 0
            for i in range(size):
                for j in range(0,size-i):
                    output[index] = Matrix[i][j]
                    index += 1
        if(rightuptri==True):#右上三角(R)
            index = 0
            for i in range(size):
                for j in range(i, size):
                    output[index] = Matrix[i][j]
                    index += 1
        if(leftlowtri==True):#左下三角(R)
            index=0
            for i in range(size):
                for j in range(0,i+1) :
                    output[index] = Matrix[i][j]
                    index += 1
        if(rightlowtri==True):#右下三角(R)
            index = 0
            for i in range(size):
                for j in range(size-i-1,size):
                    output[index] = Matrix[i][j]
                    index += 1
    if(Major=='c'):
        if(leftuptri==True):#左上三角(C)
            index = 0
            for i in range(size):
                for j in range(0,size-i):
                    output[index] = Matrix[j][i]
                    index += 1
        if(rightuptri==True):#右上三角(C)
            index=0
            for i in range(size):
                for j in range(0,i+1) :
                    output[index] = Matrix[j][i]
                    index += 1
        if(leftlowtri==True):#左下三角(C)
            index = 0
            for i in range(size):
                for j in range(i, size):
                    output[index] = Matrix[j][i]
                    index += 1
        if(rightlowtri==True):#右下三角(C)
            index = 0
            for i in range(size):
                for j in range(size-i-1,size):
                    output[index] = Matrix[j][i]
                    index += 1
    return output# 回傳值型態:list
if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[7,0,0,0],
                    [8,3,0,0],
                    [4,6,5,0],
                    [0,5,6,7]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板