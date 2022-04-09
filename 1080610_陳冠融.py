import numpy as np  # import numpy


def to_1D_array(Matrix, Major):  # Matrix型態:list[list]，Major型態:str
    # Generate the compressed representation of the lower triangular matrix (row-major)
    size = len(Matrix)
    B = [None] * ((1 + size) * size // 2)
    # Print the lower triangular matrix
    for i in range(len(Matrix)):  # 從i開始讀Matrix
        for j in range(len(Matrix)):  # 從j開始讀Matrix
            f'{Matrix[i][j]}'  # 匯入Matrix

    if Major == "c":  # 判斷Major=c
        Matrix = np.transpose(Matrix)  # 當Major=c 時，轉置Matrix
    elif Major == "r":  # 判斷Major=r
        Matrix[i][j] = Matrix[i][j]  # 當Major=r 時，Matrix = Matrix

    for i in range(len(Matrix)):  # 從i開始讀Matrix
        for j in range(len(Matrix)):  # 從j開始讀Matrix
            # 1.上三角
            # (1)上右三角形矩陣
            if Matrix[1][0] == 0 and i > j:  # 判斷式
                if Matrix[2][0] == 0 and i > j:  # 判斷式
                    index = 0  # index = 0
                    for i in range(size):  # 從i開始讀Matrix
                        for j in range(i, size):  # 從j開始讀 i, size前一個
                            B[index] = Matrix[i][j]  # 將Matrix給陣列B
                            index += 1  # index +1，目的是在記數
            # (２)上左三角形矩陣
            if Matrix[1][size-1] == 0 and i > j:  # 判斷式
                if Matrix[2][size-1] == 0 and i > j:  # 判斷式
                    index = 0  # index = 0
                    for i in range(0, size):  # 從i開始讀Matrix
                        if i == 0:
                            for j in range(i, size):  # 從j開始讀 i到size前一個
                                B[index] = Matrix[i][j]  # 將Matrix給陣列B
                                index += 1  # index +1，目的是在記數
                        if i >= 1:
                            for j in range(i-i, size-i):  # 從j開始讀 i-i到size-i前一個
                                B[index] = Matrix[i][j]  # 將Matrix給陣列B
                                index += 1  # index +1，目的是在記數

            # 2.下三角
            # (3)下左三角形矩陣
            if Matrix[0][size-1] == 0 and Matrix[0][size-2] == 0:  # 判斷式
                if Matrix[1][size-1] == 0:  # 判斷式
                    index = 0  # index = 0
                    for i in range(size):  # 從i開始讀Matrix
                        for j in range(0, i+1):  # 從j開始讀 0到i+1前一個
                            B[index] = Matrix[i][j]  # 將Matrix給陣列B
                            index += 1  # index +1，目的是在記數
            # (4)下右三角形矩陣
            if Matrix[0][0] == 0 and Matrix[0][1] == 0:  # 判斷式
                if Matrix[1][0] == 0:  # 判斷式
                    index = 0  # index = 0
                    for i in range(size):  # 從i開始讀Matrix
                        # 從j開始讀Matrix = size-(i+1)到size前一個
                        for j in range(size-(i+1), size):  # 從j開始讀 size-(i+1)到size前一個
                            B[index] = Matrix[i][j]  # 將Matrix給陣列B
                            index += 1  # index +1，目的是在記數
    list_out = []  # 以一維陣列表示此三角形矩陣：
    for i in range(len(B)):  # 從i開始讀Ｂ
        list_out.append(B[i])  # Ｂ變成陣列
    return list_out  # 回傳值型態:list


if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。

    """
    input_matrix = [[1, 2, 3, 4],
                    [5, 6, 7, 0],
                    [8, 9, 0, 0],
                    [0, 0, 0, 0]]
    output_array = to_1D_array(input_matrix, "c")
    """
    """
    input_matrix = [[7, 0, 0, 0, 0],
                    [8, 3, 0, 0, 0],
                    [4, 6, 5, 0, 0],
                    [2, 5, 6, 7, 0],
                    [0, 4, 2, 8, 9]]
    output_array = to_1D_array(input_matrix, "r")
    """

    """
    input_matrix = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 7, 8],
                    [0, 0, 0, 5, 5, 9],
                    [0, 0, 1, 6, 4, 1],
                    [0, 0, 5, 8, 4, 9],
                    [0, 7, 2, 6, 9, 0]]
    output_array = to_1D_array(input_matrix, "c")
    """

    input_matrix = [[0, 5, 2, 0],
                    [0, 0, 3, 1],
                    [0, 0, 0, 7],
                    [0, 0, 0, 0]]
    output_array = to_1D_array(input_matrix, "r")

    print(output_array)


#留言板