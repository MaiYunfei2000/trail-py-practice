import numpy as np

##### [Indexing — NumPy v1.17 Manual](https://docs.scipy.org/doc/numpy/user/basics.indexing.html)



#### Single element indexing

# https://docs.scipy.org/doc/numpy/user/basics.indexing.html#single-element-indexing

# Single element indexing for a 1-D array is what one expects. It work exactly like that for other standard Python sequences. It is 0-based, and accepts negative indices for indexing from the end of the array.

# 此时（1D情形）类似于list(range(10))
x = np.arange(10)
print(x)
print(x[2])
print(x[-2])

# Unlike lists and tuples, numpy arrays support multidimensional indexing for multidimensional arrays. That means that it is not necessary to separate each dimension’s index into its own set of square brackets.

# 只改变形状没改变
x.shape = (2, 5) # now x is 2-dimensional
print(x)
# 0轴第1个，1轴第3个；即第二行第四列
print(x[1,3])
print(x[1,-1])

# Note that if one indexes a multidimensional array with fewer indices than dimensions, one gets a subdimensional array. For example:

# x为2D数组，这样子调取了里面的一个1D数组
# It must be noted that the returned array is not a copy of the original, but points to the same values in memory as does the original array.
print(x[0])
# 注意两者的差别：
    # 前者是直接用坐标索引
    # 后者是调取子维度的数组，再对那个子数组进行索引
print(x[0,2], x[0][2])



# test 啊哈，果然跟MATLAB一样
print(x[:,0])
# 这样则不行了
print(x[:][0])

print()

#### Other indexing options

# https://docs.scipy.org/doc/numpy/user/basics.indexing.html#other-indexing-options

# It is possible to slice and stride arrays to extract arrays of the same number of dimensions, but of different sizes than the original. The slicing and striding works exactly the same way it does for lists and tuples except that they can be applied to multiple dimensions as well. A few examples illustrates best:

x = np.arange(10)
print(x)
# 前开，index2，第3位，数字为2；后闭，index5，第6位，数字5
print(x[2:5])
print(x[-7])
# 2为步长
print(x[1:7:2])

y = np.arange(35).reshape(5, 7)
print(y)

# 第0轴（行轴）：第1行至第4行，步长2 => 1、3行（二、四行）
# 第1轴（列轴）：整个轴（整列），步长3 => 0、3、6行
print(y[1:5:2,::3])

# Note that slices of arrays do not copy the internal array data but only produce new views of the original data. This is different from list or tuple slicing and an explicit copy() is recommended if the original data is not required anymore.
# 

#### Index arrays

# https://docs.scipy.org/doc/numpy/user/basics.indexing.html#index-arrays

# NumPy arrays may be indexed with other arrays (or any other sequence- like object that can be converted to an array, such as lists, with the exception of tuples; see the end of this document for why this is). The use of index arrays ranges from simple, straightforward cases to complex, hard-to-understand cases. For all cases of index arrays, what is returned is a copy of the original data, not a view as one gets for slices.

# Index arrays must be of integer type. Each value in the array indicates which value in the array to use in place of the index. To illustrate:
x = np.arange(10,1,-1)
print(x)
# x[a](x和a都是np数组)：返回一个与a同型的数组，数组的元素是以a的元素为索引的x的元素值
print(x[np.array([3, 3, 1, 8])])
# 相当于np.array(x[3], x[3], x[1], x[8])
# The index array consisting of the values 3, 3, 1 and 8 correspondingly create an array of length 4 (same as the index array) where each index is replaced by the value the index array has in the array being indexed.

# Negative values are permitted and work as they do with single indices or slices:
print(x[np.array([3, 3, -3, 8])])

# Generally speaking, what is returned when index arrays are used is an array with the same shape as the index array, but with the type and values of the array being indexed. As an example, we can use a multidimensional index array instead:
print(x[np.array([[1,1],[2,3]])])
# 那如果x是多维数组呢❓

#### Indexing Multi-dimensional arrays

# https://docs.scipy.org/doc/numpy/user/basics.indexing.html#indexing-multi-dimensional-arrays