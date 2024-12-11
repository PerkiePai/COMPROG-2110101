def RLE(t):
    if not t:
        return []
    
    result = []
    current_char = t[0]
    count = 1
    
    for char in t[1:]:
        if char == current_char:
            count += 1
        else:
            result.append([current_char, count])
            current_char = char
            count = 1
    
    result.append([current_char, count])
    
    return result

exec(input()) # DON'T remove this line
            
        
    
