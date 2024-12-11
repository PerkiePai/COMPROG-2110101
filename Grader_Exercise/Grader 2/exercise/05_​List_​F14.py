def peaks(data):
    peak = list()
    count=0
    for i in range(1,len(data)-1):
        if data[i]>data[i-1] and data[i]>data[i+1]:
            peak.append(i)
    return peak      

exec(input()) # DON'T remove this line
