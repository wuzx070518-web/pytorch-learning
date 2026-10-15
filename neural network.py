import torch 
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1=nn.Conv2d(1,6,5)
        self.conv2=nn.Conv2d(6,16,5)
        self.fc1=nn.Linear(16*5*5,120)
        self.fc2=nn.Linear(120,84)
        self.fc3=nn.Linear(84,10)

    def forward(self,input):
        c1=F.relu(self.conv1(input))
        s2=F.max_pool2d(c1,(2,2))
        c3=F.relu(self.conv2(s2))
        s4=F.max_pool2d(c3,2)
        s4=torch.flatten(s4,1)
        f5=F.relu(self.fc1(s4))
        f6=F.relu(self.fc2(f5))
        output=self.fc3(f6)
        return output

net=Net()

# params=list(net.parameters())
# print(len(params))

# input=torch.rand(1,1,32,32)
# out=net(input)
# print(out)
x=torch.rand(1,1,32,32)


# net.zero_grad()
# out.backward(torch.randn(1,10))

output=net(x)
target=torch.randn(10)
target=target.view(1,-1)
criterion=nn.MSELoss()
loss=criterion(output,target)
print(loss)

net.zero_grad()
loss.backward()
print(net.conv1.bias.grad)

# 更新权重
# weight=weight-learning_rate*gradient
learning_rate=0.01
for f in net.parameters():
    with torch.no_grad():
        f-=f.grad*learning_rate

# 不同更新规则
# import torch.optim as optim
# optimizer=optim.SGD(net.parameters(),lr=0.01)
# optimizer.zero_grad()
# output=net(input)
# loss=criterion(output,target)
# loss.backward()
# optimizer.step()