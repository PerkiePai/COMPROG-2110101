m = int(input())

def checker(play1,play2):
    if play1 == play2:
        return 0
    elif (play1 == 'R' and play2 == 'S') or \
         (play1 == 'P' and play2 == 'R') or \
         (play1 == 'S' and play2 == 'P'):
        return 1
    else:
        return 2

round_count=0
score_p1=0
score_p2=0
while True:
    if score_p1==m or score_p2==m:
        print(score_p1, score_p2)
        print('Player 1 wins') if score_p1==m else print('Player 2 wins')
        break
    if round_count==3*m:
        print(score_p1, score_p2)
        print('Tie')
        break
    else:
        p1,p2 = [e for e in input().strip().split()]
        if checker(p1,p2) == 1:
            score_p1+=1
        elif checker(p1,p2) == 2:
            score_p2+=1
        round_count+=1
            
