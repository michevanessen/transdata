import pandas as pd
from datetime import datetime

# Historical legislation data compiled from translegislation.com and other sources
# This includes passed bills from 2020-2024

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
        "Legislation": "AR HB1570 - SAFE Act (Save Adolescents From Experimentation)",
        "State/Federal": "AR",
        "Year": 2021,
        "Date": "2021-04-01",
        "Link": "https://www.arkleg.state.ar.us/Bills/Detail?id=HB1570&ddBienniumSession=2021%2F2021R",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "Vetoed (Override)",
        "Status Notes": "Vetoed by Governor Hutchinson in April 2021, but veto was overridden by legislature. First state to ban gender-affirming medical care for minors including puberty blockers, hormone therapy, and surgery."
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
        "Status Notes": "Signed March 2021. Bans transgender girls from participating in sports teams that align with their gender identity from elementary through college."
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
        "Status Notes": "Signed March 11, 2021. First statewide anti-trans law of 2021. Bans transgender girls and women from competing in women's sports at public schools and colleges."
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
        "Status Notes": "Signed by Gov. Bill Lee March 2021. Requires students to prove assigned sex at birth to play in middle and high school sports."
    }
])

# 2022 Data
historical_data.extend([
    {
        "Legislation": "AL SB184 - Vulnerable Child Compassion and Protection Act",
        "State/Federal": "AL",
        "Year": 2022,
        "Date": "2022-04-08",
        "Link": "https://legiscan.com/AL/text/SB184/2022",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Signed April 2022. Imposed criminal penalties on healthcare providers for providing gender-affirming care to minors."
    },
    {
        "Legislation": "AL HB322 - Parental Rights in Education",
        "State/Federal": "AL",
        "Year": 2022,
        "Date": None,
        "Link": "https://legiscan.com/AL/bill/HB322/2022",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Parental rights law restricting discussion of gender identity and sexual orientation in schools."
    },
    {
        "Legislation": "AZ SB1138 - Gender transition prohibition",
        "State/Federal": "AZ",
        "Year": 2022,
        "Date": None,
        "Link": "https://www.azleg.gov/legtext/55leg/2R/bills/SB1138S.pdf",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Anti-trans healthcare restrictions."
    },
    {
        "Legislation": "AZ HB2161 - Parental Rights",
        "State/Federal": "AZ",
        "Year": 2022,
        "Date": None,
        "Link": "https://www.azleg.gov/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Parental rights law."
    },
    {
        "Legislation": "AZ SB1399 - Religious Exemptions",
        "State/Federal": "AZ",
        "Year": 2022,
        "Date": None,
        "Link": "https://www.azleg.gov/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Allows religious exemptions for discrimination."
    },
    {
        "Legislation": "FL H1557 - Parental Rights in Education (Don't Say Gay)",
        "State/Federal": "FL",
        "Year": 2022,
        "Date": "2022-03-28",
        "Link": "https://www.flsenate.gov/Session/Bill/2022/1557",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Signed March 28, 2022. Restricts classroom discussion of sexual orientation and gender identity in K-3 and beyond without parental consent."
    },
    {
        "Legislation": "GA HB1084 - Save Women's Sports Act",
        "State/Federal": "GA",
        "Year": 2022,
        "Date": None,
        "Link": "https://www.legis.ga.gov/legislation/60459",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Segregates sports by biological sex assigned at birth."
    },
    {
        "Legislation": "IA HF2416 - Save Women's Sports Act",
        "State/Federal": "IA",
        "Year": 2022,
        "Date": None,
        "Link": "https://www.legis.iowa.gov/legislation/BillBook?ga=89&ba=HF2416",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports participation restrictions based on biological sex."
    },
    {
        "Legislation": "IN HB1041 - Fairness in Women's Sports",
        "State/Federal": "IN",
        "Year": 2022,
        "Date": None,
        "Link": "http://iga.in.gov/legislative/2022/bills/house/1041",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports ban based on biological sex."
    },
    {
        "Legislation": "KY SB83 - Fairness in Women's Sports Act",
        "State/Federal": "KY",
        "Year": 2022,
        "Date": None,
        "Link": "https://apps.legislature.ky.gov/record/22rs/sb83.html",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports participation restrictions."
    },
    {
        "Legislation": "LA SB44 - Fairness in Women's Sports Act",
        "State/Federal": "LA",
        "Year": 2022,
        "Date": None,
        "Link": "https://legis.la.gov/legis/BillInfo.aspx?s=22RS&b=SB44",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports segregation by biological sex."
    },
    {
        "Legislation": "LA HR158 - Gender-altering care study",
        "State/Federal": "LA",
        "Year": 2022,
        "Date": None,
        "Link": "https://legis.la.gov/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Commissioned study on risks of gender-affirming care."
    },
    {
        "Legislation": "OK SB2 - Save Women's Sports Act",
        "State/Federal": "OK",
        "Year": 2022,
        "Date": None,
        "Link": "http://www.oklegislature.gov/BillInfo.aspx?Bill=sb2&Session=2200",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Segregates sports by biological sex assigned at birth."
    },
    {
        "Legislation": "OK SB1100 - Birth certificate restrictions",
        "State/Federal": "OK",
        "Year": 2022,
        "Date": None,
        "Link": "http://www.oklegislature.gov/",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Prohibited non-binary birth certificates."
    },
    {
        "Legislation": "SC H4608 - Save Women's Sports Act",
        "State/Federal": "SC",
        "Year": 2022,
        "Date": None,
        "Link": "https://www.scstatehouse.gov/sess124_2021-2022/bills/4608.htm",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports segregation by biological sex."
    },
    {
        "Legislation": "SD SB46 - Fairness in Women's Sports",
        "State/Federal": "SD",
        "Year": 2022,
        "Date": None,
        "Link": "https://sdlegislature.gov/Session/Bill/23492",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports participation restrictions."
    },
    {
        "Legislation": "TN HB2316 - Sports participation restrictions",
        "State/Federal": "TN",
        "Year": 2022,
        "Date": None,
        "Link": "https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB2316",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Fairness in Women's Sports Act."
    },
    {
        "Legislation": "UT HB0011 - Transgender student participation restrictions",
        "State/Federal": "UT",
        "Year": 2022,
        "Date": None,
        "Link": "https://le.utah.gov/~2022/bills/static/HB0011.html",
        "Proposed": "Yes",
        "Passed": "Yes",
        "Denied/Vetoed": "No",
        "Status Notes": "Sports ban for transgender students."
    }
])

# 2023 Data - Major bills (comprehensive list from web scraping)
_2023_bills = [
    # Alabama
    ("AL HB261", "AL", "Sports - Prohibits biological males from athletic teams designated for females"),
    ("AL SB261", "AL", "Government contracts protection regarding boycotts"),

    # Arkansas
    ("AR HB1156", "AR", "Public school student sex policies - bathrooms"),
    ("AR HB1468", "AR", "Given Name Act - restricts pronoun usage without parental consent"),
    ("AR HB1615", "AR", "Conscience Protection Act"),
    ("AR SB125", "AR", "Free speech at higher education institutions"),
    ("AR SB199", "AR", "Protecting Minors From Medical Malpractice Act - healthcare restrictions"),
    ("AR SB270", "AR", "Bathroom access - criminal offense amendments"),
    ("AR SB294", "AR", "LEARNS Act - education restrictions"),
    ("AR SB43", "AR", "Adult-oriented performance restrictions"),

    # Florida
    ("FL H1069", "FL", "Defines sex; revises instruction on reproductive health and human sexuality"),
    ("FL H1521", "FL", "Restroom and facility access based on sex"),
    ("FL S0254", "FL", "Prohibits sex-reassignment procedures for minors under 18"),
    ("FL S0266", "FL", "Higher education board duties regarding certain expenditures"),
    ("FL S1382", "FL", "Department of Defense personnel recruitment principles"),

    # Georgia
    ("GA SB140", "GA", "Prohibits certain surgical procedures for gender dysphoria in minors"),

    # Iowa
    ("IA SF482", "IA", "Restroom access based on biological sex in schools"),
    ("IA SF496", "IA", "Parental rights; prohibits gender identity/sexual orientation instruction K-6"),
    ("IA SF538", "IA", "Restricts gender transition procedures for minors"),

    # Idaho
    ("ID H0071", "ID", "Vulnerable Child Protection Act"),
    ("ID S1016", "ID", "Restroom access based on sex for public works contractors"),
    ("ID S1100", "ID", "Privacy and safety standards in public schools - bathrooms"),

    # Indiana
    ("IN HB1569", "IN", "Department of Correction restrictions on gender therapy"),
    ("IN HB1608", "IN", "No human sexuality instruction pre-K-3; parental notification of name/pronoun changes"),
    ("IN SB0480", "IN", "Prohibits gender transition procedures for minors under 18"),

    # Kansas
    ("KS HB2100", "KS", "Kansas Public Investments and Contracts Protection Act"),
    ("KS HB2138", "KS", "Separate accommodations by biological sex on school trips"),
    ("KS HB2238", "KS", "Fairness in Women's Sports Act"),
    ("KS SB180", "KS", "Women's Bill of Rights - defines biological sex"),
    ("KS SB228", "KS", "County jail provisions"),

    # Kentucky
    ("KY SB145", "KY", "Interscholastic athletics eligibility modifications"),
    ("KY SB150", "KY", "Parental notifications; pronoun usage restrictions; parental rights procedures"),

    # Louisiana
    ("LA HB648", "LA", "Prohibits certain procedures to alter sex of minors"),

    # Missouri
    ("MO HB15", "MO", "Appropriation bill with anti-trans provisions"),
    ("MO SB39", "MO", "Guidelines for student athletic participation by sex"),
    ("MO SB49", "MO", "Missouri SAFE Act - restricts gender transition procedure funding"),

    # Mississippi
    ("MS HB1125", "MS", "REAP Act - regulates transgender procedures and surgeries for minors"),

    # Montana
    ("MT HB234", "MT", "Revises obscene material dissemination laws"),
    ("MT HB303", "MT", "Medical Ethics and Diversity Act"),
    ("MT HB359", "MT", "Prohibits minors from attending drag shows"),
    ("MT HB361", "MT", "Name and sex usage not discrimination"),
    ("MT SB458", "MT", "Defines sex in Montana law"),
    ("MT SB518", "MT", "Increases parental involvement in education"),
    ("MT SB99", "MT", "Youth Health Protection Act"),

    # North Carolina
    ("NC H574", "NC", "Fairness in Women's Sports Act"),
    ("NC H808", "NC", "Gender transition restrictions for minors"),
    ("NC S49", "NC", "Parents' Bill of Rights"),

    # North Dakota
    ("ND HB1139", "ND", "Required elements of birth records"),
    ("ND HB1205", "ND", "Public libraries restrict explicit sexual material"),
    ("ND HB1249", "ND", "Athletic teams designated by sex"),
    ("ND HB1254", "ND", "Prohibition of certain practices against minors - healthcare"),
    ("ND HB1297", "ND", "Birth record corrections/amendments"),
    ("ND HB1333", "ND", "Adult-oriented performance restrictions"),
    ("ND HB1473", "ND", "Restroom/locker room use by sex in state facilities"),
    ("ND HB1474", "ND", "Defines female, male, and sex"),
    ("ND HB1489", "ND", "Higher education athletic team designations by sex"),
    ("ND HB1522", "ND", "Preferred pronouns restrictions"),
    ("ND HCR3010", "ND", "Urges schools to distinguish by biological sex"),

    # Nebraska
    ("NE LB574", "NE", "Let Them Grow Act and Preborn Child Protection Act"),

    # Oklahoma
    ("OK SB26", "OK", "School restroom/changing area designations"),
    ("OK SB404", "OK", "Oklahoma Religious Freedom Act"),
    ("OK SB613", "OK", "Prohibits gender transition procedures for children"),

    # South Dakota
    ("SD HB1080", "SD", "Prohibits medical/surgical interventions on minor patients"),

    # Tennessee
    ("TN HB0001", "TN", "Prohibits medical procedures enabling identity inconsistent with sex"),
    ("TN HB0009", "TN", "Creates offense for adult cabaret performances viewable by minors"),
    ("TN HB0239", "TN", "Adds 'sex' as defined statutory term"),
    ("TN HB0306", "TN", "Private school athletic participation by biological sex"),
    ("TN HB0727", "TN", "Requires parental consent for certain school activities"),
    ("TN HB1269", "TN", "Specifies teachers not required to use preferred pronouns"),
    ("TN SB0001", "TN", "Prohibits medical procedures enabling identity inconsistent with sex"),

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
    ("WV SB252", "WV", "Relating to prohibited medical procedures for minors"),

    # Wisconsin
    ("WI AB377", "WI", "Relating to gender transition medical intervention for individuals under 18"),

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

# Create DataFrame
df_historical = pd.DataFrame(historical_data)

# Load existing 2025 data
df_2025 = pd.read_excel('anti_trans_legislation_2025_with_dates.xlsx')

# Combine all data
df_combined = pd.concat([df_historical, df_2025], ignore_index=True)

# Sort by year (descending) and state
df_combined = df_combined.sort_values(by=['Year', 'State/Federal'], ascending=[False, True])

# Save combined file
df_combined.to_excel('anti_trans_legislation_2025_with_dates.xlsx', index=False)

print("✓ Historical data compilation complete!")
print(f"\nData Summary:")
print(f"  2020: {len(df_combined[df_combined['Year'] == 2020])} bills")
print(f"  2021: {len(df_combined[df_combined['Year'] == 2021])} bills")
print(f"  2022: {len(df_combined[df_combined['Year'] == 2022])} bills")
print(f"  2023: {len(df_combined[df_combined['Year'] == 2023])} bills")
print(f"  2025: {len(df_combined[df_combined['Year'] == 2025])} bills")
print(f"\n  Total: {len(df_combined)} bills")
print(f"\n✓ Saved to: anti_trans_legislation_2025_with_dates.xlsx")
