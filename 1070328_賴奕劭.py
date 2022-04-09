from distutils.fancy_getopt import FancyGetopt
from operator import truediv


def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    
    size = len(Matrix)
    upper_tri = True                                    # 預設為右上三角矩陣
    right_tri = True
    # 判斷每行(列)的0是遞增或遞減
    x=0                                                 # 抓出要比較的兩行
    for k in range(size-1):                             # 總共要比size-1次
        countUpper=countLower=countLeft=countRight=0
        for j in range(size):
            if(Matrix[x][j] == 0):                      # 數前一行出現0的次數
                countUpper += 1
            if(Matrix[j][x] == 0):                      # 數前一列出現0的次數
                countLeft += 1
        x+=1
        for j in range(size):
            if(Matrix[x][j] == 0):                      # 數後一行出現0的次數
                countLower += 1
            if(Matrix[j][x] == 0):                      # 數後一列出現0的次數
                countRight += 1
        if(countUpper > countLower):                    # 上面那行0比下面那行多則為下三角
            upper_tri = False
        if(countRight > countLeft):                     # 右邊那列0比左邊那列多則為左三角
            right_tri = False

    # output: to hold the compressed representation of the triangular matrix
    output = [None] * ((1 + size) * size // 2)
    if Major=='c':                                      # 先判斷Major為'c'還是'r'
        if upper_tri == False and right_tri == False:   # 這邊再做判斷為左下三角形矩陣
            index = 0                                   # 先將index初始化
            for i in range(size):                       # 這邊將原先的Matrix的row從0到size,column從i到size放入output矩陣內
                for j in range(i,size):
                    output[index] = Matrix[j][i]
                    index += 1
        
        elif upper_tri == False and right_tri == True:  # 這邊再做判斷為右下三角形矩陣
             index = 0
             for i in range(size):                      # 這邊將原先的Matrix的row從0到size,column從0到size-i-1放入output矩陣內    
                 for j in range(0,size-i-1):
                    output[index] = Matrix[j][i]
                    index += 1
        
        elif upper_tri == True and right_tri == False:  # 這邊再做判斷為左上三角形矩陣
             index = 0
             for i in range(size):                      # 這邊將原先的Matrix的row從0到size,column從0到size-i放入output矩陣內
                 for j in range(0, size-i):
                    output[index] = Matrix[j][i]
                    index += 1

        elif upper_tri == True and right_tri == True:   # 這邊再做判斷為右上三角形矩陣
             index = 0
             for i in range(size):                      # 這邊將原先的Matrix的row從0到size,column從0到i+1放入output矩陣內
                 for j in range(0, i+1):
                    output[index] = Matrix[j][i]
                    index += 1


    elif Major=='r':
        if upper_tri == False and right_tri == False:   # 這邊再做判斷為左下三角形矩陣
            index = 0
            for i in range(size):                       # 這邊將原先的Matrix的row從0到size,column從0到i+1放入output矩陣內
                for j in range(0, i+1):
                    output[index] = Matrix[i][j]
                    index += 1
        
        elif upper_tri == False and right_tri == True:  # 這邊再做判斷為右上三角形矩陣
             index = 0
             for i in range(size):                      # 這邊將原先的Matrix的row從0到size,column從0到size-i放入output矩陣內
                 for j in range(0,size-i):
                    output[index] = Matrix[i][j]
                    index += 1

        
        elif upper_tri == True and right_tri == False:  # 這邊再做判斷為左上三角形矩陣
             index = 0
             for i in range(size):                      # 這邊將原先的Matrix的row從0到size,column從0到size-i放入output矩陣內
                 for j in range(0, size-i):
                    output[index] = Matrix[i][j]
                    index += 1

            
        elif upper_tri == True and right_tri == False:  # 這邊再做判斷為右上三角形矩陣
             index = 0
             for i in range(size):                      # 這邊將原先的Matrix的row從0到size,column從i到size放入output矩陣內
                 for j in range(i, size):
                    output[index] = Matrix[i][j]
                    index += 1

    return output # 回傳值型態:list

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