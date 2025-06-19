import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("=== NumPy Array Operations ===")
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", arr)

arr_transpose = arr.T
print("Transposed Array:\n", arr_transpose)

arr_sum = np.sum(arr)
print("Sum of all elements:", arr_sum)

print("\n=== Pandas DataFrame Operations ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 63, 91, 78]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

print("Basic statistics:\n", df.describe())

print("\n=== Matplotlib Plot ===")
plt.figure(figsize=(8, 5))
plt.plot(df['Name'], df['Score'], marker='o', linestyle='-', color='blue', label='Score')
plt.title('Scores by Person')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
