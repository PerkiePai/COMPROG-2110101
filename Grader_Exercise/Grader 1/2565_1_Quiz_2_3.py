with open('data/data1.txt','r') as f1:
    with open('data/data2.txt','r') as f2:
        color_string=''
        for e in f1:
            color_string+=e.strip('\n').lower()+' '
        colors=color_string.split()
        
        while True:
            line = f2.readline()
            if line=='':
                break
            new_line=''
            
            for color in colors:
                for i in range(len(line)-len(color)):
                    idx=i
                    idx=line.lower().find(color,i)
                    if idx==-1:
                        new_line+=line[idx:]
                        break
                    else:
                        new_line+=line[:idx]+"<"+color+">"+line[idx:idx+len(color)]+"</>"
                        idx+=len(line[:idx]+"<"+color+">"+line[idx:idx+len(color)]+"</>")
                        
                    
                    
            
            print(new_line)
        