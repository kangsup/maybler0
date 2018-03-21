
##1.5.1 Bringing the NumPy
import numpy as np
##1.5.2 Generating a NumPy array
x = np.array([1.0, 2.0, 3.0])
print(x)
type(x)

##1.5.3 NumPy Arithmetic Operations
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y # 원소별 덧셈 
x - y # 원소별 뺄셈
x * y # 원소별 곱셈
x / y # 원소별 나눗셈

x = np.array([1.0, 2.0, 3.0])
x / 2.0

##1.5.4 N-dimensional NumPy Array
A = np.array([[1, 2], [3, 4]])
print(A)
A.shape
A.dtype

C = np.array([[0, 1, 2], [3, 4, 5]])
print(C)
C.shape
C.dtype

B = np.array([[3, 0], [0, 6]])
A + B

A * B

print(A)
A * 10


##1.5.5 Broadcast in NumPy
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])

A * B


##1.5.6 Accessing any element of NumPy array
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)

X[0]

X[0][1]
### access by for loop
for row in X:
	print(row)
### Flattening the 2-dim array X into one-dim
X = X.flatten()
print(X)

X[np.array([0, 2, 4])]
### Poking specific elements by conditional index
X > 15

X[X > 15]


#1.6 Python's Graph Drawing: matplotlib
##1.6.1 Drawing a simple graph

import numpy as np
import matplotlib.pyplot as plt

# data preparation
x = np.arange(0, 6, 0.1) # generate from 0 to 6 by 0.1 intervals
y = np.sin(x)

# drawing the graph
plt.plot(x, y)
plt.show()

##1.6.2 matplotlib.pyplot module's functions
######### Sin & Cos Graph ###########
import numpy as np
import matplotlib.pyplot as plt

# data preparation
x = np.arange(0, 6.5, 0.1) # generate from 0 to 6 by 0.1 intervals
y1 = np.sin(x)
y2 = np.cos(x)

# drawing the graph
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos") #draw cosine function with dashed lines
plt.xlabel("x")  # name the x-axis 
plt.ylabel("y")  # name the y-axis 
plt.title("sin & cos") #title
plt.legend()

plt.show()

##1.6.3 Showing an image
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png') # Reading the image

plt.imshow(img)
plt.show()




#1.7 Ending words for further journey






