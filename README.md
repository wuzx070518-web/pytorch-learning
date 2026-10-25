# PyTorch 学习记录

这个仓库记录我学习 PyTorch 时编写的练习代码。目前主要围绕 Tensor 操作、自动微分、神经网络搭建，以及一个 CIFAR-10 图像分类练习。

## 已完成的练习

- **Tensor 基础**：创建张量，练习索引、拼接、原地运算，以及 Tensor 与 NumPy 数组的转换。
- **自动微分**：通过计算损失并调用 `backward()` 观察梯度；练习冻结已有参数和替换模型最后一层。
- **网络搭建**：使用 `nn.Module` 定义前向传播，将卷积、ReLU、最大池化、展平和全连接层连接起来。
- **训练流程**：练习损失函数、梯度清零、反向传播和优化器更新；在 CIFAR-10 上使用交叉熵损失与带动量的 SGD 训练一个简单卷积网络，并统计各类别的测试准确率。

## 代码索引

| 文件 | 内容 |
| --- | --- |
| `tensor/tensor_create.py` | Tensor 创建及与 NumPy 的转换 |
| `tensor/tensor_stack.py` | Tensor 索引、拼接与原地操作 |
| `autograd/train.py` | 自动微分和模型参数练习 |
| `neural network.py` | 卷积网络的前向传播、MSE 损失、反向传播与参数更新 |
| `classifier.py` | CIFAR-10 分类网络的训练、权重加载和分类评估 |

## 运行说明

代码使用 Python、PyTorch 和 torchvision；`classifier.py` 还使用 NumPy、Matplotlib。运行 `classifier.py` 时会下载 CIFAR-10：如果同目录下没有 `cifar_net.pt`，程序会训练两轮并保存权重；如果已有该文件，则加载权重并进行分类评估。数据和权重文件未纳入仓库。`autograd/train.py` 使用预训练 ResNet18，首次运行可能下载模型权重。

这些代码目前是用于理解和跑通基本机制的学习练习，尚未进行系统的超参数搜索或对照实验。
