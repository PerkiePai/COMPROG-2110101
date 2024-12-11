file1,file2 = input().strip().split()
    
with open(file1,'r') as f1:
    with open(file2,'r') as f2:
        line1 = f1.readline().strip()
        line2 = f2.readline().strip() 
        while True:
            if line1 == '' and line2=='':
                break
            elif not line1 == '' and line2=='':
                print(line1)
                line1 = f1.readline().strip()
            elif line1 == '' and not line2=='':
                print(line2)
                line2 = f2.readline().strip() 
            else:
                name1,gpa1 = line1.split()
                fac1=name1[-2:]
                y1=name1[:2]
                or1=name1[3:8]
                name2,gpa2 = line2.split()
                fac2=name2[-2:]
                y2=name2[:2]
                or2=name2[3:8]
                if fac1<fac2:
                    print(line1)
                    line1 = f1.readline().strip()
                elif fac2<fac1:
                    print(line2)
                    line2 = f2.readline().strip() 
                else:
                    if y1<y2:
                        print(line1)
                        line1 = f1.readline().strip()
                    elif y2<y1:
                        print(line2)
                        line2 = f2.readline().strip() 
                    else:
                        if or1<or2:
                            print(line1)
                            line1 = f1.readline().strip()
                        elif or2<or1:
                            print(line2)
                            line2 = f2.readline().strip() 
                        else:
                            print(0)
            
            
            
        