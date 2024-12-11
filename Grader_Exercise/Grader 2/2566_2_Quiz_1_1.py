face = ['A','K','Q','J','X','9','8','7','6','5','4','3','2','A']
    
def checker(cards):
    i = 0
    index = face.index(cards[i][0])
    if cards[i][0] == 'A':
        if cards[i][0] == face[index] and cards[i+1][0] == face[index+1] and cards[i+2][0] == face[index+2] and cards[i+3][0] == face[index+3] and cards[i+4][0] == face[index+4]:
            if cards[i][1] == cards[i+1][1] and cards[i][1] == cards[i+2][1] and cards[i][1] == cards[i+3][1] and cards[i][1] == cards[i+4][1]:
                return 'Royal Straight Flush'
            else:
                return 'Straight'
    else:
        if cards[i][0] == face[index] and cards[i+1][0] == face[index+1] and cards[i+2][0] == face[index+2] and cards[i+3][0] == face[index+3] and cards[i+4][0] == face[index+4]:
            if cards[i][1] == cards[i+1][1] and cards[i][1] == cards[i+2][1] and cards[i][1] == cards[i+3][1] and cards[i][1] == cards[i+4][1]:
                return 'Straight Flush'
            else:
                return 'Straight'
        elif cards[i][1] == cards[i+1][1] and cards[i][1] == cards[i+2][1] and cards[i][1] == cards[i+3][1] and cards[i][1] == cards[i+4][1]:
            return 'Flush'

N = int(input())
for _ in range(N):
    cards = input().strip()
    cards = cards[1:-1]
    cards = cards.split('|')
    print(checker(cards))
