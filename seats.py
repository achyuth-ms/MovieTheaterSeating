#Main function to reserve the seats where input is each line from the input document and outputs the string of all seats allocated and if no more seats avaiavle returns "House Full"
def reserve(seats):
#Update made after interview to return "Error" if desired seats <= 0    
#    if seats <= 0:
#        return "Error"
    r, c = getPosition(seats)
    
    #Condition to check for availability of continuous number of given seats
    if r == -1 and c == -1:
        remSeats = getPositionII(seats)          
        #print(remSeats)
        if not remSeats:
            return "House Full"
        
        for i in remSeats:
            for k in range(i[1], min(len(arr[r]), i[1]+3)):
                arr[i[0]][k] = 1
            if i[0] == 0:
                arr[i[0]+1][i[1]] = 1
            elif i[0] == len(arr)-1:
                arr[i[0]-1][i[1]] = 1
            else:
                arr[i[0]-1][i[1]] = 1
                arr[i[0]+1][i[1]] = 1
        res = []
        for m in remSeats:
            row = chr(ord('J')-m[0])
            res.append(row+str(m[1]+1))
        return ','.join(res)

    #print(r, c)
    #print(len(arr[r]))
    
    #Runs when contineous seats are available 
    for j in range(c, min(len(arr[r]), c+seats+3)):
        arr[r][j] = 1
    if r == 0:
        for j in range(c, c + seats):
            arr[r + 1][j] = 1
    elif r == len(arr)-1:
        for j in range(c, c + seats):
            arr[r - 1][j] = 1
    else:
        for j in range(c, c + seats):
            arr[r + 1][j] = 1
            arr[r - 1][j] = 1
    res = []
    row = chr( ord('J') - r)
    for j in range(c, c + seats):
        res.append(row + str(j + 1))
    return ','.join(res)

#Function to return row and column position where continuous given number of seats are available
#Input seats and outputs the row and column from where continuous seats are available
def getPosition(seats):
    count = 0
    i = 0
    j = 0    
    while i < len(arr):
        while j < len(arr[i]):
            if arr[i][j] == 0:
                count = count+ 1
                if count == seats:
                    return i, j - seats + 1
            else:
                count = 0
            j = j + 1           
        i = i + 1
        j = 0
        count = 0 
    return -1, -1

#Function to return row and column position where seats are available (non-continuous)
#Input required number of seats and outputs list of row , column positions where the non-continuous seats are available if not avaiable return None
def getPositionII(seats):
    count = 0
    i = 0
    j = 0    
    res = []
    while(i < len(arr)):
        while(j < len(arr[i])):
            if(arr[i][j] == 0):
                l = []
                l.append(i)
                l.append(j)
                res.append(l)
                count = count+ 1
                if(count == seats):
                    return res
            j = j + 1  
        i = i + 1
        j = 0
    return None


#Driver code to execute from the input file
import os
rowsCount = 10
seatsCount = 20
arr = [[0 for i in range(seatsCount)] for j in range(rowsCount)]
path = input("Input file:")
inputFile = open(path, 'r')
Lines = inputFile.readlines()
#print(Lines)

tickets = []
prefix = []
for line in Lines:
    prefix.append(line[:6])
    tickets.append(int(line[6:]))
#print(tickets)
#print(prefix)

out = []
for val in tickets:
    out.append(reserve(val))
#print(out)

p = os.path.dirname(inputFile.name)
#print(p)
outputFile = p + '\\' + 'output.txt'
print(outputFile)
outFile=open(outputFile,'w')
for j in range(len(out)):
    outFile.write(prefix[j])
    outFile.write(out[j])
    outFile.write('\n')
outFile.close()

