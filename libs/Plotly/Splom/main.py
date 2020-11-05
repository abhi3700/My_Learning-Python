'''
        Here, plot a diabetic 
        Reference: https://plotly.com/python/splom/#

'''

import plotly as py
import plotly.graph_objs as go
import pandas as pd

# ============================DATA==========================================
df = pd.read_csv("data/diabetes.csv")

# create a list with '0' as non-diabetic & '1' as diabetic
text_d = ['non-diabetic' if cl=0 else 'diabetic' for cl in df['Outcome']]

fig = go.Figure(data=go.Splom(
                        dimensions= [
                            dict(label='Pregnancies', values=df['Pregnancies']),
                            dict(label='Glucose', values=df['BloodPressure']),
                            dict(label='SkinThickness', values=df['SkinThickness']),
                            dict(label='Insulin', values=df['Insulin']),
                            dict(label='BMI', values=df['BMI']),
                            dict(label='DiabetesPedigreeFunction', values=df['DiabetesPedigreeFunction']),
                            dict(label='Age', values=df['Age'])],

    ))



