import pandas as pd

# Read the existing Excel file
df = pd.read_excel('anti_trans_legislation_2025_with_dates.xlsx')

# Add Year column - all current bills are from 2025
df['Year'] = 2025

# Reorder columns to put Year after State/Federal
columns = ['Legislation', 'State/Federal', 'Year', 'Date', 'Link', 'Proposed', 'Passed', 'Denied/Vetoed', 'Status Notes']
df = df[columns]

# Save updated Excel file
df.to_excel('anti_trans_legislation_with_years.xlsx', index=False)
print("✓ Updated Excel file saved as: anti_trans_legislation_with_years.xlsx")
print(f"✓ Added Year column with value 2025 to all {len(df)} bills")

# Also update the original file
df.to_excel('anti_trans_legislation_2025_with_dates.xlsx', index=False)
print("✓ Updated anti_trans_legislation_2025_with_dates.xlsx with Year column")
