# open file and store data in a list
f = open("QuickSort.txt", "r")
inputs=[]
for line in f:
    inputs.append(int(line));

res=[0]

#inputs=[1, 20, 6, 4, 5]

def partition(inputs,l,r):
    mid = (l+r-1)//2
    if inputs[mid]<inputs[l]:
        if inputs[mid]>inputs[r-1]:
            inputs[mid],inputs[l]=inputs[l],inputs[mid]
        elif inputs[l]>inputs[r-1]:
            inputs[r-1],inputs[l]=inputs[l],inputs[r-1]
    else:
        if inputs[mid]<inputs[r-1]:
            inputs[mid],inputs[l]=inputs[l],inputs[mid]
        elif inputs[l]<inputs[r-1]:
            inputs[r-1],inputs[l]=inputs[l],inputs[r-1]
    i,j=l+1,l+1
    while j<r:
        if inputs[j]<inputs[l]:
            inputs[i],inputs[j]=inputs[j],inputs[i]
            i+=1
        j+=1
    inputs[l],inputs[i-1]=inputs[i-1],inputs[l]
    return i-1

def quicksort(inputs,l,r):
    if r>l:
        res[0]+=r-l-1
        mid = partition(inputs,l,r)
        quicksort(inputs,l,mid)
        quicksort(inputs,mid+1,r)
        

quicksort(inputs,0,len(inputs))
#print(inputs)
print(res)





