# Cloud Threat Detection Lab

This project demonstrates how to detect common threats in cloud environments using Python, Azure Sentinel, and log analysis.

## Features

- PowerShell abuse detection
- RDP brute force detection
- Azure sign-in anomaly alerts
- Integration with Azure Sentinel
- Optional Flask dashboard

## Folder Structure

- `detections/` — Python scripts to analyze logs
- `logs/` — Sample or synthetic logs for testing
- `sentinel-integration/` — KQL queries and Sentinel setup guides
- `reports/` — Detection results, screenshots, and documentation
- `dashboard/` — Flask app (optional)

## Getting Started

1. Create a `.env` file based on `.env.example`
2. Install dependencies: `pip install -r requirements.txt`
3. Run detection scripts from `detections/`
4. View logs or launch dashboard
