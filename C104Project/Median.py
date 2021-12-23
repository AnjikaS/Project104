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
    new_data.append(n_num) #append joins multiple values

n = len(new_data)
new_data.sort()

#Using flow division to get the nearest whole number
#Flow division removes the decimal (For eg: 12//2 = 12)
if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else:
    median = new_data[n//2]

print("Median is: "+str(median))
