import matplotlib.pyplot as plt
import datetime

def plot_metrics(server_name, cpu_usages, memory_usages, disk_usages, cpu_anomalies, memory_anomalies, disk_anomalies):
    timestamps = [datetime.datetime.now() - datetime.timedelta(seconds=i*10) for i in range(len(cpu_usages))][::-1]

    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.plot(timestamps, cpu_usages, label='CPU Usage', color='blue')
    plt.scatter([timestamps[i] for i, anomaly in enumerate(cpu_anomalies) if anomaly],
                [cpu_usages[i] for i, anomaly in enumerate(cpu_anomalies) if anomaly],
                color='red', label='Anomalies')
    plt.ylabel('CPU Usage (%)')
    plt.legend()
    plt.title(f'System Health Report for {server_name}')

    plt.subplot(3, 1, 2)
    plt.plot(timestamps, memory_usages, label='Memory Usage', color='green')
    plt.scatter([timestamps[i] for i, anomaly in enumerate(memory_anomalies) if anomaly],
                [memory_usages[i] for i, anomaly in enumerate(memory_anomalies) if anomaly],
                color='red', label='Anomalies')
    plt.ylabel('Memory Usage (%)')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(timestamps, disk_usages, label='Disk Usage', color='orange')
    plt.scatter([timestamps[i] for i, anomaly in enumerate(disk_anomalies) if anomaly],
                [disk_usages[i] for i, anomaly in enumerate(disk_anomalies) if anomaly],
                color='red', label='Anomalies')
    plt.ylabel('Disk Usage (%)')
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'{server_name}_system_health_report.png')
    plt.close()
