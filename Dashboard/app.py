# app.py
from dash import Dash, dcc, html, Input, Output
import utils.db as db
import utils.data as data_gen
import plot.figures as plot

# Initialize the app
app = Dash(__name__)

# Load servers from the database
DATABASE_FILENAME = 'servers.db'
conn = db.connect_to_db(DATABASE_FILENAME)
servers = db.fetch_servers_from_db(conn)
conn.close()

# App layout
app.layout = html.Div([
    html.H1("Server Health Dashboard"),
    
    # Dropdown for selecting server
    dcc.Dropdown(
        id='server-dropdown',
        options=[{'label': server, 'value': server} for server in servers],
        value=servers[0] if servers else None  # Default value if servers are loaded
    ),
    
    # Graphs
    dcc.Graph(id='cpu-usage-line-chart'),
    dcc.Graph(id='memory-usage-line-chart'),
    dcc.Graph(id='disk-usage-line-chart'),
    dcc.Graph(id='cpu-memory-disk-bar-chart'),
    dcc.Graph(id='disk-usage-gauge-chart')
])

# Callback to update graphs based on selected server
@app.callback(
    [Output('cpu-usage-line-chart', 'figure'),
     Output('memory-usage-line-chart', 'figure'),
     Output('disk-usage-line-chart', 'figure'),
     Output('cpu-memory-disk-bar-chart', 'figure'),
     Output('disk-usage-gauge-chart', 'figure')],
    [Input('server-dropdown', 'value')]
)
def update_graphs(selected_server):
    if not selected_server:
        return {}, {}, {}, {}, {}  # Return empty figures if no server selected

    timestamps, cpu_usages, memory_usages, disk_usages = data_gen.generate_sample_data(selected_server)

    cpu_fig = plot.create_cpu_usage_figure(timestamps, cpu_usages, selected_server)
    memory_fig = plot.create_memory_usage_figure(timestamps, memory_usages, selected_server)
    disk_fig = plot.create_disk_usage_figure(timestamps, disk_usages, selected_server)
    bar_fig = plot.create_avg_usage_bar_chart(cpu_usages, memory_usages, disk_usages, selected_server)
    gauge_fig = plot.create_disk_usage_gauge_chart(np.mean(disk_usages), selected_server)

    return cpu_fig, memory_fig, disk_fig, bar_fig, gauge_fig

if __name__ == '__main__':
    app.run_server(debug=True)
