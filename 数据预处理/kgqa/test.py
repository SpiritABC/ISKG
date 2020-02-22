import torch
import numpy as np
from torch.autograd import Variable

tensor = torch.FloatTensor([[1, 2],[ 1, 2]])
variable = Variable(tensor, requires_grad=True)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

print(t_out)
print(v_out)

v_out.backward()
print(variable.grad)
print(variable.data)
print(variable.data.numpy())

# np_data = np.arange(6).reshape(2, 3)
# torch_data = torch.from_numpy(np_data)
# tensor2array = torch_data.numpy()
#
# print(
#     '\nnumpy',np_data,
#     '\ntorch', torch_data,
#     '\ntensor2array', tensor2array
# )

# data = [[1, 2],[ 1, 2]]
# data = np.array(data)
# tensor = torch.FloatTensor(data)
# print(np.matmul(data, data))
# print(torch.mm(tensor, tensor))
# print(data.dot(data))
# print(tensor.dot(tensor))