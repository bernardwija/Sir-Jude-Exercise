print('Welcome to CSV Exercise!')
file = None
with open('csvexercise.csv','r') as a:
    file = a.read()

result = {}

def csv():
    for i in range(1,len(file.split("\n"))):
        data = file.split("\n")[i].split(",")
        if len(data) < 3:
            continue
        if data[1] in result:
            if data[0] != "NA":
                result[data[1]][0] += int(data[0])
                result[data[1]][2][data[2]] = int(data[0])
            else:
                result[data[1]][1] += 1
                result[data[1]][2][data[2]] = 0
        else:
            if data[0] != "NA":
                result[data[1]] = [int(data[0]), 0, {data[2]: data[0]}]
            else:
                result[data[1]] = [0, 1, {data[2]: 0}]

    print(result)

csv()
print('Thankyou for using our service!')