import torch
tensor=torch.ones(4,4)
tensor[:,2]=0
# t1=torch.cat([tensor,tensor,tensor],dim=0)
# print(t1)

# tensor.mul(tensor)

#print(tensor.matmul(tensor.T))

#in_place operations: x.copy_(y),x.t_() change x

# print(tensor.add_(5))

# t=torch.ones(5)
# n=t.numpy()
# t.add_(1)
# print(t)
# print(n)
#对t的操作在n中会体现，所以存储的空间没变

