# `pandas`
## Installation
* `$ conda install pandas`

## Coding 
* ### Loading from a dictionary
**Code:**
```py
dict = {"Litho": ["Verma", "Raja", "Tiwari", "Arpit", "Meena", "Shashikant", "Amit"],
        "Dry": ["Anuvesh", "Vijay", "Zaheer", "Girish", "Abhijit", "Abhishek", ""],
        "ThinFilm": ["Mk Singh", "Luxmi", "Tarun Malviya", "Sunil", "Surya", "", ""],
        "Diffusion": ["Mahesh", "Ravi", "Harmeet", "Deeconda", "", "", ""]
            
}
df = pd.DataFrame(dict)
# df = df.replace(r'^\s*$', np.nan, regex=True)	# replacing the empty box and spaces with NaN using numpy library
print(df)
```
**Output:**
```
       Litho       Dry       ThinFilm Diffusion
0       Verma   Anuvesh       Mk Singh    Mahesh
1        Raja     Vijay          Luxmi      Ravi
2      Tiwari    Zaheer  Tarun Malviya   Harmeet
3       Arpit    Girish          Sunil  Deeconda
4       Meena   Abhijit          Surya          
5  Shashikant  Abhishek                         
6        Amit                                   
```

* ### Loading from a `.csv` file
