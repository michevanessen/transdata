import pandas as pd
import re
from datetime import datetime

# Read the Excel file
df = pd.read_excel('anti_trans_legislation_2025.xlsx')

# Function to extract dates from Status Notes
def extract_date(status_notes):
    """Extract dates from status notes text."""
    if pd.isna(status_notes):
        return None

    text = str(status_notes)

    # Common date patterns (in order of specificity)
    patterns = [
        # Full date with day: Jan 14, 2025 or Jan. 14, 2025
        (r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4}',
         ['%b %d, %Y', '%b. %d, %Y', '%b %d %Y', '%B %d, %Y', '%B. %d, %Y', '%B %d %Y']),
        # Numeric date: 1/14/2025
        (r'\d{1,2}/\d{1,2}/\d{4}', ['%m/%d/%Y']),
        # ISO date: 2025-01-14
        (r'\d{4}-\d{2}-\d{2}', ['%Y-%m-%d']),
        # Month and year only: May 2025
        (r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}',
         ['%b %Y', '%b. %Y', '%B %Y', '%B. %Y']),
    ]

    for pattern, formats in patterns:
        match = re.search(pattern, text)
        if match:
            date_str = match.group(0)
            # Try to parse the date
            for fmt in formats:
                try:
                    parsed_date = datetime.strptime(date_str.replace(',', ''), fmt)
                    return parsed_date.strftime('%Y-%m-%d')
                except ValueError:
                    continue

    return None

# Extract dates and add to DataFrame
df['Date'] = df['Status Notes'].apply(extract_date)

# Reorder columns to put Date after State/Federal
columns = ['Legislation', 'State/Federal', 'Date', 'Link', 'Proposed', 'Passed', 'Denied/Vetoed', 'Status Notes']
df = df[columns]

# Save updated Excel file
df.to_excel('anti_trans_legislation_2025_with_dates.xlsx', index=False)
print("✓ Updated Excel file saved as: anti_trans_legislation_2025_with_dates.xlsx")

# Convert to JSON for web use
legislation_data = df.to_dict('records')

# Create a summary by state
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
    if 'Yes' in str(row['Denied/Vetoed']):
        state_summary[state]['denied'] += 1

# Create final JSON structure
output_data = {
    'legislation': legislation_data,
    'stateSummary': state_summary,
    'lastUpdated': datetime.now().strftime('%Y-%m-%d')
}

import json
with open('legislation_data.json', 'w') as f:
    json.dump(output_data, f, indent=2)

print("✓ JSON data saved as: legislation_data.json")
print(f"\nProcessed {len(df)} legislation items across {len(state_summary)} states/federal")
print(f"Dates extracted for {df['Date'].notna().sum()} items")
