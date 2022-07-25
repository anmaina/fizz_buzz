'''The bowling alley
Statement
In bowling, the player starts wtih 10 pins at the far end of a lane. 
The object is to knock all the pins down. For this exercise, the number of pins and balls will vary. 
Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers 
(one for each ball rolled), determine which pins remain standing after all the balls have been rolled. 
The balls are numbered from 1 to N (inclusive) for this situation. 
The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins
 that were knocked down with each role. Print a sequence of N characters, where "I" represents a pin left
  standing and "." represents a pin knocked down. '''
l = input().split()
#print(l)
list_I = ['I']*int(l[0])
#print(list_I)
list_II = list()
for i in range(int(l[1])):
    list_II = input().split()
    index_1 = int(list_II[0])-1
    index_2 = int(list_II[1])-1
    difference_index = index_2-index_1+1
    #print(index_1, index_2, difference_index)
    list_I[index_1:index_2+1]=['.']*difference_index
print(''.join([str(i) for i in list_I]))

# computer solution:
'''n, k = [int(s) for s in input().split()]
bahn = ['I'] * n
for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        bahn[j] = '.'
print(''.join(bahn))'''