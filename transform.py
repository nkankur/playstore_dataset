import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("Google-Playstore-32K.csv")
columns = list(df.columns)

df['Rating_validated'] = pd.to_numeric(df['Rating'], errors='coerce')

df_count_by_category = df.groupby('Category').mean().dropna(axis=0).sort_values('Rating_validated',ascending=False).head()

def AvgRating (dataframe,x,y,title):
    x_value = x
    y_value = y

    return dict(data=[go.Bar(x=x_value, y=y_value)], layout=go.Layout(title=title))
