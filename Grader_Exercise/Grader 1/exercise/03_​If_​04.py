t = input()

tel = ['06','08','09']
if len(t) == 10 and t[0:2] in tel:
    print('Mobile number')
else:
    print('Not a mobile number')