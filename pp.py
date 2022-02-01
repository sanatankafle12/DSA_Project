def square(location):
    if(location[1]<0 or location[0]<0 or location[0]>7 or location[1]>7):
        return
    
    valid_square = []
    row = location[1]
    col = location[0]
    valid_square.append((col+2,row+1))
    valid_square.append((col+1,row+2))
    valid_square.append((col-2,row+1))
    valid_square.append((col-1,row+2))
    valid_square.append((col+2,row-1))
    valid_square.append((col+1,row-2))
    valid_square.append((col-2,row-1))
    valid_square.append((col-1,row-2))
    for j in range(len(valid_square)):
        for i in valid_square:
            if (i[1]<0 or i[0]<0 or i[0]>7 or i[1]>7):
                valid_square.remove(i)
    return valid_square

if __name__ == "__main__":
    print(square((0,0)))
