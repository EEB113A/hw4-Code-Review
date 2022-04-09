def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    len_Matrix = len(Matrix)
    output_list = []

    RUT = False  #right up triangle
    RDT = False  #right down triangle
    LUT = False  #left up triangle
    LDT = False  #left down triangle
    r0 = True   #右排為0(除了兩端)
    l0 = True   #左排為0(除了兩端)
    u0 = True   #上排為0(除了兩端)
    d0 = True   #下排為0(除了兩端)

    #判斷0三角形的兩股
    for x in range(1,len_Matrix-1):
        if Matrix[0][x] != 0:
            u0 = False
        if Matrix[len_Matrix-1][x] != 0:
            d0 = False
    for y in range(1,len_Matrix-1):
        if Matrix[y][0] != 0:
            l0 = False
        if Matrix[y][len_Matrix-1] != 0:
            r0 = False
    
    if r0 == True and u0 == True:
        LDT = True
    elif l0 == True and u0 == True:
        RDT = True
    elif r0 == True and d0 == True:
        LUT = True
    elif l0 == True and d0 == True:
        RUT = True

    #如果是左下三角形的話
    if LDT == True:
        if Major == 'r':
            for y in range(len_Matrix):
                for x in range(y+1):
                    output_list.append(Matrix[y][x])
        if Major == 'c':
            for x in range(len_Matrix):
                for y  in range(x,len_Matrix):
                    output_list.append(Matrix[y][x])
    #如果是左上三角形的話
    if LUT == True:
        if Major == 'r':
            for y in range(len_Matrix):
                for x in range(len_Matrix-y):
                    output_list.append(Matrix[y][x])
        if Major == 'c':
            for x in range(len_Matrix):
                for y  in range(len_Matrix-x):
                    output_list.append(Matrix[y][x])
    #如果是右下三角形的話
    if RDT == True:
        if Major == 'r':
            for y in range(len_Matrix):
                for x in range(len_Matrix-y-1,len_Matrix):
                    output_list.append(Matrix[y][x])
        if Major == 'c':
            for x in range(len_Matrix):
                for y in range(len_Matrix-x-1,len_Matrix):
                    output_list.append(Matrix[y][x])
    #如果是右上三角形的話
    if RUT == True:
        if Major == 'r':
            for y in range(len_Matrix):
                for x in range(y,len_Matrix):
                    output_list.append(Matrix[y][x])
        if Major == 'c':
            for x in range(len_Matrix):
                for y in range(0,x+1):
                    output_list.append(Matrix[y][x])
    #print("RUT:", RUT, "RDT:", RDT, "LUT:", LUT, "LDT:", LDT)

    return output_list

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