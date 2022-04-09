def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    count1=count2=len(Matrix)
    m_len=len(Matrix)-1
    size=len(Matrix)
    output=[]
    stop=0
    if Matrix[m_len][m_len]==0 and Matrix[m_len][1]==0 and Matrix[1][m_len]==0:#左上矩陣壓縮
        for i in range(count1):#利用巢狀迴圈遍歷左上矩陣內應該要有值位置
            for j in range(count2):
                if Major=='r':            
                    output.append(Matrix[i][j])#從左至右一個一個放進output
                if Major=='c':
                    output.append(Matrix[j][i])#從上至下一個一個放進output
            count2-=1
        return output1
    elif Matrix[m_len][0]==0 and Matrix[1][0]==0 and Matrix[m_len][m_len-1]==0:#右上矩陣壓縮
        for i in range(0,count1):#利用巢狀迴圈遍歷右上矩陣內應該要有值位置
            for j in range(stop,count2):
                if Major=='r':            
                    output.append(Matrix[i][j])#從左至右一個一個放進output
                if Major=='c':
                    output.append(Matrix[j][i])#從上至下一個一個放進output
            stop+=1
        return output
    elif Matrix[0][m_len]==0 and Matrix[0][1]==0 and Matrix[m_len-1][m_len]==0:#左下矩陣壓縮
        for i in range(count1):
            for j in range(stop+1):#利用巢狀迴圈遍歷左下矩陣內應該要有值位置
                if Major=='r':            
                    output.append(Matrix[i][j])#從左至右一個一個放進output
                if Major=='c':
                    output.append(Matrix[j][i])#從上至下一個一個放進output
            stop+=1
        return output
    elif Matrix[0][0]==0 and Matrix[m_len-1][0]==0 and Matrix[0][m_len-1]==0:#右下壓縮
        stop=m_len
        for i in range(count1):
            for j in range(stop,count2):#利用巢狀迴圈遍歷右下矩陣內應該要有值位置
                if Major=='r':            
                    output.append(Matrix[i][j])#從左至右一個一個放進output
                if Major=='c':
                    output.append(Matrix[j][i])#從上至下一個一個放進output
            stop-=1
        return output
          


    
    


            

    return # 回傳值型態:list

if __name__ == "__main__":
    # 只有當這個 py 檔案以 Python 直譯器執行時，才會執行到以下程式碼。
    # 若是把這個 py 檔案做為模組來匯入，不會執行到以下程式碼。
    input_matrix =     [[0,0,0,0,0,0],
                        [0,0,0,0,7,8],
                        [0,0,0,5,5,9],
                        [0,0,1,6,4,1],
                        [0,0,5,8,4,9],
                        [0,7,2,6,9,0]]
    output_array = to_1D_array(input_matrix, "c")
    print(output_array)


#留言板