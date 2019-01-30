#Initial
str1 = "Bugs Bunny"
#Target
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

#Creating table
for x in range(1,str1len+1):
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

#Displaying table
for x in range(len(array)):
    for y in range(len(array[x])):
      if(y == len(array[x])-1):
          if(array[x][y] < 10):
              print(" "+str(array[x][y]),end = "")
          else:
              print(array[x][y],end = "")
      else:
          if(array[x][y] < 10):
              print(" "+str(array[x][y]),end = ", ")
          else:
              print(array[x][y],end = ", ")
    print("") 

x = str1len
y = str2len
path = []

#Back-Trace
while(x > 0 or y > 0):
    if(str1[x-1] == str2[y-1]):
        num1 = array[x-1][y-1]
    else:
        num1 = array[x-1][y-1] + 2
    num2 = array[x][y-1]+1
    num3 = array[x-1][y]+1
    
    if (num1 <= num2) and (num1 <= num3):
        if(num1 > array[x-1][y-1]):
            path.append('S')
        else:
            path.append('M')
        x-=1
        y-=1
    elif (num2 <= num1) and (num2 <= num3):
        path.append('I')
        y-=1
    else:
        path.append('D')
        x-=1
    #print(array[x][y])

print("-------------------------------")
print("Distance: " + str(len(path)-1))
print("-------------------------------")
initCharInd = 0
targetCharInd = 0
initAlign = ""
targetAlign = ""
pathAlign = ""
#Showing alignment (M = match, S = substitue, D = delete, I = insert)
for f in reversed(path):
    pathAlign+=f
    
    if(f == "M" or f == 'S'):
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
#print("Final Last: " + str(array[str1len][str2len]))
