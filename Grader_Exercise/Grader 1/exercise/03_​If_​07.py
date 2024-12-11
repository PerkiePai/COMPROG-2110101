n = int(input())


def num_find(n,m):
    if len(str(n))%3==1:
        return round(n/10**m,1)
    elif len(str(n))%3==2:
        return round(n/10**m)
    elif len(str(n))%3==0:
        return round(n/10**m)


if n<10**3:
    print(n)
elif n<10**6:
    print(f'{num_find(n,3)}K')
elif n<10**9:
    print(f'{num_find(n,6)}M')
elif n<10**12:
    print(f'{num_find(n,9)}B')
else:
    print(f'{round(n/10**9)}B')