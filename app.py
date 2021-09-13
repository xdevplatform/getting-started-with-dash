import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import os
import requests

app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])

server = app.server

search_url = "https://api.twitter.com/2/tweets/counts/recent"
query_params = {"query": "from:jessicagarson", "granularity": "day"}


bearer_token = os.environ.get("BEARER_TOKEN")


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "GettingStartedDash"
    return r


def connect_to_endpoint(url, tweet_fields):
    response = requests.request("GET", url, auth=bearer_oauth, params=tweet_fields)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


json_response = connect_to_endpoint(search_url, query_params)


df = pd.DataFrame(json_response["data"])
df["start"] = pd.to_datetime(df["start"])

final = df[["start", "tweet_count"]]
fig = px.line(final, x="start", y="tweet_count")

colors = {"background": "#FFFFFF", "text": "#1DA1F2"}


fig.update_layout(
    plot_bgcolor=colors["background"],
    paper_bgcolor=colors["background"],
    font_color=colors["text"],
)

app.layout = html.Div(
    style={"backgroundColor": colors["background"]},
    children=[
        html.H1(
            children="Tweets by Date",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        html.Div(
            children="An example using Dash and the Twitter API recent search counts to see how much I've been Tweeting this week",
            style={"textAlign": "center", "color": colors["text"]},
        ),
        dcc.Graph(id="example-twitter", figure=fig),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
