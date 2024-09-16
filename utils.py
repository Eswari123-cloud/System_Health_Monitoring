import psutil
import datetime
import socket
import shutil
import os
from scipy.stats import zscore

# Thresholds
THRESHOLD_CPU = 95
THRESHOLD_MEMORY = 80
THRESHOLD_DISK = 90
DISK_CLEANUP_THRESHOLD = 90

def detect_anomalies(data_series):
    if len(data_series) < 3:
        return [False] * len(data_series)  # Not enough data to compute anomalies
    z_scores = zscore(data_series)
    return [abs(z) > 2 for z in z_scores]  # Flag as anomaly if Z-score is greater than 2

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    status = "High Usage" if cpu_usage > THRESHOLD_CPU else "Normal"
    return cpu_usage, status

def check_memory_usage():
    memory_usage = psutil.virtual_memory().percent
    status = "High Usage" if memory_usage > THRESHOLD_MEMORY else "Normal"
    return memory_usage, status

def check_disk_usage(disk_path='/'):
    try:
        disk_usage = psutil.disk_usage(disk_path).percent
        status = "High Usage" if disk_usage > THRESHOLD_DISK else "Normal"
        return disk_usage, status
    except Exception as e:
        return None, f"Disk Usage check failed: {str(e)}"

def auto_cleanup(directory='C:\\Temp', threshold=90):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return None

    disk_usage = psutil.disk_usage(directory).percent
    if disk_usage > threshold:
        shutil.rmtree(directory)
        os.makedirs(directory)
        return f"Auto Cleanup performed on {directory} due to high disk usage."
    return None

def check_network_connectivity(host='google.com', port=80, timeout=3):
    try:
        socket.create_connection((host, port), timeout)
        return "OK"
    except OSError:
        return "Issue: Unable to reach the internet"

def get_system_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    days, seconds = uptime.days, uptime.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{days} days, {hours} hours, {minutes} minutes"
