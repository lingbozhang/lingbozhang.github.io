class unionfind:

    def __init__(self,num):
        self.num = num
        self.parent = [ i for i in range(num)]
        self.rank = [ 1 for i in range(num)]
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)

        if px!=py:
            if self.rank[px]>self.rank[py]:
                self.parent[py]=px
                self.rank[px]+=1
            else:
                self.parent[px]=py
                self.rank[py]+=1
# test union-find

def test_unionfind():
    testIpts=[[1,2],[3,4],[5,3],[5,4]]
    num=5
    uf=unionfind(num)

    for ele in testIpts:
        uf.union(ele[0]-1,ele[1]-1)

    print(set(uf.parent))

import random

def test_random_sampling():
    edges=set([1,2,3,4,5,6])
    for i in range(3):
        ele = random.sample(edges,1)
        print(ele)
        edges.remove(ele[0])
    print(edges)



#test_random_sampling()
#test_unionfind()
res=[0]

# open file and store data in a list
f = open("kargerMinCut.txt", "r")
etov={}
vtoe={}
numE=0
numV=0

testD=["1 4 2","2 1 4 3","3 2 4","4 1 2 3","5 1"]

for line in f:
    #print(line)
    tmp=line.split()
    for i in range(1,len(tmp)):
        key = (int(tmp[0]),int(tmp[i]))  
        if tmp[0]>tmp[i]:
            key = (int(tmp[i]),int(tmp[0]))
        if not vtoe.get(key):
            numE+=1
            vtoe[key]=numE
            etov[numE]=key
    numV+=1

print("total number of vertices:{}".format(numV))
print("total number of edges:{}".format(numE))
#print(etov)
edges=set([i+1 for i in range(numE)])

# constraction algorithm
num_loops = 1000
min_cuts = numE
for i in range(num_loops):
    num_remain_v=numV
    remain_edges=set(edges)
    uf=unionfind(numV)
    print("== Start contraction algorithm :{}==".format(i))
    while num_remain_v>2:
        #random sampling edge
        edge = (random.sample(remain_edges,1))[0]
        remain_edges.remove(edge)
        #print("sample edge {}".format(edge))

        vs=etov[edge]
        p1=uf.find(vs[0]-1)
        p2=uf.find(vs[1]-1)
        #print("get v1:{}, v2:{}".format(vs[0],vs[1]))

        if p1!=p2:
            uf.union(vs[0]-1,vs[1]-1)
            num_remain_v-=1
    #print("->start cleaning up edges")
    remove_edges=set([])
    for edge in remain_edges:
        vs=etov[edge]
        p1=uf.find(vs[0]-1)
        p2=uf.find(vs[1]-1)
    
        if p1==p2: remove_edges.add(edge)

    
    num_cuts=len(remain_edges)-len(remove_edges)
    print("num of remain_edges:{}".format(len(remain_edges)-len(remove_edges)))
    min_cuts=min(min_cuts,num_cuts)

print("min_cuts:{} get from num_loops:{}".format(min_cuts,num_loops))
#print(inputs)
#print(res)





