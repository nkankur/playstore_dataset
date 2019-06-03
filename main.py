import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()

app.layout = html.Div([
                    html.Div("Average Rating by Category"),
                    dcc.Graph(id='AvgRating',
                                figure={
                                'data' : 
                                })
])

if __name__ == '__main__':
    app.run_server()
