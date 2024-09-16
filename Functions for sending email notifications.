import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

EMAIL_SENDER = config['email']['EMAIL_SENDER']
EMAIL_RECEIVERS = config['email']['EMAIL_RECEIVER'].split(',')
SMTP_SERVER = config['email']['SMTP_SERVER']
SMTP_PORT = int(config['email']['SMTP_PORT'])
SMTP_USER = config['email']['SMTP_USER']
SMTP_PASSWORD = config['email']['SMTP_PASSWORD']

def send_report(subject, report, alerts, attachment_path=None, anomalies_detected=False):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = ", ".join(EMAIL_RECEIVERS)
    msg['Subject'] = subject

    # Add anomaly detection status
    anomaly_status = "Anomalies detected." if anomalies_detected else "No anomalies detected."
    report += f"\n\n{anomaly_status}"

    # Add report text if needed
    if report:
        msg.attach(MIMEText(report, 'plain'))

    # Add attachment if provided
    if attachment_path:
        try:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
                part['Content-Disposition'] = f'attachment; filename={os.path.basename(attachment_path)}'
                msg.attach(part)
        except Exception as e:
            print(f"Failed to attach file {attachment_path}: {str(e)}")

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
