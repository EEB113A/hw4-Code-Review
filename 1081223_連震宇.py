def to_1D_array(Matrix, Major):  # Matrix型態:list[list]，Major型態:str

    size = len(Matrix)  # 讀取矩陣長度
    B = [None] * ((1 + size) * size // 2)  # 設定一維壓縮矩陣

    sum = 0                             # 右下 0 -> 左上 row，一一確認值並相加，sum == 0 就確定是 左上三角矩陣
    if Major == "r":
        for i in range(0, size):
            for j in range(size-i, size):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "rlup"

    sum = 0                             # 右上 0 -> 左下row，一一確認值並相加，sum == 0 就確定是 左下三角矩陣
    if Major == "r":
        for i in range(0, size):
            for j in range(i+1, size):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "rldn"

    sum = 0                             # 左上 0 -> 右下row，一一確認值並相加，sum == 0 就確定是 右下三角矩陣
    if Major == "r":
        for i in range(0, size):
            for j in range(0, size-i-1):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "rrdn"

    sum = 0                             # 左下 0 -> 右上row，一一確認值並相加，sum == 0 就確定是 右上三角矩陣
    if Major == "r":
        for i in range(1, size):
            for j in range(0, i):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "rrup"

# ======= 上面是 row 的判定，下面是 column 的判定 =======

    sum = 0                             # 右下 0 -> 左上column，一一確認值並相加，sum == 0 就確定是 左上三角矩陣
    if Major == "c":
        for i in range(0, size):
            for j in range(size-i, size):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "clup"

    sum = 0                             # 右上 0 -> 左下column，一一確認值並相加，sum == 0 就確定是 左下三角矩陣
    if Major == "c":
        for i in range(0, size):
            for j in range(i+1, size):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "cldn"

    sum = 0                             # 左上 0 -> 右下column，一一確認值並相加，sum == 0 就確定是 右下三角矩陣
    if Major == "c":
        for i in range(0, size):
            for j in range(0, size-i-1):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "crdn"

    sum = 0                             # 左下 0 -> 右上column，一一確認值並相加，sum == 0 就確定是 右上三角矩陣
    if Major == "c":
        for i in range(1, size):
            for j in range(0, i):
                sum = sum + Matrix[i][j]
        if sum == 0:
            Major = "crup"

# ==========上面為判讀哪種三角形============

    index = 0
    if Major == "rrup":                 # row 右上，壓縮成一維矩陣
        for i in range(size):
            for j in range(i, size):
                B[index] = Matrix[i][j]
                index += 1

    index = 0
    if Major == "rldn":                 # row 左下，壓縮成一維矩陣
        for i in range(size):
            for j in range(0, i+1):
                B[index] = Matrix[i][j]
                index += 1

    index = 0
    if Major == "rrdn":                 # row 右下，壓縮成一維矩陣
        for i in range(size):
            for j in range(size-1-i, size):
                B[index] = Matrix[i][j]
                index += 1

    index = 0
    if Major == "rlup":                 # row 左上，壓縮成一維矩陣
        for i in range(size):
            for j in range(0, size-i):
                B[index] = Matrix[i][j]
                index += 1

    index = 0
    if Major == "cldn":                 # column 左下，壓縮成一維矩陣
        for i in range(size):
            for j in range(i, size):
                B[index] = Matrix[j][i]
                index += 1

    index = 0
    if Major == "clup":                 # column 左上，壓縮成一維矩陣
        for i in range(size):
            for j in range(0, size-i):
                B[index] = Matrix[j][i]
                index += 1

    index = 0
    if Major == "crdn":                 # column 右下，壓縮成一維矩陣
        for i in range(size):
            for j in range(size-i-1, size):
                B[index] = Matrix[j][i]
                index += 1

    index = 0
    if Major == "crup":                 # column 右上，壓縮成一維矩陣
        for i in range(size):
            for j in range(0, i+1):
                B[index] = Matrix[j][i]
                index += 1

    return B                            # 回傳值型態:list # [row][column]


if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix = [[0, 0, 0, 9],
                    [0, 0, 0, 8],
                    [0, 5, 0, 5],
                    [1, 6, 7, 8]]

    # 呼叫函式，給予 矩陣 和 row -> r or column -> c
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)  # 印出結果


#留言板