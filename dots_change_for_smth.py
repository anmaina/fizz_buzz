'''Given two numbers n and m. Create a two-dimensional array of size (n×m) and populate it with the characters "." 
and "*" in a checkerboard pattern. The top left corner should have the character "." . '''

n = 9
list_of_dots = [['.']*n for i in range(n)]
for a in range(n):
    for b in range(n):
        if abs(a-b)%2==0:
            list_of_dots[a][b] = '*'
for j in range(n): 
    print(' '.join(list_of_dots[j]))