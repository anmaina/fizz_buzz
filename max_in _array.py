'''Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements, 
find the index position of the maximum element and print two numbers representing the index (i×j)
 or the row number and the column number. If there exist multiple such elements in different rows, print the one with smaller row number.
 If there multiple such elements occur on the same row, output the smallest column number. '''

indexes = input().split()
elem = int(indexes[0])
list_of_num = [[int(j) for j in input().split()] for i in range(elem)]
max_value =[max(i) for i in list_of_num]
max_max_value = max(max_value)
t = ()
for a in range(int(elem)):
    if t!=():
        break
    for b in range(int(indexes[1])):
        if list_of_num[a][b] == max_max_value:
            t = (a, b)
            print(a,b)
            break 