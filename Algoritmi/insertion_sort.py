def insertion_sort(s):
    for i in range(1,len(s)):
        val = s[i]
        j = i-1
        while j>=0 and s[j]>val:
            s[j+1]=s[j]
            j-=1
        s[j+1] = val
    print s

        
        
