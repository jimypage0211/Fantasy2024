import csv
from sklearn.preprocessing import StandardScaler

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
batHeaders= [
    'ï»¿Name','AB','H','HR',"R",'RBI','BB','SO', "SB","CS","AVG","OBP","SLG","OPS", "wRC+" ,"WAR", "PlayerId"
]
batWeights = [0.5,2,8,2,2,3,-0.5,1,3,4,5,6]

def filterBatHeadersIndexes(headers):
    myHeadersIndexes = []
    for header in headers:
        if header in batHeaders:
            myHeadersIndexes.append(headers.index(header))
    return myHeadersIndexes

batHeadersIndexes = filterBatHeadersIndexes(headers)


def getBatData(data):
    batData = []
    sb = 0
    for row in data:
        myRow = []
        for index in batHeadersIndexes:
            if index == 0 or index == 46:
                myRow.append(row[index])
            elif index == 19:
                sb = float(row[index])
                continue
            elif index == 20:
                myRow.append(sb -float(row[index]))       
            else:
                myRow.append(float(row[index]))
        batData.append(myRow)
    batHeaders= ['ï»¿Name','AB','H','HR',"R",'RBI','BB','SO', "NSB","AVG","OBP","SLG","OPS", "wRC+" ,"WAR","PlayerID","Score"]
    return batHeaders,batData

batHeaders,batData = getBatData(data)
def getDataWithScore():
    numericData = []
    for row in batData:
        numericData.append(row[1:len(row)-1])

    scaler = StandardScaler()
    scaler.fit(numericData)
    standarizedData = scaler.transform(numericData).tolist()
    finalData = []
    for i in range(len(standarizedData)):
        dataToWeight = []
        weightedRow = []
        dataToWeight = standarizedData[i][0:12]
        for j in range(len(dataToWeight)):
            weightedRow.append(dataToWeight[j]*batWeights[j])
        score = [sum(weightedRow)]    
        finalData.append(batData[i] + score)
    return finalData

rows = getDataWithScore()
with open('score1.csv', 'w') as f:
     
    # using csv.writer method from CSV package
    write = csv.writer(f)
    write.writerow(batHeaders)
    write.writerows(rows)
print(batHeaders)



