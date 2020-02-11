
class Node:

    def __init__(self,values, l, r):
        self.l = l
        self.r = r
        if l == r:
            self.val = values[l]
        else:
            mid = (l+r)//2
            self.left = Node(values,l,mid)
            self.right = Node(values,mid+1,r)
            self.val = self.left.val + self.right.val 
        #print(self.val)

    def query_max(self,L,R):
        if L > self.r or R < self.l: return 0
        if L <= self.l and R >= self.r: return self.val

        return self.left.query_max(L,R) + self.right.query_max(L,R)

arr = [5,6,7,4,1,2] 

parent = Node(arr,0,5)

print(parent.query_max(1,3))












