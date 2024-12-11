data = input()

if data == 'q':
    print('No Data')
else:
    sum=0
    n=1
    sum+=float(data)
    data = input()
    while data!='q':
        n+=1
        sum+=float(data)
        data=input()
    avg=sum/n
    print(round(avg,2))