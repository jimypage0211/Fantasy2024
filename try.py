import csv
def getData (filepath):
    data = []
    with open(filepath, mode="r") as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            data.append(line)   
    headers = data[0]
    data = data[1 : len(data)]
    return headers, data

headers, data = getData("Bats_ATC.csv")
print(headers)

batHeaders= [
    'ï»¿Name','AB','H','HR',"R",'RBI','BB','SO', "SB","CS","AVG","OBP","SLG","OPS", "wRC+" ,"WAR"
]

def filterBatHeadersIndexes(headers):
    myHeadersIndexes = []
    for header in headers:
        if header in batHeaders:
            myHeadersIndexes.append(headers.index(header))
    return myHeadersIndexes

batHeadersIndexes = filterBatHeadersIndexes(headers)
print(batHeadersIndexes)

def getBatData(data):
    batData = []
    sb = 0
    for row in data:
        myRow = []
        for index in batHeadersIndexes:
            if index == 0:
                myRow.append(row[index])
            elif index == 19:
                sb = float(row[index])
                continue
            elif index == 20:
                myRow.append(sb -float(row[index]))                
            else:
                myRow.append(float(row[index]))
        batData.append(myRow)
    batHeaders= ['ï»¿Name','AB','H','HR',"R",'RBI','BB','SO', "NSB","AVG","OBP","SLG","OPS", "wRC+" ,"WAR"]
    return batHeaders,batData

batHeaders,batData = getBatData(data)
print(batHeaders)
print(batData[0])

