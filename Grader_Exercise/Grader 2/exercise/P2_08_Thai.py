tn = {1:'neung', 2:'song', 3:'sam', 4:'si', 5:'ha', 6:'hok', 7:'chet', 8:'paet', 9:'kao', 0:'soon'}

def to_Thai( N ):
    M=N
    out=''
    if N>=1000:
        out+=tn[N//1000]+' pun '
        N%=1000

    if N>=100:
        out+=tn[N//100]+' roi'
        N%=100
        
    if N>=10:
        if N//10==2:
            out+=" "+' yi sip'
        elif N//10>=3:
            out+=" "+tn[N//10]+' sip'
        else:
            out+=' sip'
        N%=10

    if M<10:
        return tn[N].strip()
    
    else:
        if N==0:
            return out.strip()
        elif N==1:
            return (out+' et').strip()
        else:
            return (out+' '+tn[N]).strip()
        
                
exec(input().strip())           
            