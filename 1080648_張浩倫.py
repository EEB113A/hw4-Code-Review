from tkinter import X

def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size=len(Matrix)#設定矩陣長度
    num=int(size*(1+size)/2) #設定三角形內數字的個數
    B=[None]*(num)#設定空陣列
    sum0=0
    sum1=0
    sum2=0
    sum3=0 
    for y in range(size): 
        for x in range(y,size):#右上三角形
            sum0=sum0+Matrix[y][x]
        for x in range(size-y-1,size):#右下三角形
            sum1=sum1+Matrix[y][x]
    for x in range(size): 
        for y in range(x,size):#左下三角形
            sum2=sum2+Matrix[y][x]
        for y in range(0,size-x):#左上三角形         
            sum3=sum3+Matrix[y][x]
    S=[sum0, sum1, sum2, sum3]
    max=S[0]
    tri=0
    for s in range(4):#比較四種三角內數字總和 最大的就是屬於那個三角形
        if S[s]>max:
            max=S[s]
            tri=s#三角形的編號
        
    index=-1
    if tri==0:#右上
        if Major=='c':#若為colume的排列方式
            for x in range(size):
                for y in range(x+1):
                    index=index+1
                    B[index]=Matrix[y][x]
        if Major=='r':#若為row的排列方式
            for y in range(size): 
                for x in range(y,size):
                    index=index+1
                    B[index]=Matrix[y][x]
    if tri==1:#右下
        if Major=='c':#若為colume的排列方式
            for x in range(size):
                for y in range(size-x-1,size):
                    index=index+1
                    B[index]=Matrix[y][x]
        if Major=='r':#若為row的排列方式
            for y in range(size):
                for x in range(size-y-1,size): 
                    index=index+1
                    B[index]=Matrix[y][x]

    if tri==2:#左下
        if Major=='c':#若為colume的排列方式
            for x in range(size):
                for y in range(x,size):
                    index=index+1
                    B[index]=Matrix[y][x]
        if Major=='r':#若為row的排列方式
            for y in range(size):
                for x in range(y+1):
                    index=index+1
                    B[index]=Matrix[y][x]
        
    if tri==3:#左上
        if Major=='c':#若為colume的排列方式
            for x in range(size):
                for y in range(size-x):
                    index=index+1
                    B[index]=Matrix[y][x]
        if Major=='r':#若為row的排列方式
            for y in range(size):
                for x in range(size-y):
                    index=index+1
                    B[index]=Matrix[y][x]
    
    return B#回傳陣列

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