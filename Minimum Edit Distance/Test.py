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

x = str1len
y = str2len
path = []
path.append(array[x][y])

print(path)

while(array[x][y][0] != 0 and array[x][y][1] != 0):
    num1 = array[x-1][y-1][0]
    num2 = array[x][y-1][0]
    num3 = array[x-1][y][0]

    if (num1 <= num2) and (num1 <= num3):
        path.append(array[x-1][y-1])
        x-=1
        y-=1
    elif (num2 <= num1) and (num2 <= num3):
        path.append(array[x][y-1])
        y-=1
    else:
        path.append(array[x-1][y])
        x-=1

print(path)
print(len(path))




    
