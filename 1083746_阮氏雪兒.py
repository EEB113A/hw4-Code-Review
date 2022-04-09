def to_1D_array(Matrix, Major): 
    size = len(Matrix)
    res = []
    
    """Check whether the given matrix is upper right matrix then print its requirement major"""

    #Check whether the given matrix is upper right matrix or not
    def check_upper_right(Matrix):
        for row in range(1, size):
            for col in range(row):
                if (Matrix[row][col]) != 0:
                    return False
        return True
    
    #Print row major or collumn major of a given matrix
    if check_upper_right(Matrix):
        for i in range(size):
            if Major == "r":
                for j in range(i, size):
                    res.append(Matrix[i][j])
            if Major == "c":
                for k in range(0, i+1):
                    res.append(Matrix[k][i]) 
                    
###############################################################################
    
    """Check whether the given matrix is lower left matrix then print its requirement major"""                
    
    #Check whether the given matrix is lower left matrix or not             
    def check_lower_left(Matrix):
        for row in range(size):
            for col in range(row+1, size):
                if (Matrix[row][col]) != 0:
                    return False
        return True
    
    #Print row major or collumn major of a given matrix                
    if check_lower_left(Matrix):
        for i in range(size):
            if Major == "c":
                for j in range(i, size):
                    res.append(Matrix[j][i])
            if Major == "r":
                for k in range(0, i+1):
                    res.append(Matrix[i][k])

###############################################################################
                    
    """Check whether the given matrix is upper right matrix then print its requirement major"""                
    
    #Check whether the given matrix is lower right triangular matrix or not
    def check_lower_right(Matrix):
        for row in range(size-1):
            for col in range(size -2, -1, -1):
                if (Matrix[row][col]) !=  0:
                    return False
            return True
    
    #Print row major or collumn major of a given matrix
    if check_lower_right(Matrix):
            new_range = size
            for i in range(0, size):
                for j in range(new_range -1, size):
                    if Major == "r":
                        res.append(Matrix[i][j])
                    if Major == "c":
                        res.append(Matrix[j][i])
                new_range -=1

###############################################################################
                
    """Check whether the given matrix is upper left matrix then print its requirement major"""
    
    #Check whether the given matrix is upper left triangular matrix or not
    def check_upper_left(Matrix):
        for row in range(size-1):
            for col in range(size -2, -1, -1):
                if (Matrix[row][col]) ==  0:
                    return False
            return True
        
    #Print row major or collumn major of a given matrix    
    if check_upper_left(Matrix):
            for i in range(size):
                for j in range(0, size):
                    if Major == "r":
                        res.append(Matrix[i][j])
                    if Major == "c":
                        res.append(Matrix[j][i])
                size -=1
                    
    #Return 1D matrix result               
    return res

##################################################################               
if __name__ == "__main__":
    input_matrix =  [[0,0,0,0,0,0],
                     [0,0,0,0,7,8],
                     [0,0,0,5,5,9],
                     [0,0,1,6,4,1],
                     [0,0,5,8,4,9],
                     [0,7,2,6,9,0]]

    output_array = to_1D_array(input_matrix, "r")
    print(output_array)
           

#留言板