## Installation
* `conda install matplotlib`

## Coding
* ### Import 
  ```py
  import matplotlib.pyplot as plt
  ```
* ### Plot `x` vs `y`
  **Code:**
  ```py
  plt.plot([1, 2, 3, 4])
  plt.ylabel('some numbers')
  plt.show()
  ```
  **Description:**
  - `y = [1, 2, 3, 4]`
  - `x = [0, 1, 2, 3]` (by default, starts with '0')
  
* ### Plot `x` vs `y` with both the data
  **Code:**  
  ```py
  plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
  plt.ylabel('square numbers')
  plt.show()
  ```
  **Description:**
  - `x = [1, 2, 3, 4]`
  - `y = [1, 4, 9, 16]`  
  
