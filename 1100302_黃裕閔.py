from turtle import Turtle


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size = len(Matrix)  #先算出此矩陣的長度
    leftu = False #設置一個代表左上矩陣的變數
    leftd = False #設置一個代表左下矩陣的變數
    rightu = False #設置一個代表右上矩陣的變數
    rightd = False #設置一個代表右下矩陣的變數
    countld = 0 # 此變數用來計算矩陣中的0
    countlu = 0 # 此變數用來計算矩陣中的0
    countrd = 0 # 此變數用來計算矩陣中的0
    countru = 0 # 此變數用來計算矩陣中的0
    r_function = False #用來偵測是否為row壓縮
    c_function = False #用來偵測是否為column壓縮
    number_of_half = (size+1)*size//2 - size #一半的矩陣扣掉對角線之元素和  
    compre = [None] * ((size+1) *size //2 ) #用來裝載壓縮後的元素
    for i in range(0,size):        #計算右上角0的個數
        for j in range(1+i,size):
            if Matrix[i][j] ==0:
                countld += 1
    for i in range(1,size):        #計算右下角0的個數
        for j in range(size-1-i,size):
            if Matrix[i][j] ==0:
                countlu += 1
    for i in range(1,size):        #計算左下角0的個數
        for j in range(0,1+i):
            if Matrix[i][j] ==0:
                countru += 1
    for i in range(0,size):        #計算左上角0的個數
        for j in range(0,size-1-i):
            if Matrix[i][j] ==0:
                countrd += 1
    if countrd >= number_of_half:  #確定每個角的0的個數符不符合所求
        rightd = True
    if countru >= number_of_half:  #確定每個角的0的個數符不符合所求
        rightu = True
    if countlu >= number_of_half:  #確定每個角的0的個數符不符合所求
        leftu = True
    if countld >= number_of_half:  #確定每個角的0的個數符不符合所求
        leftd = True
    if Major == "r":      #確定此次要進行的壓縮方式
        r_function = True
    if Major == "c":      #確定此次要進行的壓縮方式
        c_function = True
    if leftu and c_function:    #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(0,size-i):
                compre[index] = Matrix[j][i]
                index +=1
    if leftd and c_function:    #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(i,size):
                compre[index] = Matrix[j][i]
                index +=1
    if rightd and c_function:   #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(size-1-i,size):
                compre[index] = Matrix[j][i]
                index += 1
    if rightu and c_function:   #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(0,1+i):
                compre[index] = Matrix[j][i]
                index +=1
    if leftu and r_function:    #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(0,size-i):
                compre[index] = Matrix[i][j]
                index +=1
    if leftd and r_function:    #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(0,1+i):
                compre[index] = Matrix[i][j]
                index +=1
    if rightd and r_function:   #將確定的三角矩陣壓縮
        index = 0
        for i in range(size):
            for j in range(size-1-i,size):
                compre[index] = Matrix[i][j]
                index += 1
    if rightu and r_function:   #將確定的三角矩陣壓縮
        index = 0 
        for i in range(size):
            for j in range(i,size):
                compre[index] = Matrix[i][j]
                index +=1
    return compre  #回傳壓縮後矩陣
if __name__ == "__main__":
    input_matrix = [[0,5,2,0],
[0,0,3,1],
[0,0,0,7],
[0,0,0,0]]
    output_array = to_1D_array(input_matrix, "r")
    print(output_array)


#留言板