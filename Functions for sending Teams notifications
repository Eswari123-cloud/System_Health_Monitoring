import requests
import configparser

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

TEAMS_WEBHOOK_URL = config['teams']['WEBHOOK_URL']

def send_teams_notification(message, full_report=None, anomalies_detected=False):
    if not TEAMS_WEBHOOK_URL:
        print("Teams webhook URL not configured.")
        return

    headers = {
        "Content-Type": "application/json"
    }

    # Include anomaly detection status
    anomaly_status = "Anomalies detected." if anomalies_detected else "No anomalies detected."
    
    # If full report is provided, append it
    if full_report:
        message = f"{message} - {anomaly_status}. Full report: {full_report}"
    else:
        message = f"{message} - {anomaly_status}."

    payload = {
        "text": message
    }

    try:
        response = requests.post(TEAMS_WEBHOOK_URL, json=payload, headers=headers)
        response.raise_for_status()
        print("Teams notification sent.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Teams notification: {str(e)}")
