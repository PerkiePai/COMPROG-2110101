import math

w1=float(input())
h1=float(input())

most=(math.sqrt(w1*h1))/60
hayc=.024265*w1**.5378*h1**.3964
boyd=.0333*w1**(.6157-.0188*math.log(w1,10))*h1**.3

print(most)
print(hayc)
print(boyd)