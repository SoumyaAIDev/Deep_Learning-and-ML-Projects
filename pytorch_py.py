# -*- coding: utf-8 -*-
"""Pytorch.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15J9OvCAtIdC3RvUDBb7d9q4GP0t2aZIU
"""

import torch
x= torch.ones(2,2)
print(x.dtype)

import torch
x= torch.rand(2,2)
y= torch.rand(2,2)
y.add_(x)
print(y)

import torch
x=torch.rand(4,4)
print(x)
y=x.view(16)
print(y)

import torch
import numpy as np


a=torch.ones(5)
print(a)
b=a.numpy()
print(b)

a.add_(1)
print(a)

import pandas as pd
import torch

# Example pandas DataFrame
data = pd.DataFrame({
    'feature1': [1, 2, 3],
    'feature2': [4, 5, 6]
})

# Convert pandas DataFrame to a NumPy array
numpy_data = data.values

# Convert NumPy array to PyTorch tensor
tensor_data = torch.tensor(numpy_data, dtype=torch.float32)

print(tensor_data)

import tensorflow as tf
import numpy as np

# Generate some dummy data
X_train = np.random.rand(100, 3)  # 100 samples, 3 features
y_train = np.random.randint(2, size=(100, 1))  # Binary target (0 or 1)

# Define a simple neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(3,)),  # Input layer (3 features)
    tf.keras.layers.Dense(8, activation='relu'),                     # Hidden layer
    tf.keras.layers.Dense(1, activation='sigmoid')                   # Output layer (binary classification)
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10)

# Predict with the model
predictions = model.predict(X_train[:5])
print(predictions)

import torch
import numpy as np

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5,device=device)
    y = torch.ones(5)
    y = y.to(device)
    z = x+y
    z = z.to("cpu")

import torch
x = torch.randn(3,requires_grad=True)
print(x)

y=x+2
print(y)
z=y*y*2
z=z.mean()
print(z)

z.backward()
print(x.grad)

import torch

x = torch.randn(3,requires_grad=True)
print(x)

y =x+2
print(y)
z=y*y*2
print(z)

v=torch.tensor([0.1,0.1,0.001],dtype=torch.float32)
z.backward(v)
print(x.grad)