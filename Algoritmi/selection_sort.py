def selection(L):
    for i in range(len(L)-1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal>L[j]:
                minIndx = j
                minVal = L[j]
	     j +=1
	     swap(L,i,minIndx)
def swap(L,x,y):
  t = L[x]
  L[x] = L[y]
  L[y] = t
