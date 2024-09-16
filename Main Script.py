import datetime
from database import connect_to_db, fetch_servers_from_db
from utils import check_cpu_usage, check_memory_usage, check_disk_usage, check_network_connectivity, auto_cleanup, detect_anomalies, get_system_uptime
from plot import plot_metrics
from email_notifications import send_report
from teams_notifications import send_teams_notification

DATABASE_FILENAME = 'data/servers.db'

def monitor_server(server):
    hostname = server['hostname']
    ip_address = server['ip']

    alerts = []
    
    cpu_usage, cpu_status = check_cpu_usage()
    memory_usage, memory_status = check_memory_usage()
    disk_usage, disk_status = check_disk_usage()
    network_status = check_network_connectivity()
    cleanup_message = auto_cleanup()

    if cpu_usage is None or memory_usage is None or disk_usage is None:
        alerts.append(f"{hostname} ({ip_address}): Error checking system health.")
    else:
        if cpu_status == "High Usage":
            alerts.append(f"{hostname} ({ip_address}): CPU usage is high ({cpu_usage}%).")
        if memory_status == "High Usage":
            alerts.append(f"{hostname} ({ip_address}): Memory usage is high ({memory_usage}%).")
        if disk_status == "High Usage":
            alerts.append(f"{hostname} ({ip_address}): Disk usage is high ({disk_usage}%).")
        if network_status == "Issue: Unable to reach the internet":
            alerts.append(f"{hostname} ({ip_address}): Network connectivity issue.")
        if cleanup_message:
            alerts.append(cleanup_message)

    # Collect data for anomaly detection
    cpu_usages = [cpu_usage] * 10  # Example, replace with actual data
    memory_usages = [memory_usage] * 10  # Example, replace with actual data
    disk_usages = [disk_usage] * 10  # Example, replace with actual data

    cpu_anomalies = detect_anomalies(cpu_usages)
    memory_anomalies = detect_anomalies(memory_usages)
    disk_anomalies = detect_anomalies(disk_usages)

    # Plot metrics
    plot_metrics(hostname, cpu_usages, memory_usages, disk_usages, cpu_anomalies, memory_anomalies, disk_anomalies)

    # Send notifications and reports
    full_report = f"Hostname: {hostname}\nIP Address: {ip_address}\nCPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}%\nDisk Usage: {disk_usage}%\nNetwork Status: {network_status}\nCleanup: {cleanup_message if cleanup_message else 'None'}"
    send_report(subject=f"System Health Report - {hostname}", report="\n".join(alerts), alerts=alerts, attachment_path=f"{hostname}_system_health_report.png", anomalies_detected=any(cpu_anomalies + memory_anomalies + disk_anomalies))
    send_teams_notification(message=f"System health report for {hostname}", full_report=full_report, anomalies_detected=any(cpu_anomalies + memory_anomalies + disk_anomalies))

def generate_month_end_report():
    # Your implementation for generating the monthly report
    # Combine all server reports into a single Excel sheet and send it via email
    pass

def is_last_day_of_month(date):
    next_day = date + datetime.timedelta(days=1)
    return next_day.month != date.month

# Main script
if __name__ == "__main__":
    today = datetime.datetime.now()
    
    # Load servers from SQLite database
    conn = connect_to_db(DATABASE_FILENAME)
    SERVERS = fetch_servers_from_db(conn)
    conn.close()
    
    # Monitor each server
    for server in SERVERS:
        monitor_server(server)
    
    # Generate month-end report if today is the last day of the month
    if is_last_day_of_month(today):
        generate_month_end_report()
