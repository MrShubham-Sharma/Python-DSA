def funct(s): # we Have String as an s object

    l = 0
    # l will be the left pointer
    
    r = len(s) - 1
    # r will be the right pointer
    
    while l < r:
    #if the l< r then it's an false  
    
        if s[l] != s[r]:
            print(False)
            return False
        l += 1
        r -= 1
    # else true it's an palidrome    
    print(True)
    return True

funct("NITIN")