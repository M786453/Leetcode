def gcd(str1, str2):
    
    length = len(str1)
    
    if length > len(str2):
        
        length = len(str2)
        
    for i in range(1,length+1):
        
        divisor = str1[:i]
        
        m1 = len(str1) // len(divisor)
        
        m2 = len(str2) // len(divisor)
        
        if divisor*m1 == str1 and divisor*m2 == str2:
            return str1[:i]
          
    return ""
