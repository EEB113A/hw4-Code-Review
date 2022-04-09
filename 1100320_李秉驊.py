def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    count = count1 = count2 = count3 = 0
    size = len(input_matrix) #矩陣大小
    sum0 = 0
    lst = [] #空list，用來收集結果並回傳
    output = [None] * ((1 + size) * size // 2)

    for k in range(size): #不同類型矩陣之主對角線對照另一面包含0的個數
        sum0 += k

    #左下三角
    for i in range(size-1):
        for j in range(i+1, size):
            if input_matrix[i][j] == 0: #判斷矩陣過程抓到幾個0
                count += 1
    #壓縮矩陣(左下三角)
    if count == sum0:
        #水平壓縮
        index = 0
        if Major == "r":
            for f in range(size):
                for g in range(f+1):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])
        #垂直壓縮
        elif Major == "c":
            for g in range(size):
                for f in range(g, size):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])        
    #右下三角
    for i in range(size-1):
        for j in range(size-1-i):
            if input_matrix[i][j] == 0: #判斷矩陣過程抓到幾個0
                count1 += 1
    #壓縮矩陣(右下三角)
    if count1 == sum0:
        index = 0
        #水平壓縮
        if Major == "r":
            for f in range(size):
                for g in range(size-1-f, size):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])
        #垂直壓縮
        elif Major == "c":
            for g in range(size):
                for f in range(size-1-g, size):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])

    #左上三角
    for i in range(1, size):
        for j in range(size-i, size):
            if input_matrix[i][j] == 0: #判斷矩陣過程抓到幾個0
                count2 += 1
    #壓縮矩陣(左上三角)
    if count2 == sum0:
        index = 0
        #水平壓縮
        if Major == "r":
            for f in range(size):
                for g in range(size-f):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])
        #垂直壓縮
        elif Major == "c":
            for g in range(size):
                for f in range(size-g):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])

    #右上三角
    for i in range(1, size):
        for j in range(i):
            if input_matrix[i][j] == 0: #判斷矩陣過程抓到幾個0
                count3 += 1
    #壓縮矩陣(右上三角)
    if count3 == sum0:
        index = 0
        #水平壓縮
        if Major == "r":
            for f in range(0, size):
                for g in range(f, size):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])
        #垂直壓縮
        elif Major == "c":
            for g in range(size):
                for f in range(g+1):
                    output[index] = input_matrix[f][g]
                    index += 1
            for s in range(len(output)):
                lst.append(output[s])

    return lst # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0,0,0,0,0,0],
                    [0,0,0,0,7,8],
                    [0,0,0,5,5,9],
                    [0,0,1,6,4,1],
                    [0,0,5,8,4,9],
                    [0,7,2,6,9,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)

#留言板