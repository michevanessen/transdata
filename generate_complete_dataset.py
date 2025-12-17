import pandas as pd
import json
from datetime import datetime
import re

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

print("Building complete legislation dataset...")
print("=" * 60)

# Load existing 2025 data
df_2025 = pd.read_excel('anti_trans_legislation_2025.xlsx')
df_2025['Year'] = 2025

# Historical legislation data
historical_data = []

# 2020 Data
historical_data.extend([
    {
        "Legislation": "ID HB500 - Fairness in Women's Sports Act",
        "State/Federal": "ID",
        "Year": 2020,
        "Date": "2020-03-16",
        "Link": "https://legislature.idaho.gov/sessioninfo/2020/legislation/H0500/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Signed March 2020. Banned transgender girls and women from competing in women's sports. Later blocked by federal court injunction in August 2020."
    },
    {
        "Legislation": "ID - Birth certificate gender marker ban",
        "State/Federal": "ID",
        "Year": 2020,
        "Date": "2020-03-01",
        "Link": "https://www.nbcnews.com/feature/nbc-out/idaho-governor-signs-law-anti-transgender-legislation-n1172886",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Prohibited transgender people from changing sex on birth certificates. Struck down by federal court as unconstitutional."
    }
])

# 2021 Data
historical_data.extend([
    {
        "Legislation": "AR HB1570 - SAFE Act",
        "State/Federal": "AR",
        "Year": 2021,
        "Date": "2021-04-01",
        "Link": "https://www.arkleg.state.ar.us/Bills/Detail?id=HB1570&ddBienniumSession=2021%2F2021R",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "Vetoed (Override)",
        "Status Notes": "Vetoed by Governor Hutchinson in April 2021, but veto was overridden. First state to ban gender-affirming medical care for minors."
    },
    {
        "Legislation": "AR - Fairness in Women's Sports Act",
        "State/Federal": "AR",
        "Year": 2021,
        "Date": "2021-03-01",
        "Link": "https://www.arkleg.state.ar.us/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Signed March 2021. Bans transgender girls from sports that align with their gender identity, elementary through college."
    },
    {
        "Legislation": "MS - Mississippi Fairness Act",
        "State/Federal": "MS",
        "Year": 2021,
        "Date": "2021-03-11",
        "Link": "https://www.ms.gov/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Signed March 11, 2021. First statewide anti-trans law of 2021. Bans transgender girls and women from competing in women's sports."
    },
    {
        "Legislation": "TN - Anti-trans sports bill",
        "State/Federal": "TN",
        "Year": 2021,
        "Date": "2021-03-01",
        "Link": "https://www.tn.gov/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Signed March 2021. Requires students to prove assigned sex at birth to play in middle and high school sports."
    }
])

# 2022 Data
_2022_bills = [
    ("AL SB184", "AL", "Vulnerable Child Compassion and Protection Act - healthcare restrictions", "2022-04-08"),
    ("AL HB322", "AL", "Parental Rights in Education", None),
    ("AZ SB1138", "AZ", "Gender transition prohibition - healthcare", None),
    ("AZ HB2161", "AZ", "Parental Rights", None),
    ("AZ SB1399", "AZ", "Religious Exemptions for discrimination", None),
    ("FL H1557", "FL", "Parental Rights in Education (Don't Say Gay)", "2022-03-28"),
    ("GA HB1084", "GA", "Save Women's Sports Act", None),
    ("IA HF2416", "IA", "Save Women's Sports Act", None),
    ("IN HB1041", "IN", "Fairness in Women's Sports", None),
    ("KY SB83", "KY", "Fairness in Women's Sports Act", None),
    ("LA SB44", "LA", "Fairness in Women's Sports Act", None),
    ("LA HR158", "LA", "Gender-altering care study", None),
    ("OK SB2", "OK", "Save Women's Sports Act", None),
    ("OK SB1100", "OK", "Birth certificate restrictions - non-binary ban", None),
    ("SC H4608", "SC", "Save Women's Sports Act", None),
    ("SD SB46", "SD", "Fairness in Women's Sports", None),
    ("TN HB2316", "TN", "Sports participation restrictions", None),
    ("UT HB0011", "UT", "Transgender student participation restrictions", None),
]

for bill_num, state, description, date in _2022_bills:
    historical_data.append({
        "Legislation": f"{bill_num} - {description}",
        "State/Federal": state,
        "Year": 2022,
        "Date": date,
        "Link": "",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": f"Passed in 2022. {description}"
    })

# 2023 Data - Major passed bills
_2023_bills = [
    # Alabama
    ("AL HB261", "AL", "Sports - Prohibits biological males from athletic teams for females"),
    ("AL SB261", "AL", "Government contracts protection"),
    # Arkansas
    ("AR HB1156", "AR", "Public school student sex policies - bathrooms"),
    ("AR HB1468", "AR", "Given Name Act - restricts pronouns without parental consent"),
    ("AR HB1615", "AR", "Conscience Protection Act"),
    ("AR SB125", "AR", "Free speech at higher education"),
    ("AR SB199", "AR", "Protecting Minors From Medical Malpractice Act"),
    ("AR SB270", "AR", "Bathroom access - criminal amendments"),
    ("AR SB294", "AR", "LEARNS Act - education restrictions"),
    ("AR SB43", "AR", "Adult-oriented performance restrictions"),
    # Florida
    ("FL H1069", "FL", "Defines sex; revises instruction on reproductive health"),
    ("FL H1521", "FL", "Restroom and facility access based on sex"),
    ("FL S0254", "FL", "Prohibits sex-reassignment procedures for minors"),
    ("FL S0266", "FL", "Higher education board duties"),
    ("FL S1382", "FL", "Defense personnel recruitment principles"),
    # Georgia
    ("GA SB140", "GA", "Prohibits surgical procedures for gender dysphoria in minors"),
    # Iowa
    ("IA SF482", "IA", "Restroom access based on biological sex"),
    ("IA SF496", "IA", "Parental rights; prohibits gender identity instruction K-6"),
    ("IA SF538", "IA", "Restricts gender transition procedures for minors"),
    # Idaho
    ("ID H0071", "ID", "Vulnerable Child Protection Act"),
    ("ID S1016", "ID", "Restroom access for public works contractors"),
    ("ID S1100", "ID", "Privacy standards in public schools - bathrooms"),
    # Indiana
    ("IN HB1569", "IN", "Corrections restrictions on gender therapy"),
    ("IN HB1608", "IN", "No sexuality instruction pre-K-3; parental notification"),
    ("IN SB0480", "IN", "Prohibits gender transition for minors"),
    # Kansas
    ("KS HB2100", "KS", "Public Investments and Contracts Protection"),
    ("KS HB2138", "KS", "Separate accommodations by biological sex on trips"),
    ("KS HB2238", "KS", "Fairness in Women's Sports Act"),
    ("KS SB180", "KS", "Women's Bill of Rights - defines biological sex"),
    ("KS SB228", "KS", "County jail provisions"),
    # Kentucky
    ("KY SB145", "KY", "Interscholastic athletics eligibility"),
    ("KY SB150", "KY", "Parental notifications; pronoun restrictions"),
    # Louisiana
    ("LA HB648", "LA", "Prohibits procedures to alter sex of minors"),
    # Missouri
    ("MO HB15", "MO", "Appropriation bill with anti-trans provisions"),
    ("MO SB39", "MO", "Student athletic participation by sex"),
    ("MO SB49", "MO", "Missouri SAFE Act - healthcare restrictions"),
    # Mississippi
    ("MS HB1125", "MS", "REAP Act - regulates transgender procedures for minors"),
    # Montana
    ("MT HB234", "MT", "Obscene material dissemination laws"),
    ("MT HB303", "MT", "Medical Ethics and Diversity Act"),
    ("MT HB359", "MT", "Prohibits minors from attending drag shows"),
    ("MT HB361", "MT", "Name and sex usage not discrimination"),
    ("MT SB458", "MT", "Defines sex in Montana law"),
    ("MT SB518", "MT", "Parental involvement in education"),
    ("MT SB99", "MT", "Youth Health Protection Act"),
    # North Carolina
    ("NC H574", "NC", "Fairness in Women's Sports Act"),
    ("NC H808", "NC", "Gender transition restrictions for minors"),
    ("NC S49", "NC", "Parents' Bill of Rights"),
    # North Dakota
    ("ND HB1139", "ND", "Required elements of birth records"),
    ("ND HB1205", "ND", "Libraries restrict explicit sexual material"),
    ("ND HB1249", "ND", "Athletic teams designated by sex"),
    ("ND HB1254", "ND", "Prohibition of practices against minors - healthcare"),
    ("ND HB1297", "ND", "Birth record corrections/amendments"),
    ("ND HB1333", "ND", "Adult-oriented performance restrictions"),
    ("ND HB1473", "ND", "Restroom/locker room use by sex"),
    ("ND HB1474", "ND", "Defines female, male, and sex"),
    ("ND HB1489", "ND", "Higher ed athletic designations by sex"),
    ("ND HB1522", "ND", "Preferred pronouns restrictions"),
    ("ND HCR3010", "ND", "Urges schools to distinguish by biological sex"),
    # Nebraska
    ("NE LB574", "NE", "Let Them Grow Act and Preborn Child Protection"),
    # Oklahoma
    ("OK SB26", "OK", "School restroom/changing area designations"),
    ("OK SB404", "OK", "Oklahoma Religious Freedom Act"),
    ("OK SB613", "OK", "Prohibits gender transition for children"),
    # South Dakota
    ("SD HB1080", "SD", "Prohibits medical/surgical interventions on minors"),
    # Tennessee
    ("TN HB0001", "TN", "Prohibits medical procedures enabling inconsistent identity"),
    ("TN HB0009", "TN", "Adult cabaret performances viewable by minors offense"),
    ("TN HB0239", "TN", "Adds 'sex' as defined statutory term"),
    ("TN HB0306", "TN", "Private school athletic participation by biological sex"),
    ("TN HB0727", "TN", "Parental consent for school activities"),
    ("TN HB1269", "TN", "Teachers not required to use preferred pronouns"),
    ("TN SB0001", "TN", "Prohibits medical procedures for gender transition"),
    # Texas
    ("TX SB14", "TX", "Gender-affirming care restrictions for minors"),
    ("TX SB15", "TX", "Sports participation restrictions"),
    ("TX HB1686", "TX", "Parental rights and school policies"),
    # Utah
    ("UT HB257", "UT", "Gender transition modifications for minors"),
    ("UT SB16", "UT", "Sensitive materials in schools"),
    ("UT SB93", "UT", "School restroom and locker room amendments"),
    # West Virginia
    ("WV HB3042", "WV", "Save Women's Sports Bill"),
    ("WV SB252", "WV", "Prohibited medical procedures for minors"),
    # Wisconsin
    ("WI AB377", "WI", "Gender transition medical intervention for under 18"),
    # Wyoming
    ("WY SF0111", "WY", "Gender-affirming care classified as child abuse"),
    ("WY HB0004", "WY", "School bathroom access restrictions"),
]

for bill_num, state, description in _2023_bills:
    historical_data.append({
        "Legislation": f"{bill_num} - {description}",
        "State/Federal": state,
        "Year": 2023,
        "Date": None,
        "Link": "",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": f"Passed in 2023. {description}"
    })

# Create DataFrame from historical data
df_historical = pd.DataFrame(historical_data)

# Combine with 2025 data
df_combined = pd.concat([df_historical, df_2025], ignore_index=True)

# Extract dates if not already present
df_combined['Date'] = df_combined.apply(
    lambda row: row['Date'] if pd.notna(row.get('Date')) else extract_date(row.get('Status Notes')),
    axis=1
)

# Ensure all required columns exist
required_columns = ['Legislation', 'State/Federal', 'Year', 'Date', 'Link', 'Proposed', 'Passed', 'Denied/Vetoed', 'Status Notes']
for col in required_columns:
    if col not in df_combined.columns:
        df_combined[col] = None

df_combined = df_combined[required_columns]

# Sort by year (descending) and state
df_combined = df_combined.sort_values(by=['Year', 'State/Federal'], ascending=[False, True])

# Save to Excel
df_combined.to_excel('anti_trans_legislation_2025_with_dates.xlsx', index=False)

print(f"✓ Complete dataset created!")
print(f"\nData Summary:")
print(f"  2020: {len(df_combined[df_combined['Year'] == 2020])} bills")
print(f"  2021: {len(df_combined[df_combined['Year'] == 2021])} bills")
print(f"  2022: {len(df_combined[df_combined['Year'] == 2022])} bills")
print(f"  2023: {len(df_combined[df_combined['Year'] == 2023])} bills")
print(f"  2025: {len(df_combined[df_combined['Year'] == 2025])} bills")
print(f"\n  Total: {len(df_combined)} bills across {df_combined['Year'].nunique()} years")

# Generate JSON for website
legislation_data = df_combined.to_dict('records')

# Create state summary
state_summary = {}
for _, row in df_combined.iterrows():
    state = row['State/Federal']
    if state not in state_summary:
        state_summary[state] = {'total': 0, 'proposed': 0, 'passed': 0, 'denied': 0}
    state_summary[state]['total'] += 1
    if row['Proposed'] == 'Yes':
        state_summary[state]['proposed'] += 1
    if 'Yes' in str(row['Passed']):
        state_summary[state]['passed'] += 1
    if row['Denied/Vetoed'] not in ['No', '']:
        state_summary[state]['denied'] += 1

# Save JSON
output_data = {
    'legislation': legislation_data,
    'stateSummary': state_summary,
    'lastUpdated': datetime.now().strftime('%Y-%m-%d')
}

with open('legislation_data.json', 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"\n✓ JSON data generated: legislation_data.json")
print(f"✓ Excel file saved: anti_trans_legislation_2025_with_dates.xlsx")
print(f"\nReady to push to GitHub!")
