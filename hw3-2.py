import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("305335hw03data.xlsx - Grade.csv")
data = data.sort_values(by='grade')

ck1 = 5.5
ck2 = 56
ck3 = 64.5
ck4 = 70.8
ck5 = 75.9
ck6 = 78.6
ck7 = 83.8
ck8 = 91.9

ck = []
ck1arr = []
ck2arr = []
ck3arr = []
ck4arr = []
ck5arr = []
ck6arr = []
ck7arr = []
ck8arr = []

for i in data['grade']:
    abs_grade1 = abs(i-ck1)
    abs_grade2 = abs(i-ck2)
    abs_grade3 = abs(i-ck3)
    abs_grade4 = abs(i-ck4)
    abs_grade5 = abs(i-ck5)
    abs_grade6 = abs(i-ck6)
    abs_grade7 = abs(i-ck7)
    abs_grade8 = abs(i-ck8)
    ck = [abs_grade1, abs_grade2, abs_grade3, abs_grade4, abs_grade5, abs_grade6, abs_grade7, abs_grade8]
    print(i,"ck: ", ck,"\n\n")
    minCk = min(ck)
    if minCk == abs_grade1:
        ck1arr.append(i)
    elif minCk == abs_grade2:
        ck2arr.append(i)
    elif minCk == abs_grade3:
        ck3arr.append(i)
    elif minCk == abs_grade4:
        ck4arr.append(i)
    elif minCk == abs_grade5:
        ck5arr.append(i)
    elif minCk == abs_grade6:
        ck6arr.append(i)
    elif minCk == abs_grade7:
        ck7arr.append(i)
    elif minCk == abs_grade8:
        ck8arr.append(i)

print("ck1: ", ck1arr,"\n\n")
print("ck2: ", ck2arr,"\n\n")
print("ck3: ", ck3arr,"\n\n")
print("ck4: ", ck4arr,"\n\n")
print("ck5: ", ck5arr,"\n\n")
print("ck6: ", ck6arr,"\n\n")
print("ck7: ", ck7arr,"\n\n")
print("ck8: ", ck8arr,"\n\n")

ck1arrSum = 0
ck2arrSum = 0
ck3arrSum = 0
ck4arrSum = 0
ck5arrSum = 0
ck6arrSum = 0
ck7arrSum = 0
ck8arrSum = 0

for i in ck1arr:
    ck1arrSum += abs(i-ck1)

for i in ck2arr:
    ck2arrSum += abs(i-ck2)

for i in ck3arr:
    ck3arrSum += abs(i-ck3)

for i in ck4arr:
    ck4arrSum += abs(i-ck4)

for i in ck5arr:
    ck5arrSum += abs(i-ck5)

for i in ck6arr:
    ck6arrSum += abs(i-ck6)

for i in ck7arr:
    ck7arrSum += abs(i-ck7)

for i in ck8arr:
    ck8arrSum += abs(i-ck8)

print("ck1arrSum: ", ck1arrSum,"\n\n")
print("ck2arrSum: ", ck2arrSum,"\n\n")
print("ck3arrSum: ", ck3arrSum,"\n\n")
print("ck4arrSum: ", ck4arrSum,"\n\n")
print("ck5arrSum: ", ck5arrSum,"\n\n")
print("ck6arrSum: ", ck6arrSum,"\n\n")
print("ck7arrSum: ", ck7arrSum,"\n\n")
print("ck8arrSum: ", ck8arrSum,"\n\n")

ckSum = ck1arrSum + ck2arrSum + ck3arrSum + ck4arrSum + ck5arrSum + ck6arrSum + ck7arrSum + ck8arrSum
print("ckSum: ", ckSum,"\n\n")

p = ckSum / sum(data['grade'])
print("p: ", p,"\n\n")