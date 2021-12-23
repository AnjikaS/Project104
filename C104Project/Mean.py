import csv

with open('height-weight.csv',newline='') as f:
    reader = csv.reader(f)
    #list gives bullet numbers to each data so that you can pick certain data easily
    #has multiple data types
    file_data = list(reader)

file_data.pop(0) #push = adds element; pop = removes element
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1] #complete index of height
    new_data.append(float(n_num)) #append joins multiple values

#Getting the mean
n = len(new_data) #len = total number of data/elements in file
total = 0
for x in new_data:
    total = total+x
mean = total/n
print("Mean or Average is: "+str(mean))