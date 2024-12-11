id_1, gpax_1, comp_1, cal1_1, cal2_1 = input().split()
id_2, gpax_2, comp_2, cal1_2, cal2_2 = input().split()

gpax_1 = float(gpax_1)
gpax_2 = float(gpax_2)

if comp_1 == 'A' and cal1_1 <= 'C' and cal2_1 <= 'C':
    if comp_2 == 'A' and cal1_2 <= 'C' and cal2_2 <= 'C':
        if gpax_1 != gpax_2:
            if gpax_1 > gpax_2:
                print(id_1)
            else:
                print(id_2)
        else:
            if cal1_1 != cal1_2:
                if cal1_1 < cal1_2:
                    print(id_1)
                else:
                    print(id_2)
            else:
                if cal2_1 != cal2_2:
                    if cal2_1 < cal2_2:
                        print(id_1)
                    else:
                        print(id_2)
                else:
                    print('Both')
    else:
        print(id_1)
else:
    if comp_2 == 'A' and cal1_2 <= 'C' and cal2_2 <= 'C':
        print(id_2)
    else:
        print('None')
