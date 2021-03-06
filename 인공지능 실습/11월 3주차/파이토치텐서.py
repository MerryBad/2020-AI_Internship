# -*- coding: utf-8 -*-
"""파이토치텐서.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VLLcLL-QqxkhPdynW7sYQ9qledugFWwQ
"""

import numpy as np
import torch
A = torch.tensor([[1., -1.], [1., -1.]])
print('A = ', A)
B = torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]))
print('B = ', B)
C = torch.rand(3,3)
print('C = ', C)
D = C.numpy()
print('D = ', D)
E = B.view(1,1,2,3)
print('E = ', E)
print('sum of A = ', A.sum())
print('mean of A = ', A.mean())