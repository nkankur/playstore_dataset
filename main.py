import dash
import dash_core_components as dcc
import dash_html_components as html
from transform import AvgRating
import pandas as pd


df = pd.read_csv("Google-Playstore-32K.csv")
columns = list(df.columns)

df['Rating_validated'] = pd.to_numeric(df['Rating'], errors='coerce')

df_count_by_category = df.groupby('Category').mean().dropna(axis=0).sort_values('Rating_validated',ascending=False).head()

app = dash.Dash()

print(list(df_count_by_category.index))

app.layout = html.Div([
                    html.Div("Average Rating by Category"),
                    dcc.Graph(id='AvgRating',
                                figure=AvgRating(df_count_by_category,list(df_count_by_category.index), df_count_by_category['Rating_validated'], "Avg Rating"))
])



if __name__ == '__main__':
    app.run_server()
