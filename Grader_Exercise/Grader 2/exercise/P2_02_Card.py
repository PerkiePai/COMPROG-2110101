output = ''
string_list = ['A', '2', '3', '4' ,'5', '6', '7', '8', '9' ,'T', 'J' ,'Q' ,'K','C','D','H','S']
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4]

def card_to_num(index):
    num = num_list[string_list.index(cards[index])]
    return num    
    
def compare(index):
    if card_to_num(index) != card_to_num(index+2):
        if card_to_num(index+1) != card_to_num(index+3):
            value = card_to_num(index)-card_to_num(index+2)
        else:
            value = card_to_num(index)-card_to_num(index+2)
    else:
        if card_to_num(index+1) != card_to_num(index+3):
            value = card_to_num(index+1)-card_to_num(index+3)
        else:
            return str(0)
        
    if value>0:
        return '+'+str(value)
    else:
        return str(value)

cards = input().strip()
n_card = len(cards)/2

for i in range(0,len(cards)-2,2):
    output += compare(i)

print(output)
    
    
    
    
    
        