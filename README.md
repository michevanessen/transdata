# Anti-Trans Legislation Tracker 2025

An interactive web application for tracking proposed and enacted anti-trans legislation across the United States.

## Files

- `index.html` - Main HTML file
- `styles.css` - Styling and responsive design
- `script.js` - Interactive functionality (map, tables, filters)
- `legislation_data.json` - Processed legislation data
- `anti_trans_legislation_2025_with_dates.xlsx` - Updated Excel file with dates column
- `process_legislation.py` - Python script to extract dates and convert data to JSON

## Features

### Map View
- Interactive US map showing legislation by state
- Color-coded states based on number of bills (darker red = more legislation)
- Click on states to see detailed legislation

### State Detail View
- Detailed list of legislation for selected state
- Status badges (Proposed, Passed, Denied)
- Direct links to legislation sources
- Date information when available

### Table View
- Sortable columns (click headers to sort)
- Filter by state (dropdown)
- Filter by status (Passed, Pending, Denied)
- Search functionality across legislation and status notes
- Excel-like appearance with modern design

## Local Testing

To test locally, start a simple HTTP server:

```bash
# Using Python 3
python3 -m http.server 8000

# Or using Python 2
python -m SimpleHTTPServer 8000

# Or using Node.js (if npx is installed)
npx http-server
```

Then open `http://localhost:8000` in your browser.

## Deployment Options

### 1. GitHub Pages (Recommended - Free & Easy)

1. Create a GitHub repository
2. Upload all files (index.html, styles.css, script.js, legislation_data.json)
3. Go to repository Settings > Pages
4. Set source to "main" branch and root folder
5. Your site will be live at `https://yourusername.github.io/repository-name`

### 2. Netlify (Free - Drag & Drop)

1. Go to [netlify.com](https://netlify.com)
2. Sign up for free account
3. Drag and drop your project folder
4. Instant deployment with custom domain support

### 3. Vercel (Free - Modern Platform)

1. Go to [vercel.com](https://vercel.com)
2. Sign up for free account
3. Connect GitHub repo or upload files
4. Automatic deployment and CDN

### 4. Cloudflare Pages (Free - Fast CDN)

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com)
2. Connect GitHub repository
3. Deploy with global CDN

### 5. Static Hosting Services

Other options:
- **Render** (free tier available)
- **Firebase Hosting** (free tier)
- **Surge.sh** (simple CLI deployment)

## Updating Data

To update the data:

1. Update the Excel file: `anti_trans_legislation_2025.xlsx`
2. Run the processing script:
   ```bash
   python3 process_legislation.py
   ```
3. This will regenerate:
   - `anti_trans_legislation_2025_with_dates.xlsx` (Excel with dates)
   - `legislation_data.json` (data for website)
4. Redeploy the website with updated files

## Browser Compatibility

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers supported

## Technologies Used

- **D3.js** - Interactive map visualization
- **TopoJSON** - US map data
- **Vanilla JavaScript** - No framework dependencies
- **CSS Grid/Flexbox** - Responsive layout
- **Python/Pandas** - Data processing

## License

Data visualization project for public awareness and advocacy.
