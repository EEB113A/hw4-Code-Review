def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    input_matrix=Matrix
    n = len(input_matrix) # 判斷幾乘幾的矩陣
    m = [None] * ((1 + n) *n // 2)  # 用於存放的一維陣列
    left_up_triangle = False
    left_down_triangle = False
    right_up_triangle = False
    right_down_triangle = False
    sum = 0 # sum用於判斷0的位置
    for x in range(1,n): # 判斷是否為右上三角矩陣
      for y in range(x):
        sum += Matrix[x][y]
    if sum == 0:#若為右上三角形矩陣
      print("It's right up triangle")
      if Major == 'r':#將結果以row排列
          index = 0
          for j in range(n):
            for i in range(j,n):
              m[index] = Matrix[j][i]
              index += 1
          return m 
      elif Major == 'c':#將結果以column排列
        index = 0
        for j in range(n):
          for i in range(j+1):
            m[index] = Matrix[i][j]
            index += 1
        return m #回傳值型態:list
    sum = 0 # sum用於判斷0的位置
    for x in range(n-1): # 判斷是否為右下三角矩陣
        for y in range(n-1-x):
            sum += Matrix[y][x]
    if sum == 0:
        right_down_triangle = True

    if right_down_triangle == True: #若為右下三角形矩陣
        print("It's right down triangle")
    #將結果以row排列
        if Major == 'r':
            index = 0
            for i in range(n):
                for j in range(n-1-i,n):
                    m[index] = Matrix[i][j]
                    index += 1
            return m #回傳值型態:list
    #將結果以column排列
        elif Major == 'c':
            index = 0
            for j in range(n):
                for i in range(n-1-j,n):
                    m[index] = Matrix[i][j]
                    index += 1
            return m #回傳值型態:list
    sum = 0
    for y in range(1,n): # 判斷是否為左上三角矩陣
        for x in range(n-y,n):
            sum += Matrix[y][x]
    if sum == 0:
        left_up_triangle = True
        if left_up_triangle==True: #若為左上三角矩陣
            if Major == 'r':
                index = 0
                for i in range(n):
                    for j in range(n-i):
                        m[index] = Matrix[i][j]
                        index += 1
                return m
            if Major == "c":
                index = 0
                for j in range(n):
                    for i in range(n-j):
                        m[index] = Matrix[i][j]
                        index += 1
                return m
    sum = 0 # sum用於判斷0的位置
    for x in range(1,n):
        for y in range(x-1):
            sum += Matrix[y][x]
    if sum == 0:  #左下
        if Major == 'r':
            index = 0
            for i in range(n):
                for j in range(0, i+1):
                    m[index] = Matrix[i][j]
                    index += 1
            return m
        if Major == "c":
            index = 0
            for j in range(n):
                for i in range(j,n):
                    m[index] = Matrix[i][j]
                    index += 1
            return m

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =  [[0,5,2,0],
                     [0,0,3,1],
                     [0,0,0,7],
                     [0,0,0,0]]

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板