str1 = "Bugs Bunny"
str2 = "Dig Chungus"

str1len = len(str1)
str2len = len(str2)

array = [[[0 for z in range(2)] for x in range(str2len+1)] for y in range(str1len+1)]
print("Initial word: " + str1)
print("Length of initial word: " + str(str1len))
print("Target word: " + str2)
print("Length of target word: " + str(str2len))
#print("Initial Last: " + str(array[str1len][str2len]))

for x in range(str1len+1):
    array[x][0][0] = x

for x in range(str2len+1):
    array[0][x][0] = x

num1 = 0
num2 = 0
num3 = 0

for x in range(1,str1len+1):
    print("{", end="")
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
        print('%3s' % str(array[x][y][0]) + ",", end=" ")
    print("}")
        
            

x = str1len
y = str2len
path = []
num1 = array[x-1][y-1][0]
num2 = array[x][y-1][0]
num3 = array[x-1][y][0]
if (num1 <= num2) and (num1 <= num3):
    path.append('M')
elif (num2 <= num1) and (num2 <= num3):
    path.append('I')
else:
    path.append('D')

#checks if the value is part of table
def check(val):
    if(val[1] == 0):
        return 100
    else:
        return val[0]

#Back-Trace
while(x > 1 and y > 1):
    num1 = check(array[x-1][y-1])
    num2 = check(array[x][y-1])
    num3 = check(array[x-1][y])
    
    if (num1 <= num2) and (num1 <= num3):
        path.append(array[x-1][y-1][1])
        x-=1
        y-=1
    elif (num2 <= num1) and (num2 <= num3):
        path.append(array[x][y-1][1])
        y-=1
    else:
        path.append(array[x-1][y][1])
        x-=1

print("VVVVVVVVVVVVVVVVVVVVVVVVV")
print("Distance: " + str(len(path)-1))
print(path)
print("-----")
print("Sammie")
initCharInd = 0
targetCharInd = 0
initAlign = ""
targetAlign = ""
pathAlign = ""
for f in reversed(path):
    pathAlign+=f
    
    if(f == "M"):
        initAlign+=str1[initCharInd]
        targetAlign+=str2[targetCharInd]
        initCharInd+=1
        targetCharInd+=1
    elif(f == "I"):
        initAlign+="-"
        targetAlign+=str2[targetCharInd]
        targetCharInd+=1
    else:
        initAlign+=str1[initCharInd]
        targetAlign+="-"
        initCharInd+=1
print(initAlign)
print(pathAlign)
print(targetAlign)
print("\nSammie")
#print("Final Last: " + str(array[str1len][str2len]))
    
