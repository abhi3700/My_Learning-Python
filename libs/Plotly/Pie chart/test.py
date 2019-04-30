import pandas as pd
emission = pd.read_csv('data/emission.csv')
print(emission.to_string(index=False))