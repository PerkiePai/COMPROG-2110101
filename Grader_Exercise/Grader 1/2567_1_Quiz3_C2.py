
# d1={}
# d2={}
# for i in range(int(input())):
#     data=input().split(',')
#     d1[data[0]]=data[1]
#     d2[data[0]]=int(data[2])

# d3={}
# for k,v in d1.items():
#     if v in d3:
#         d3[v].append(k)
#     else:
#         d3[v]=[k]

# # print(d3)

# while True:
#     dtemp1=dict(zip(d3.keys(),d3.values()))
#     for k1,v1 in d3.items():
#         for k2,v2 in d3.items():
#             if k1==k2:
#                 continue
#             if k2 in v1:
#                 d3[k1]=d3[k1]+d3[k2]
#                 d3[k2]=[]
#     dtemp2=dict(zip(d3.keys(),d3.values()))
#     if dtemp1==dtemp2:
#         break

# d4={}
# for k1,v1 in d3.items():
#     t=0
#     for e in v1:
#         t+=d2[e]
#     d4[k1]=t

# l1=sorted([[k,v] for k,v in d4.items() if v!=0],key=lambda a:-a[1])
# for e in l1:
#     line='Boss '+e[0]+' '+str(e[1])
#     print(line)

