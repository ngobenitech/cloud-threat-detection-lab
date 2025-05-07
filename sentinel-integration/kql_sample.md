# Azure Sentinel Integration

## Sample KQL Query for PowerShell Abuse
```kql
SecurityEvent
| where CommandLine contains "powershell"
| summarize count() by Account, Computer, bin(TimeGenerated, 1h)
```
