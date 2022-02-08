import random

def main():
    array = [0,1,2,3,4,5,6,7]
    start_col = random.choice(array)
    start_row = random.choice(array)
    destination_col = random.choice(array)
    destination_row = random.choice(array)
    if(destination_col == start_col and destination_row == start_row):
        destination_col = random.choice(array)
        destination_row = random.choice(array)
    start = (start_col,start_row)
    destination = (destination_col,destination_row)
    return start,destination

if __name__ == "__main__":
    print(main())