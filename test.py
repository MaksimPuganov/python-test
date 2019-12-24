from __future__ import print_function
import torch
x = torch.rand(5, 3).cuda()
print('out tensor -->', x)
print(' torch.cuda.is_available() -->', torch.cuda.is_available())