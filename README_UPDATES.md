# How to Easily Update Your Legislation Tracker

This guide explains the easiest ways to add new legislation data to your tracker.

## Quick Overview

You have **three easy options** for updating data:

1. **Excel (Easiest)** - Edit the Excel file directly
2. **Google Sheets (Recommended)** - Edit online, sync with one command
3. **CSV Upload** - Export from any spreadsheet tool

---

## Option 1: Direct Excel Editing (Easiest)

### Steps:
1. Open `anti_trans_legislation_2025_with_dates.xlsx` in Excel, Numbers, or Google Sheets
2. Add new rows with legislation data
3. Fill in these columns:
   - **Legislation**: Bill name/number and title
   - **State/Federal**: State abbreviation (TX, CA, etc.) or "Federal"
   - **Year**: Year the bill was introduced (2020-2025)
   - **Date**: Leave blank (auto-extracted) or enter as YYYY-MM-DD
   - **Link**: URL to the bill
   - **Proposed**: "Yes" or "No"
   - **Passed**: "Yes", "No", "Pending", or "Yes (House)"
   - **Denied/Vetoed**: "No", "Vetoed", "Defeated", etc.
   - **Status Notes**: Description of current status

4. Save the file
5. Run the update script:
   ```bash
   python3 process_legislation.py
   ```

6. Push to GitHub:
   ```bash
   git add .
   git commit -m "Update legislation data"
   git push origin main
   ```

**Done!** Your website updates automatically.

---

## Option 2: Google Sheets Integration (Recommended for Teams)

This method lets multiple people update data online, then sync with one command.

### Initial Setup (One-Time):

1. **Create a Google Sheet**
   - Go to https://sheets.google.com
   - Create a new spreadsheet
   - Name it "Trans Legislation Tracker"

2. **Copy your existing data**
   - Open `anti_trans_legislation_2025_with_dates.xlsx`
   - Copy all data
   - Paste into your Google Sheet

3. **Set up Google Sheets API** (Optional - for automation)

   **Simple Method** (No API needed):
   - File → Download → Microsoft Excel (.xlsx)
   - Save as `anti_trans_legislation_2025_with_dates.xlsx`
   - Run `python3 process_legislation.py`

   **Advanced Method** (API automation):
   a. Go to https://console.cloud.google.com
   b. Create a new project
   c. Enable Google Sheets API
   d. Create credentials (Service Account)
   e. Download JSON credentials as `credentials.json`
   f. Share your Google Sheet with the service account email
   g. Update `SHEET_URL` in `update_from_sheets.py`
   h. Install packages:
      ```bash
      pip3 install gspread google-auth
      ```

### Daily Use:

**Simple Method:**
1. Edit your Google Sheet online
2. Download as Excel (.xlsx)
3. Run `python3 process_legislation.py`
4. Push to GitHub

**Advanced Method** (if API is set up):
1. Edit your Google Sheet online
2. Run: `python3 update_from_sheets.py`
3. Push to GitHub

---

## Option 3: Bulk Import from Research

### For importing data from tracking sites like translegislation.com:

1. **Export data to CSV**
   - Copy legislation data from source
   - Paste into Excel/Google Sheets
   - Format columns to match the structure above

2. **Save as Excel**
   - File → Save As → Excel Workbook
   - Name: `anti_trans_legislation_2025_with_dates.xlsx`

3. **Process and upload**
   ```bash
   python3 process_legislation.py
   git add .
   git commit -m "Bulk import: [description]"
   git push origin main
   ```

---

## Adding Historical Data (2020-2024)

### Best Sources for Historical Data:

1. **Trans Legislation Tracker** - https://translegislation.com/bills/[YEAR]
   - Most comprehensive
   - Years: 2023, 2024 available
   - Organized by state and category

2. **ACLU Tracker** - https://www.aclu.org/legislative-attacks-on-lgbtq-rights-2023
   - Well-documented
   - Includes vetoed bills

3. **Erin Reed's Tracker** - https://www.erininthemorning.com
   - Detailed status updates
   - Expert analysis

### How to Add Historical Bills:

1. Open the Excel file
2. Add new rows for each historical bill
3. **Important**: Set the **Year** column to the correct year (2020-2024)
4. Fill in all other columns as normal
5. Run `python3 process_legislation.py`
6. The year filter will automatically populate with all years in your data

---

## Column Reference

| Column | Required | Format | Examples |
|--------|----------|--------|----------|
| Legislation | Yes | Text | "H.R. 28 - Sports Act" |
| State/Federal | Yes | 2-letter or "Federal" | "TX", "CA", "Federal" |
| Year | Yes | 4-digit year | 2020, 2021, 2025 |
| Date | No | Auto or YYYY-MM-DD | "2025-01-14" or blank |
| Link | Yes | URL | "https://..." |
| Proposed | Yes | Yes/No | "Yes", "No" |
| Passed | Yes | Status text | "Yes", "No", "Pending" |
| Denied/Vetoed | Yes | Status text | "No", "Vetoed", "Defeated" |
| Status Notes | Yes | Text | Detailed description |

---

## Quick Commands Reference

```bash
# Update data after editing Excel
python3 process_legislation.py

# Update from Google Sheets (if configured)
python3 update_from_sheets.py

# Push to GitHub
git add .
git commit -m "Update legislation data"
git push origin main

# Check what changed
git status
git diff
```

---

## Tips for Efficient Updating

### Daily/Weekly Updates:
1. Keep your Google Sheet or Excel file open
2. Add new bills as you find them
3. At end of day: process and push

### Bulk Historical Imports:
1. Focus on one year at a time
2. Use the year filter to verify data
3. Start with most recent years (2024, 2023, etc.)

### Team Collaboration:
- Use Google Sheets for real-time collaboration
- Assign states to different team members
- Use comments in Google Sheets for questions

### Data Quality:
- Always include a source link
- Be specific in Status Notes
- Use consistent state abbreviations
- Double-check the year column

---

## Troubleshooting

**"Module not found" error:**
```bash
pip3 install pandas openpyxl
```

**Google Sheets not syncing:**
- Use the simple download method instead
- Check that credentials.json is in the folder
- Verify the sheet is shared with service account

**Website not updating:**
- Make sure you pushed to GitHub (`git push origin main`)
- Wait 1-2 minutes for GitHub Pages to rebuild
- Hard refresh your browser (Cmd+Shift+R)

**Year filter not showing new years:**
- Check the Year column has numeric values (not text)
- Run `python3 process_legislation.py` again
- Clear browser cache

---

## Need Help?

- Check that your Excel file has all required columns
- Make sure Year column contains numbers (2020-2025)
- Verify State/Federal uses 2-letter abbreviations
- Review `legislation_data.json` to see processed output

The system is designed to be flexible - as long as your Excel/Sheet has the right columns, it will work!
