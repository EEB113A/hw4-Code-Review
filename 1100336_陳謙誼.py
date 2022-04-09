def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size=len(Matrix)
    B=[None]*((1+size)*size//2)
    
    for i in range(size):
        for j in range(size):
            print(f'{Matrix[i][j]}',end='\t')
        print()
    index=0
    #右上三角形
#    for i in Matrix:
#        for j in Matrix:#判斷是哪種三角形
#            if Matrix[i+1][j+1]==0 and Matrix[]:
                ###右上三角的
    for i in Matrix:
        #print(i)
        #for j in Matrix:

            






    
    return # 回傳值型態:list

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