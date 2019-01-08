# `pandas`
## Installation
* `$ conda install pandas`

## Coding 
* ### Loading data using numpy
**Code:**
```py
data = np.array([['', 'Col1', 'Col2'],
               ['Row1', 1, 2],
               ['Row2', 3, 4]])

df = pd.DataFrame(data = data[1:, 1:],
                  index = data[1:, 0],
                  columns = data[0, 1:])
print(df)
```
**Output**:
```
     Col1 Col2
Row1    1    2
Row2    3    4
```

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
**Data:** [countries.csv](https://github.com/abhi3700/My_learning-Python/blob/master/data/countries.csv) <br/>
**Code**:
```py
data = pd.read_csv('countries.csv')
print(data)
print(data.head(6))		# head of the dataframe
print(data.tail(6))		# tail of the dataframe
```
<details>
    <summary><b>Output:<b></summary>
<p>
    
```
          country  year  population
0     Afghanistan  1952     8425333
1     Afghanistan  1957     9240934
2     Afghanistan  1962    10267083
3     Afghanistan  1967    11537966
4     Afghanistan  1972    13079460
5     Afghanistan  1977    14880372
6     Afghanistan  1982    12881816
7     Afghanistan  1987    13867957
8     Afghanistan  1992    16317921
9     Afghanistan  1997    22227415
10    Afghanistan  2002    25268405
11    Afghanistan  2007    31889923
12        Albania  1952     1282697
13        Albania  1957     1476505
14        Albania  1962     1728137
15        Albania  1967     1984060
16        Albania  1972     2263554
17        Albania  1977     2509048
18        Albania  1982     2780097
19        Albania  1987     3075321
20        Albania  1992     3326498
21        Albania  1997     3428038
22        Albania  2002     3508512
23        Albania  2007     3600523
24        Algeria  1952     9279525
25        Algeria  1957    10270856
26        Algeria  1962    11000948
27        Algeria  1967    12760499
28        Algeria  1972    14760787
29        Algeria  1977    17152804
...           ...   ...         ...
1674  Yemen, Rep.  1982     9657618
1675  Yemen, Rep.  1987    11219340
1676  Yemen, Rep.  1992    13367997
1677  Yemen, Rep.  1997    15826497
1678  Yemen, Rep.  2002    18701257
1679  Yemen, Rep.  2007    22211743
1680       Zambia  1952     2672000
1681       Zambia  1957     3016000
1682       Zambia  1962     3421000
1683       Zambia  1967     3900000
1684       Zambia  1972     4506497
1685       Zambia  1977     5216550
1686       Zambia  1982     6100407
1687       Zambia  1987     7272406
1688       Zambia  1992     8381163
1689       Zambia  1997     9417789
1690       Zambia  2002    10595811
1691       Zambia  2007    11746035
1692     Zimbabwe  1952     3080907
1693     Zimbabwe  1957     3646340
1694     Zimbabwe  1962     4277736
1695     Zimbabwe  1967     4995432
1696     Zimbabwe  1972     5861135
1697     Zimbabwe  1977     6642107
1698     Zimbabwe  1982     7636524
1699     Zimbabwe  1987     9216418
1700     Zimbabwe  1992    10704340
1701     Zimbabwe  1997    11404948
1702     Zimbabwe  2002    11926563
1703     Zimbabwe  2007    12311143

[1704 rows x 3 columns]
       country  year  population
0  Afghanistan  1952     8425333
1  Afghanistan  1957     9240934
2  Afghanistan  1962    10267083
3  Afghanistan  1967    11537966
4  Afghanistan  1972    13079460
5  Afghanistan  1977    14880372
       country  year  population
1698  Zimbabwe  1982     7636524
1699  Zimbabwe  1987     9216418
1700  Zimbabwe  1992    10704340
1701  Zimbabwe  1997    11404948
1702  Zimbabwe  2002    11926563
1703  Zimbabwe  2007    12311143
```

</p>
</details>
