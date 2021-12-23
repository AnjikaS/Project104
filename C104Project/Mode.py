import csv
from typing import Counter

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

#Calculating the Mode
data = Counter(new_data)
#initial values:
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0,
}
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"]+= occurence #increase line 21 by 1
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"]+= occurence #increase line 22 by 1
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"]+= occurence #increase line 23 to 1

mode_range,mode_occurence = 0,0

for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [
            int(range.split("-")[0]), 
            int(range.split("-")[1])
            ], occurence

mode = float((mode_range[0]+mode_range[1])/2)
print(f"Mode is -> {mode:2f}")