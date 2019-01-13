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
  
* ### Plot linestyle, marker, color
  ```py
  plt.plot(df_er["Date (MM/DD/YY)"], df_er["Etch Rate (A/Min)"], linestyle='-', marker='o', color='b')
  
  ```
  [Reference](https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line/8409110#8409110)
