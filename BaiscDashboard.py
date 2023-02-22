import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, suppress_callback_exceptions=True)

data = pd.read_csv("Data/Data - DS C1 Course.csv")

fig = px.bar(data, x="Age", y="Are you currently attending University / College?", color="Payment", barmode="group")
fig2 = data ["Are you currently attending University / College?"].value_counts().plot(kind="pie")
app.layout = html.Div(children=[
    html.H1('Course Dashboard'),
    dcc.Graph(
        id='graph1',
        figure=fig
    ), 
    dcc.Graph(
        id='graph1',
        figure=fig2
    )

])

if __name__ == '__main__':
    app.run_server(host='localhost',port=8005)


