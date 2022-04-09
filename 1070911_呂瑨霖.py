def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)
    # print(size)
    # 看每行列的0 遞增還是遞減
    uptri = ltri = True
    x = 0  # 比較的行數
    for k in range(size - 1):
        countUP = countDN = countL = countR = 0
        for j in range(size):
            if (Matrix[x][j] == 0):  # 行
                countUP += 1
            if (Matrix[j][x] == 0):  # 列
                countL += 1
        x += 1
        for j in range(size):
            if (Matrix[x][j] == 0):  # 行
                countDN += 1
            if (Matrix[j][x] == 0):  # 列
                countR += 1
        if (countUP > countDN):
            uptri = False
        if (countL > countR):
            ltri = False
    # print('uptri :',uptri)
    # print('ltri: ',ltri)

    output = [None] * ((1 + size) * size // 2)
    if (Major == 'r'):
        if (uptri == True and ltri == True):  # 上左
            index = 0
            for i in range(size):
                for j in range(0, size - i):
                    output[index] = Matrix[i][j]
                    index += 1
        if (uptri == True and ltri == False):  # 上右
            index = 0
            for i in range(size):
                for j in range(i, size):
                    output[index] = Matrix[i][j]
                    index += 1
        if (uptri == False and ltri == True):  # 下左
            index = 0
            for i in range(size):
                for j in range(0, i + 1):
                    output[index] = Matrix[i][j]
                    index += 1
        if (uptri == False and ltri == False):  # 下右
            index = 0
            for i in range(size):
                for j in range(size - i - 1, size):
                    output[index] = Matrix[i][j]
                    index += 1
    if (Major == 'c'):
        if (uptri == True and ltri == True):  # 上左
            index = 0
            for i in range(size):
                for j in range(0, size - i):
                    output[index] = Matrix[j][i]
                    index += 1
        if (uptri == True and ltri == False):  # 上右
            index = 0
            for i in range(size):
                for j in range(0, i + 1):
                    output[index] = Matrix[j][i]
                    index += 1
        if (uptri == False and ltri == True):  # 下左
            index = 0
            for i in range(size):
                for j in range(i, size):
                    output[index] = Matrix[j][i]
                    index += 1
        if (uptri == False and ltri == False):  # 下右
            index = 0
            for i in range(size):
                for j in range(size - i - 1, size):
                    output[index] = Matrix[j][i]
                    index += 1
    return output# 回傳
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