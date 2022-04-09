def to_1D_array(Matrix, Major): # Matrix型態:list[list]，Major型態:str
    size=len(Matrix)
    B = [None] * ((1 + size) * size // 2)
    index = 0   
    lst1=[]
    lst2=[]
    lst3=[]
##############################################################################  
    #右下三角形
    for i in range(0,size-1):
        for j in range(0,size-1-i):
            lst1.append(Matrix[i][j])                #左上位置的數字
      
    #左下三角形         
    for i in range(1,size):
        for j in range(i):  
            lst2.append(Matrix[j][i])                #右上位置的數字    
        
    #右上三角形
    for i in range(1,size):
        for j in range(0,i):
            lst3.append(Matrix[i][j])                #左下位置的數字
##############################################################################  
    if any(lst1)==0:                                 #若左上位置的數字皆為 0
        if Major == "c" : #右下,c
            for i in range(size):
                for j in range(size-1-i, size):
                    B[index] = Matrix[j][i]
                    index += 1
            lstc1=[]        
            for k in range(len(B)):
                lstc1.append(f'{B[k]}')
                lstc1 = [ int(x) for x in lstc1 ]    #list內的str元素轉成int
            return lstc1  #==右下,c
             
        elif Major == "r":  #右下,r
            for i in range(size):
                for j in range(size-1-i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            lstr1=[]       
            for k in range(len(B)):
                lstr1.append(f'{B[k]}')
                lstr1 = [ int(x) for x in lstr1 ]   #list內的str元素轉成int
            return lstr1   #==右下,r
##############################################################################        
    elif any(lst2)==0:                              #若右上位置的數字皆為 0 
        if Major=="c": #左下 c
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[j][i]
                    index += 1
            lstc2=[]        
            for k in range(len(B)):
                lstc2.append(f'{B[k]}')
                lstc2 = [ int(x) for x in lstc2 ]   #list內的str元素轉成int
            return lstc2  #==左下 c
                    
            
        elif Major=="r": #左下 r
            for i in range(size):
                for j in range(0, i+1):
                    B[index] = Matrix[i][j]
                    index += 1
            lstr3=[]        
            for k in range(len(B)):
                lstr3.append(f'{B[k]}') 
                lstr3 = [ int(x) for x in lstr3 ]   #list內的str元素轉成int
            return lstr3   #==左下 r   
        
##############################################################################        
    elif any(lst3)==0:   #若左下位置的數字皆為 0
        if Major=="c":   #右上 c
            for i in range(size):
                for j in range(0, i+1):
                    B[index] = Matrix[j][i]
                    index += 1
            lstc3=[]        
            for k in range(len(B)):
                lstc3.append(f'{B[k]}')
                lstc3 = [ int(x) for x in lstc3 ]   #list內的str元素轉成int
            return lstc3   #==右上 c
        elif Major=="r": #右上 r
            for i in range(size):
                for j in range(i, size):
                    B[index] = Matrix[i][j]
                    index += 1
            lstr2=[]        
            for k in range(len(B)):
                lstr2.append(f'{B[k]}')
                lstr2 = [ int(x) for x in lstr2 ]   #list內的str元素轉成int
            return lstr2   #==右上 c          
           
##############################################################################    
    else:   #若右下位置的數字皆為 0
        if Major=="c": #左上 c
            for i in range(size):
                for j in range(0, size-i):
                    B[index] = Matrix[j][i]
                    index += 1
            lstc4=[]       
            for k in range(len(B)):
                lstc4.append(f'{B[k]}')
                lstc4 = [ int(x) for x in lstc4 ]   #list內的str元素轉成int
            return lstc4   #==左上 c
                    
        elif Major== "r": #左上 r
            for i in range(size):
                for j in range(0, size-i): 
                    B[index] = Matrix[i][j]
                    index += 1
            lstr4=[]
            for k in range(len(B)):
                lstr4 += f'{B[k]}' 
                lstr4 = [ int(x) for x in lstr4 ]   #list內的str元素轉成int
            return lstr4   #==左上 r
##############################################################################              
if __name__ == "__main__":

    input_matrix = [[0,5,2,0],
                    [0,0,3,1],
                    [0,0,0,7],
                    [0,0,0,0]]

    output_array = to_1D_array(input_matrix,"c")
    print(output_array)

    

#留言板