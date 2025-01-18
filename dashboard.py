
# /dashboard.py
import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go

# Example fungal strain data (mock data for demonstration)
prioritized_strains = [
    {"strain": "Pleurotus ostreatus", "score": 4.5},
    {"strain": "Ganoderma lucidum", "score": 3.0}
]

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("Strain Prioritization Dashboard"),
    dcc.Graph(
        id="strain-prioritization-chart",
        config={"displayModeBar": False},
    ),
    html.Div("Update the prioritization scores to see live changes."),
    dcc.Interval(
        id="interval-component",
        interval=5000,  # Update every 5 seconds
        n_intervals=0
    )
])

# Callback to update the chart
@app.callback(
    Output("strain-prioritization-chart", "figure"),
    [Input("interval-component", "n_intervals")]
)
def update_chart(n):
    # Fetch or simulate updated strain data
    scores = [strain["score"] for strain in prioritized_strains]
    names = [strain["strain"] for strain in prioritized_strains]

    # Create a bar chart
    fig = go.Figure([
        go.Bar(x=names, y=scores, text=scores, textposition="auto")
    ])
    fig.update_layout(
        title="Fungal Strain Prioritization",
        xaxis_title="Strains",
        yaxis_title="Priority Score",
        template="plotly_white"
    )
    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8050)
