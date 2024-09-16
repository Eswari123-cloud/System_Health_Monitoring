# plot/figures.py
import plotly.graph_objs as go
import numpy as np

def create_cpu_usage_figure(timestamps, cpu_usages, server_name):
    """Create a line chart for CPU usage."""
    return {
        'data': [
            go.Scatter(
                x=timestamps,
                y=cpu_usages,
                mode='lines+markers',
                name='CPU Usage'
            )
        ],
        'layout': go.Layout(
            title=f'CPU Usage Over Time ({server_name})',
            xaxis={'title': 'Time'},
            yaxis={'title': 'CPU Usage (%)'}
        )
    }

def create_memory_usage_figure(timestamps, memory_usages, server_name):
    """Create a line chart for Memory usage."""
    return {
        'data': [
            go.Scatter(
                x=timestamps,
                y=memory_usages,
                mode='lines+markers',
                name='Memory Usage'
            )
        ],
        'layout': go.Layout(
            title=f'Memory Usage Over Time ({server_name})',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Memory Usage (%)'}
        )
    }

def create_disk_usage_figure(timestamps, disk_usages, server_name):
    """Create a line chart for Disk usage."""
    return {
        'data': [
            go.Scatter(
                x=timestamps,
                y=disk_usages,
                mode='lines+markers',
                name='Disk Usage'
            )
        ],
        'layout': go.Layout(
            title=f'Disk Usage Over Time ({server_name})',
            xaxis={'title': 'Time'},
            yaxis={'title': 'Disk Usage (%)'}
        )
    }

def create_avg_usage_bar_chart(cpu_usages, memory_usages, disk_usages, server_name):
    """Create a bar chart for average CPU, memory, and disk usage."""
    avg_cpu_usage = np.mean(cpu_usages)
    avg_memory_usage = np.mean(memory_usages)
    avg_disk_usage = np.mean(disk_usages)
    
    return {
        'data': [
            go.Bar(
                x=['CPU Usage', 'Memory Usage', 'Disk Usage'],
                y=[avg_cpu_usage, avg_memory_usage, avg_disk_usage],
                name='Average Usage'
            )
        ],
        'layout': go.Layout(
            title=f'Average Usage Levels ({server_name})',
            xaxis={'title': 'Metric'},
            yaxis={'title': 'Average Usage (%)'}
        )
    }

def create_disk_usage_gauge_chart(avg_disk_usage, server_name):
    """Create a gauge chart for disk usage."""
    return {
        'data': [
            go.Indicator(
                mode='gauge+number',
                value=avg_disk_usage,
                gauge={'axis': {'range': [0, 100]}, 'bar': {'color': 'red'}}
            )
        ],
        'layout': go.Layout(
            title=f'Current Disk Usage ({server_name})'
        )
    }
