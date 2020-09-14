import re
from random import *
import psycopg2

# Open and read the file
html_file = open('python_class_test.html', 'r').read()

# Get all the code with the <td> element
html_file = re.findall('<td>.+<\/td>', str(html_file))

# Step through the list in a step of 2s starting from index one
html_file = html_file[1::2]

# Get all colour into an array
colourList = []
for item in html_file:
    new_item = item.split(',')
    for color in new_item:
        if re.search('<td>', color) or re.search('</td>', color):
            color = re.sub('<td>', '', color)
            color = re.sub('</td>', '', color)
            color = re.sub(' ', '', color)
            colourList.append(color)
        else:
            color = re.sub(' ', '', color)
            colourList.append(color)
print('Answer to question number A')
print(colourList)

# convert to Dictionary
x = iter(colourList)
colourDictionary = dict(zip(x, x))

for color in colourDictionary:
    colourDictionary[color] = colourList.count(color)

print('Answer to question number B')
print(colourDictionary)

# Question number 1
sumColours = 0
for color in colourDictionary:
    sumColours = sumColours + colourDictionary[color]

mean = sumColours / len(colourDictionary)
print('Answer to question number 1')
print(mean)

# Question number 2
maxValue = 0
maxColour = ''
for color in colourDictionary:
    if colourDictionary[color] > maxValue:
        maxValue = colourDictionary[color]
        maxColour = color

print('Answer to question number 2')
print(maxColour)

# Question number 3
allValueList = []
median = 0
for color in colourDictionary:
    allValueList.append(colourDictionary[color])
    allValueList.sort()
centerNumber = len(allValueList) * 0.5
remainder = len(allValueList) % 2
if remainder == 0:
    median = (allValueList[round(centerNumber) - 1] + allValueList[round(centerNumber)]) / 2
else:
    median = allValueList[round(centerNumber)]

print('Answer to question number 3')
print(median)

# Question number 4
# formula for variance is (summation of ((mean - value) square) / number of values)
totalSummation = 0
for item in allValueList:
    totalSummation = totalSummation + ((mean - item) * (mean - item))
variance = totalSummation / len(allValueList)
print('Answer to question number 4')
print(variance)

# Question number 5
numberOfRequierdOutcome = colourList.count('RED')
numberOfPossibleOutcome = len(colourList)
probability = numberOfRequierdOutcome / numberOfPossibleOutcome

print('Answer to question number 5')
print(probability)


# Question number 6
# Notice: The function call (storeInDatabase()) had been commented.
def storeInDatabase():
    conn = psycopg2.connect(database="mydb", user='uche', password='ucke_okeke', host='127.0.0.1', port='5432')
    cursor = conn.cursor()

    # Creating table
    sql = '''CREATE TABLE COLOURDB(
       COLOUR CHAR(20) NOT NULL,
       FREQUENCY CHAR(20) NOT NULL,
    )'''
    cursor.execute(sql)

    column = ''
    columnValue = ''
    for colour in colourDictionary:
        column = column + ', ' + colour
        columnValue = columnValue + ', ' + colourDictionary[colour]
    cursor.execute(f'''INSERT INTO COLOURDB(${column}) VALUES (${columnValue})''')
    # Closing the connection
    conn.close()


# storeInDatabase()


# Question number 7
def findNumber(num):
    if num.isnumeric():
        numList = []
        for x in range(0, 50):
            numList.append(randrange(1, 100))
        if int(num) in numList:
            print('The number ' + num + ' was found in the list bellow')
            print(numList)
        else:
            print('The number ' + num + ' wasn\'t found in the list bellow')
            print(numList)
    else:
        print('The value you entered is not a number')


findNumber(input('Enter a number: '))


# Question number 8
def generateBinary():
    binValue = ''
    for num in range(4):
        binValue = binValue + str(randrange(0, 2))

    print('Answer Question number 8')
    print(binValue)  # Answer in Binary
    print(int(binValue, 2))  # Answer in decimal


generateBinary()

# Question number 9
ansList = [0, 1]
for x in range(1, 49):
    listLen = len(ansList)
    ansList.append(ansList[listLen - 2] + ansList[listLen - 1])

print('Answer Question number 9')
print(ansList)
