from os import listdir
from os.path import isfile, join

#Compute placees all files are placed in /data folder
path = '/data/'
files = [f for f in listdir(path) if isfile(join(path, f))]


#Sums numbers
numbers = []

for file in files:
    if 'numbers' not in file:
        continue
    f = open(path + file)
    a = f.readlines()
    for num in a:
        numbers.append(int(num))

total = sum(numbers)
print(total)
#All files written to the /outputs folder will be tracked and uploaded to FAIRSCAPE
out = open('/outputs/total.txt','w')
out.write(str(total))
out.close()
