import dash
import dash_core_components as dcc
import dash_html_components as html
from transform import df_count_by_category
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input,Output

app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='graph')])

@app.callback(Output('graph','figure'), Input)
def AvgRating():
    trace = [go.Bar(x=list(df_count_by_category.index), y=list(df_count_by_category['Rating_validated']))]
    print(go)
    print(trace)
    return {'data': trace,
                'layout': go.Layout(title='Hope this works') }





if __name__ == '__main__':
    app.run_server()
