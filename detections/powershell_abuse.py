import pandas as pd
import os

def detect_powershell_abuse(log_path):
    df = pd.read_csv(log_path)
    suspicious = df[df['command_line'].str.contains("powershell", case=False, na=False)]
    return suspicious

if __name__ == "__main__":
    log_file = os.getenv("LOG_DIR", "logs/") + "security_logs.csv"
    alerts = detect_powershell_abuse(log_file)
    print(alerts)
