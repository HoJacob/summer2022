#Column names and colunm
columns = {'data':0, 'time':1, 'tempout':2, 'windspeed': 7}

#Data types for each column
types = {'tempout': float, 'windspeed':float}


#Initialize my data variable
data ={}
for column in columns:
    data[column]=[]


# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    for _ in range(3):
       print(datafile.readline())
        
   
    for line in datafile:
        datum = line.split()
        for column in columns:
            i = columns[column]
            t= types.get(column, str)
            value = t(datum[i])
            data[column].append(value)

def estimate_windchill(t, v):
    wci = t - 0.7 * v
    return wci

windchill=[]
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(estimate_windchill(temp, windspeed))

