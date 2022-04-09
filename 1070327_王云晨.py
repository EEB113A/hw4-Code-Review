from textwrap import indent
def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    global size,A
    Matrix = [[7,0,0,0],
              [8,3,0,0],
              [4,6,5,0],
              [0,5,6,7]]
    size = len(Matrix)
    Major = str
    num = int(size*(1+size)/2)
    A = [0]*(num+1)
    index = 0
    #左下
    #if Major == 'r':     
    for i in range(size): #i:row
        for j in range(size): #j:columns
            if i>=j:
                index = index + 1  
                A[index] = Matrix[i][j] #將矩陣的值assign至陣列
    print('[',end='')   
    for i in range(size):
        for j in range(i+1,size+1):
            print(' %d'%get(i,j),end='') #輸出一維陣列
    print(' ]')
    #if Major =='c':
    #for j in range(size):
        #for i in range(size):
    
    #右上    
    #for i in range(size):
        #for j in range(size):
            #if i<=j:
               #index = index + 1
                #A[index] = Matrix[i][j]
def get(i,j):
     ind = int(size*i-i*(i+1)/2+j)
     return A[ind]

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