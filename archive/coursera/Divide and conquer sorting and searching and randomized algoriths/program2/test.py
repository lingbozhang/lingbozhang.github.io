# open file and store data in a list
f = open("IntegerArray.txt", "r")
inputs=[]
for line in f:
    inputs.append(int(line));

res=[0]

#inputs=[1, 20, 6, 4, 5]

helper=[0]*(len(inputs))
print("size of inputs:",len(inputs))

def combine(array,helper,lf,mid,rt):
    for i in range(lf,rt+1,1):
        helper[i]=array[i]

    hplf=lf
    hprt=mid+1
    curr=lf
    
    while hplf<=mid and hprt<=rt:
        if helper[hplf]<helper[hprt]:
            array[curr]=helper[hplf]
            hplf+=1
        else:
            array[curr]=helper[hprt]
            hprt+=1
            res[0]+=(mid-hplf+1)
        curr+=1
    while hplf<=mid:
        array[curr]=helper[hplf]
        hplf+=1
        curr+=1
    #print(array[lf:rt+1])
    #print(res[0])

def mergeSort(array,helper,lf,rt):
    if(lf<rt):
        mid=(lf+rt)//2
        mergeSort(array,helper,lf,mid)
        mergeSort(array,helper,mid+1,rt)
        combine(array,helper,lf,mid,rt)

def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        #print(arr[i])
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 


#print(getInvCount(inputs,len(inputs)/))

mergeSort(inputs,helper,0,len(inputs)-1 )

print(res)
