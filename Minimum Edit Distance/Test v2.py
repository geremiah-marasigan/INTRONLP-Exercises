str1 = "Bugs Bunny"
str2 = "Big Chungus"

str1len = len(str1)
str2len = len(str2)

array = [[0 for x in range(str2len+1)] for y in range(str1len+1)]
print("Initial word: " + str1)
print("Length of initial word: " + str(str1len))
print("Target word: " + str2)
print("Length of target word: " + str(str2len))
#print("Initial Last: " + str(array[str1len][str2len]))

for x in range(str1len+1):
    array[x][0] = x

for x in range(str2len+1):
    array[0][x] = x

num1 = 0
num2 = 0
num3 = 0

for x in range(1,str1len+1):
    print("{", end="")
    for y in range(1,str2len+1):
        if(str1[x-1] == str2[y-1]):
            num1 = array[x-1][y-1]
        else:
            num1 = array[x-1][y-1] + 2
        num2 = array[x][y-1]+1
        num3 = array[x-1][y]+1

        if (num1 <= num2) and (num1 <= num3):
           array[x][y] = num1
        elif (num2 <= num1) and (num2 <= num3):
           array[x][y] = num2
        else:
           array[x][y] = num3
        print('%3s' % str(array[x][y]) + ",", end=" ")
    print("}")
        
            

x = str1len
y = str2len
path = []
#checks if the value is part of table
def check(xInd,yInd):
    if(xInd > 2 or yInd > 2):
        return array[xInd][yInd]
    else:
        return 100

#Back-Trace
while(x > 1 and y > 1):
    num1 = check(x-1,y-1)
    num2 = check(x,y-1)
    num3 = check(x-1,y)
    
    if (num1 <= num2) and (num1 <= num3):
        path.append("M")
        x-=1
        y-=1
    elif (num2 <= num1) and (num2 <= num3):
        path.append("I")
        y-=1
    else:
        path.append("D")
        x-=1

print("VVVVVVVVVVVVVVVVVVVVVVVVV")
print("Distance: " + str(len(path)))
print(path)
print("-----")
print("Sammie")
for f in path:
    print(f, end = ", ")
print("\nSammie")
#print("Final Last: " + str(array[str1len][str2len]))
    
