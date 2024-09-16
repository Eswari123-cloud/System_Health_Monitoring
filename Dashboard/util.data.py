# utils/data.py
import numpy as np
import pandas as pd

def generate_sample_data(server_name):
    """Generate sample data for a given server."""
    timestamps = pd.date_range(start="2024-09-01", periods=100, freq='h')
    cpu_usages = np.random.uniform(10, 90, size=len(timestamps))
    memory_usages = np.random.uniform(20, 80, size=len(timestamps))
    disk_usages = np.random.uniform(30, 70, size=len(timestamps))
    return timestamps, cpu_usages, memory_usages, disk_usages
