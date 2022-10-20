def merge_twosorted(A,B):
  c=[]
  a,b=0,0
  while a<len(A) and b<len(B):
    if A[a]<B[b]:
      c.append(A[a])
      a+=1
    else:
      c.append(B[b])
      b+=1
  if a<len(A):
   c.extend(A[a:])
  if b<len(B):
    c.extend(B[b:])
  return c


A=[2,5,6,9,10,15,18]
B=[1,4,5,8,12]
print(merge_twosorted(A,B))
