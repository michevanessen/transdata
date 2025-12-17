"""
Google Sheets Integration for Easy Data Updates

This script allows you to update your legislation tracker from a Google Sheet.

Setup Instructions:
1. Install required package: pip3 install gspread google-auth
2. Set up Google Sheets API credentials (see README_UPDATES.md)
3. Share your Google Sheet with the service account email
4. Update the SHEET_URL below with your Google Sheet URL
"""

import pandas as pd
import json
from datetime import datetime

# For Google Sheets integration (optional - requires setup)
try:
    import gspread
    from google.oauth2.service_account import Credentials
    GSPREAD_AVAILABLE = True
except ImportError:
    GSPREAD_AVAILABLE = False
    print("Google Sheets integration not available. Install with: pip3 install gspread google-auth")

# Configuration
SHEET_URL = "YOUR_GOOGLE_SHEET_URL_HERE"  # Replace with your Google Sheet URL
CREDENTIALS_FILE = "credentials.json"  # Google API credentials file

def load_from_google_sheets():
    """Load data from Google Sheets"""
    if not GSPREAD_AVAILABLE:
        print("Error: gspread not installed. Run: pip3 install gspread google-auth")
        return None

    try:
        # Authenticate with Google Sheets
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
        client = gspread.authorize(creds)

        # Open the spreadsheet
        sheet = client.open_by_url(SHEET_URL).sheet1

        # Get all values and convert to DataFrame
        data = sheet.get_all_records()
        df = pd.DataFrame(data)

        return df
    except FileNotFoundError:
        print(f"Error: {CREDENTIALS_FILE} not found. Please set up Google Sheets API credentials.")
        return None
    except Exception as e:
        print(f"Error loading from Google Sheets: {e}")
        return None

def load_from_excel(filename='anti_trans_legislation_2025_with_dates.xlsx'):
    """Load data from Excel file (fallback method)"""
    try:
        df = pd.read_excel(filename)
        return df
    except Exception as e:
        print(f"Error loading Excel file: {e}")
        return None

def save_data(df):
    """Save data to Excel and JSON"""
    if df is None or df.empty:
        print("Error: No data to save")
        return False

    try:
        # Ensure required columns exist
        required_columns = ['Legislation', 'State/Federal', 'Year', 'Date', 'Link',
                          'Proposed', 'Passed', 'Denied/Vetoed', 'Status Notes']

        for col in required_columns:
            if col not in df.columns:
                if col == 'Year':
                    df['Year'] = 2025
                elif col == 'Date':
                    df['Date'] = None
                else:
                    print(f"Error: Required column '{col}' missing from data")
                    return False

        # Reorder columns
        df = df[required_columns]

        # Save to Excel
        df.to_excel('anti_trans_legislation_2025_with_dates.xlsx', index=False)
        print("✓ Excel file updated")

        # Create JSON for website
        legislation_data = df.to_dict('records')

        # Create state summary
        state_summary = {}
        for _, row in df.iterrows():
            state = row['State/Federal']
            if state not in state_summary:
                state_summary[state] = {
                    'total': 0,
                    'proposed': 0,
                    'passed': 0,
                    'denied': 0
                }
            state_summary[state]['total'] += 1
            if row['Proposed'] == 'Yes':
                state_summary[state]['proposed'] += 1
            if 'Yes' in str(row['Passed']):
                state_summary[state]['passed'] += 1
            if 'Yes' in str(row['Denied/Vetoed']) or row['Denied/Vetoed'] not in ['No', '']:
                state_summary[state]['denied'] += 1

        # Save JSON
        output_data = {
            'legislation': legislation_data,
            'stateSummary': state_summary,
            'lastUpdated': datetime.now().strftime('%Y-%m-%d')
        }

        with open('legislation_data.json', 'w') as f:
            json.dump(output_data, f, indent=2)

        print("✓ JSON file updated")
        print(f"\nProcessed {len(df)} legislation items")
        return True

    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def main():
    print("Legislation Tracker Data Updater")
    print("=" * 50)

    # Try to load from Google Sheets first, fallback to Excel
    if GSPREAD_AVAILABLE and SHEET_URL != "YOUR_GOOGLE_SHEET_URL_HERE":
        print("\nAttempting to load from Google Sheets...")
        df = load_from_google_sheets()
    else:
        print("\nLoading from Excel file...")
        df = load_from_excel()

    if df is not None:
        print(f"Loaded {len(df)} rows")
        if save_data(df):
            print("\n✓ Update complete! Your website data has been refreshed.")
            print("  Push changes to GitHub to update the live site.")
        else:
            print("\n✗ Update failed")
    else:
        print("\n✗ Could not load data")

if __name__ == "__main__":
    main()
