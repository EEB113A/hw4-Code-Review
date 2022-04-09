def to_1D_array(Matrix,Major):

    size = len(Matrix)
    B = [None] * ((1 + size) * size // 2)

    print('==========================================')
    print('矩陣為：')
    for i in range(len(Matrix)):
        for j in range(len(Matrix)):
            print(f'{Matrix[i][j]}', end='\t')
        print()
# 左下三角形
    A = []
    for i in range(size-1):
        for j in range(i+1, size):
            A.append(Matrix[i][j])
    #print(A)
    if sum(A) == 0:
        if Major == "r" :
            index = 0
            for i in range(size):
                for j in range(i+1):
                    B[index] = Matrix[i][j]
                    index += 1
        if Major == "c" :
            index = 0
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[j][i]
                    index += 1
        print('==========================================')
        print('以一維陣列表示此左下三角形矩陣：')
        return B
        




# 右上三角形
    C = []
    for i in range(1, size):
        for j in range(i):
            C.append(Matrix[i][j])
    #print(C)
    if sum(C) == 0:
        if Major == "r":
          index = 0
          for i in range(size):
              for j in range(i, size):
                  B[index] = Matrix[i][j]
                  index += 1
        if Major == "c" :
            index = 0
            for i in range(size):
                for j in range(i+1):
                    B[index] = Matrix[j][i]
                    index += 1
        print('==========================================')
        print('以一維陣列表示此右上三角形矩陣：')
        return B




# #右下三角形
    D = []
    for i in range(size-1):
        for j in range(size-i-1):
            D.append(Matrix[i][j])
        
    #print(D)
    if sum(D) == 0:
        if Major =="r":
            index = 0
            for i in range(size):
                for j in range(size-i-1, size):
                    B[index] = Matrix[i][j]
                    index += 1
        if Major == "c" :
            index = 0
            for i in range(size):
                for j in range(size-i-1,size):
                    B[index] = Matrix[j][i]
                    index += 1
        print('==========================================')
        print('以一維陣列表示此右下三角形矩陣：')
        return B




# #左上三角形
    E = []
    for i in range(1,size):
        for j in range(size-i,size):
            E.append(Matrix[i][j])
        
    #print(E)
    if sum(E) == 0:
        if Major =="r":
            index = 0
            for i in range(size):
                for j in range(size-i):
                    B[index] = Matrix[i][j]
                    index += 1
        if Major == "c" :
            index = 0
            for i in range(size):
                for j in range(size-i):
                    B[index] = Matrix[j][i]
                    index += 1
        print('==========================================')
        print('以一維陣列表示此左上三角形矩陣：')
        return B


x = to_1D_array([[0, 0, 0, 0, 0],
                 [0, 0, 0, 9, 0],
                 [0, 0, 7, 3, 3],
                 [0, 8, 0, 6, 5],
                 [3, 9, 9, 4, 9]],"c")
print(x)

#留言板