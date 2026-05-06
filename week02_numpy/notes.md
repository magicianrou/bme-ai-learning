# Week 02 Notes: NumPy Lesson 01

## 1. NumPy array 和 Python list 的区别

Python list 的乘法是重复列表，NumPy array 的乘法是对每个元素做数学运算。

## 2. shape

shape 表示数组的形状。例如一个 3x3 矩阵的 shape 是 (3, 3)。

## 3. dtype

dtype 表示数组内部元素的数据类型，例如 int32、float32。

## 4. indexing

matrix[1, 2] 表示第 1 行第 2 列的元素。

## 5. slicing

matrix[0:2, 0:2] 表示取第 0 到第 1 行、第 0 到第 1 列，也就是左上角 2x2 区域。

## 6. 在我的练习中如何使用

在 02_array_practice.py 中，我创建了一个 4x4 矩阵，并练习了取行、取列、取单个元素、取右下角区域和矩阵整体乘法。