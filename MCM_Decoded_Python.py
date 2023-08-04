import sys
import time 

def subset(arr,tiny_1,tiny_2):
    sum=0
    #Smallest dimension within the subset
    miny=min(arr)
    #Index of the smallest dimension
    place=arr.index(miny)
    #Approach from L.H.S.
    for i in range(place):
        sum+=tiny_1*arr[i]*arr[i+1]
    #Approach from R.H.S.
    for i in reversed(range(place,len(arr)-1)):
        sum+=arr[i]*arr[i+1]*tiny_2
    sum+=tiny_1*tiny_2*miny
    return sum

#Accept matrix dimensions
n = int(input("Enter number of dimensions:"))
p = []
print("Enter each dimension")
for i in range(n):
    ele = int(input())
    p.append(ele)

start = time.time()
#Find smallest dimension 
ans=0
small=min(p)
occ=p.count(small)
#If only single smallest dimension 
if occ==1:
    stamp=p.index(small)
    #Smallest dimension is first element
    if stamp==0:
        for i in range(n-2):
            ans+=p[stamp]*p[i+1]*p[i+2]
    #Smallest dimension is last element
    elif stamp==n-1:
        for i in reversed(range(n-2)):
            ans+=p[i]*p[i+1]*p[stamp]
    #Smallest dimension is second element
    elif stamp==1:
        for i in range(1,n-2):
            ans+=p[stamp]*p[i+1]*p[i+2]
        ans+=p[0]*p[stamp]*p[n-1]
    #Smallest dimension is second last element
    elif stamp==n-2:
        for i in reversed(range(n-3)):
            ans+=p[i]*p[i+1]*p[stamp]
        ans+=p[0]*p[stamp]*p[n-1]
    #Smallest dimension is somewhere in the middle
    else:
        for i in range(stamp,n-2):
            ans+=p[stamp]*p[i+1]*p[i+2]
        for i in reversed(range(stamp-1)):
            ans+=p[i]*p[i+1]*p[stamp]
        ans+=p[0]*p[stamp]*p[n-1]
#More than one occurrence of smallest dimension
else:
    #Finding indices of all occurences
    indices=[idx for idx, value in enumerate(p) if value == small]
    #Solving each subset
    for i in range(len(indices)-1):
        #Smallest dimensions are together
        if indices[i]+1==indices[i+1]:
            continue
        ans+=subset(p[(indices[i]+1):indices[i+1]],small,small)
    #Boil down to two smallest dimension occurences
    ans+=(len(indices)-2)*(small**3)
    #Two occurences of the smallest dimension were the first and last element
    if indices[0]==0 and indices[-1]==len(p)-1:
        print("Minimum number of multiplications is ",ans)
        end = time.time()
        print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
        sys.exit()
    #One occurence of the smallest dimension is the first element
    elif indices[0]==0:
        #Find smallest remaining dimension (excluding the smallest dimension) on R.H.S.
        right_end=min(p[(indices[-1]+1):])
        #Find smallest remaining dimension index
        right_end_index=p.index(right_end,indices[-1]+1)
        #Approach smallest remaining dimension
        for i in range(indices[-1]+1,right_end_index):
            ans+=small*p[i]*p[i+1]
        ans+=small*small*right_end
        #Case 1
        for i in range(right_end_index,len(p)-1):
            ans+=small*p[i]*p[i+1]
    #One occurence of the smallest dimension is the last element
    elif indices[-1]==len(p)-1:
        #Find smallest remaining dimension (excluding the smallest dimension) on L.H.S.
        left_end=min(p[:indices[0]])
        #Find smallest remaining dimension index
        left_end_index=len(p[:indices[0]]) - p[indices[0]::-1].index(left_end)
        #Approach smallest remaining dimension
        for i in reversed(range(left_end_index,indices[0]-1)):
            ans+=p[i]*p[i+1]*small
        ans+=left_end*small*small
        #Case 1
        for i in reversed(range(left_end_index)):
            ans+=p[i]*p[i+1]*small
    else:  
        #Find smallest remaining dimension (excluding the smallest dimension) on L.H.S.
        left_end=min(p[:indices[0]])
        left_end_index=len(p[:indices[0]]) - p[indices[0]::-1].index(left_end)
        #Find smallest remaining dimension (excluding the smallest dimension) on R.H.S.
        right_end=min(p[(indices[-1]+1):])
        right_end_index=p.index(right_end,indices[-1]+1)
        #Approach the smallest remaining dimension after comparison
        if left_end>right_end:
            for i in range(indices[-1]+1,right_end_index):
                ans+=small*p[i]*p[i+1]
            ans+=small*small*right_end
            #Case 1
            for i in range(right_end_index,len(p)-1):
                ans+=small*p[i]*p[i+1]
            for i in reversed(range(indices[0]-1)):
                ans+=p[i]*p[i+1]*small
            ans+=p[0]*small*p[-1]
        else:
            for i in reversed(range(left_end_index,indices[0]-1)):
                ans+=p[i]*p[i+1]*small
            ans+=left_end*small*small
            #Case 1
            for i in reversed(range(left_end_index)):
                ans+=p[i]*p[i+1]*small
            for i in range(indices[-1]+1,len(p)-1):
                ans+=small*p[i]*p[i+1]
            ans+=p[0]*small*p[-1]
end = time.time()
print("Minimum number of multiplications is ",ans)
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
