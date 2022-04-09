def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str   
    array_size=len(Matrix)                          #設定矩陣長度
    end=0                                           #設end為0，如果為0代表還沒找到是哪個方向矩陣，如果為1代表已經找到，則不用繼續執行其他的for迴圈，即跳出while迴圈
    tri=0                                           #給定初始值0，之後利用這個變數指派是哪種矩陣
    while end==0:                                   #不斷執行程式，直到找到是哪個方向的矩陣才結束(end=1時)
        if Major == "r" :                           #如果給的Majoe是r:
            flag=0                                  #設flag為中斷點，如果接下來不符合這類的矩陣，則flag=1，執行下一個方向的矩陣
            for i in range(1,array_size):           #判斷矩陣是否為左上矩陣
                if flag==1:                         #如果flag=1:
                    break                           #則break
                for j in range(i):                  #此for是要判斷0是不是都靠在右下半部，如果都是0，則此矩陣為左上矩陣
                    if Matrix[i][-j-1]!=0:          #若偵測到其中一格應該為0的地方不為0，則不是左上矩陣
                        flag=1                      #讓flag=1可以跳出迴圈
                        break                       #break
                    
            if flag == 0:                           #如果矩陣已經判斷出來是哪一個方向
                tri = 1                             #tri=1代表此矩陣為左上矩陣
                end = 1                             #已判斷出來是哪個方向的矩陣，就讓end=1跳出迴圈

            flag=0
            for i in range(array_size-1):           #接下來的步驟與上方幾乎一樣，而此為判斷是否為左下矩陣的程式
                if flag==1:
                    break
                for j in range(1,array_size-i):
                    if Matrix[i][-j]!=0:
                        flag=1
                        break

            if flag == 0:
                tri = 2                             #tri=2代表此矩陣為左下矩陣
                end = 1
                        
            flag=0
            for i in range(1,array_size):           #此為判斷是否為右上矩陣的程式
                if flag==1:
                    break
                for j in range(0,i):
                    if Matrix[i][j]!=0:
                        flag=1
                        break
 
            if flag == 0:
                tri = 3                             #tri=3代表此矩陣為右上矩陣
                end = 1     

                        
            flag=0
            for i in range(array_size-1):           #此為判斷是否為右下矩陣的程式
                if flag==1:
                    break
                for j in range(0,array_size-i-1):
                    if Matrix[i][j]!=0:
                        flag=1
                        break
                        
            if flag == 0:
                tri = 4                             #tri=4代表此矩陣為右下矩陣
                end = 1
            
        if Major == "c":                            #這裡為Major=c的部分，而下面也是和上面非常相似
            flag=0
            for i in range(1,array_size):           #此為判斷是否為左上的程式
                if flag==1:
                    break
                for j in range(i):
                    if Matrix[i][-j-1]!=0:
                        flag=1
                        break
            if flag == 0:
                tri = 5                             #tri=5代表此矩陣為左上矩陣
                end = 1

            flag=0
            for i in range(array_size-1):           #此為判斷是否為左下的程式
                if flag==1:
                    break
                for j in range(1,array_size-i):
                    if Matrix[i][-j]!=0:
                        flag=1
                        break
            if flag == 0:
                tri = 6                             #tri=6代表此矩陣為左下矩陣
                end = 1
                        
            flag=0
            for i in range(1,array_size):           #此為判斷是否為右上的程式
                if flag==1:
                    break
                for j in range(0,i):
                    if Matrix[i][j]!=0:
                        flag=1
                        break
                       
            if flag == 0:
                tri = 7                             #tri=7代表此矩陣為右上矩陣
                end = 1     

                        
            flag=0
            for i in range(array_size-1):           #此為判斷是否為右下的程式
                if flag==1:
                    break
                for j in range(0,array_size-i-1):
                    if Matrix[i][j]!=0:
                        flag=1
                        break
                        
            if flag == 0:
                tri = 8                             #tri=8代表此矩陣為右下矩陣
                end = 1
    
    if tri == 1:                                    #依照不同方向和Major進行append
        ans=[]
        for i in range(array_size):
            for j in range(array_size-i):
                ans.append(Matrix[i][j])
    
    elif tri == 2:
        ans=[]
        for i in range(array_size):
            for j in range(0,i+1):
                ans.append(Matrix[i][j])
                
    elif tri == 3 :
        ans=[]
        for i in range(array_size):
            for j in range(i,array_size):
                ans.append(Matrix[i][j])
    
    elif tri == 4 :
        ans=[]
        for i in range(array_size):
            for j in range(array_size-i-1,array_size):
                ans.append(Matrix[i][j])
                
    elif tri == 5 :
        ans=[]
        for i in range(array_size):
            for j in range(array_size-i):
                ans.append(Matrix[j][i])
    
    elif tri == 6 :
        ans=[]
        for i in range(array_size):
            for j in range(i,array_size):
                ans.append(Matrix[j][i])
                
    elif tri == 7 :
        ans=[]
        for i in range(array_size):
            for j in range(i+1):
                ans.append(Matrix[j][i])

    elif tri == 8 :
        ans=[]
        for i in range(array_size):
            for j in range(array_size-i-1,array_size):
                ans.append(Matrix[j][i])
  
    return ans # 回傳值型態:list                     #return 答案!!!        

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