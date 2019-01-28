str1 = "Bugs Bunny"
str2 = "Big Chungus"

str1len = len(str1)
str2len = len(str2)

array = [[[0 for z in range(2)] for x in range(str2len+1)] for y in range(str1len+1)]

print(str(str1len))
print(str(str2len))
print(str(array[10][11]))

for x in range(str1len+1):
    array[x][0][0] = x

for x in range(str2len+1):
    array[0][x][0] = x

num1 = 0
num2 = 0
num3 = 0

for x in range(1,str1len+1):
    for y in range(1,str2len+1):
        if(str1[x-1] == str2[y-1]):
            num1 = array[x-1][y-1][0]
        else:
            num1 = array[x-1][y-1][0] + 2
        num2 = array[x][y-1][0]+1
        num3 = array[x-1][y][0]+1

        if (num1 <= num2) and (num1 <= num3):
           array[x][y][0] = num1
           array[x][y][1] = 'M'
        elif (num2 <= num1) and (num2 <= num3):
           array[x][y][0] = num2
           array[x][y][1] = 'I'
        else:
           array[x][y][0] = num3
           array[x][y][1] = 'D'
        
            
print(array)
print(array[10][11])
