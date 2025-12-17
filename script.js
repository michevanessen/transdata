// Global variables
let legislationData = [];
let stateSummary = {};
let currentSort = { column: null, direction: 'asc' };

// State abbreviations to full names mapping
const stateNames = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
    'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
    'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
    'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
    'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
    'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
};

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
    await loadData();
    initializeViewToggle();
    initializeMap();
    initializeTable();
    updateStats();
});

// Load data from JSON
async function loadData() {
    try {
        const response = await fetch('legislation_data.json');
        const data = await response.json();
        legislationData = data.legislation;
        stateSummary = data.stateSummary;

        if (data.lastUpdated) {
            document.getElementById('last-updated').textContent = data.lastUpdated;
        }
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

// View toggle functionality
function initializeViewToggle() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const views = document.querySelectorAll('.view-content');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const viewName = btn.dataset.view;

            tabButtons.forEach(b => b.classList.remove('active'));
            views.forEach(v => v.classList.remove('active'));

            btn.classList.add('active');
            document.getElementById(`${viewName}-view`).classList.add('active');
        });
    });
}

// Update statistics
function updateStats() {
    const totalBills = legislationData.length;
    const statesAffected = Object.keys(stateSummary).filter(s => s !== 'Federal').length;
    const billsPassed = legislationData.filter(item =>
        item.Passed && item.Passed.toLowerCase().includes('yes')
    ).length;

    document.getElementById('total-bills').textContent = totalBills;
    document.getElementById('states-affected').textContent = statesAffected;
    document.getElementById('bills-passed').textContent = billsPassed;
}

// Initialize map
async function initializeMap() {
    const width = 960;
    const height = 600;

    const svg = d3.select('#us-map')
        .attr('viewBox', `0 0 ${width} ${height}`);

    // Load US map data
    const us = await d3.json('https://cdn.jsdelivr.net/npm/us-atlas@3/states-10m.json');

    const projection = d3.geoAlbersUsa()
        .scale(1300)
        .translate([width / 2, height / 2]);

    const path = d3.geoPath().projection(projection);

    // Color scale based on number of bills
    const maxBills = Math.max(...Object.values(stateSummary).map(s => s.total));
    const colorScale = d3.scaleSequential()
        .domain([0, maxBills])
        .interpolator(d3.interpolateReds);

    // Create state abbreviation lookup
    const stateAbbr = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
        'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
        'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
        'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
        'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
        'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
    };

    // Draw states
    svg.selectAll('path')
        .data(topojson.feature(us, us.objects.states).features)
        .enter()
        .append('path')
        .attr('class', 'state')
        .attr('d', path)
        .attr('fill', d => {
            const abbr = stateAbbr[d.properties.name];
            const summary = stateSummary[abbr];
            return summary ? colorScale(summary.total) : '#e5e7eb';
        })
        .on('click', function(event, d) {
            const abbr = stateAbbr[d.properties.name];
            if (stateSummary[abbr]) {
                showStateDetail(abbr, d.properties.name);
            }
        });
}

// Show state detail
function showStateDetail(stateAbbr, stateName) {
    const stateDetail = document.getElementById('state-detail');
    const stateNameEl = document.getElementById('state-name');
    const legislationList = document.getElementById('state-legislation-list');

    stateNameEl.textContent = stateName;

    const stateBills = legislationData.filter(item => item['State/Federal'] === stateAbbr);

    legislationList.innerHTML = stateBills.map(bill => `
        <div class="legislation-item">
            <h3><a href="${bill.Link}" target="_blank">${bill.Legislation}</a></h3>
            <div class="legislation-meta">
                ${bill.Date ? `<span>Date: ${formatDate(bill.Date)}</span>` : ''}
                ${bill.Proposed === 'Yes' ? '<span class="status-badge proposed">Proposed</span>' : ''}
                ${bill.Passed && bill.Passed.toLowerCase().includes('yes') ? '<span class="status-badge passed">Passed</span>' : ''}
                ${bill['Denied/Vetoed'] && bill['Denied/Vetoed'].toLowerCase().includes('yes') ? '<span class="status-badge denied">Denied/Vetoed</span>' : ''}
            </div>
            <p>${bill['Status Notes']}</p>
        </div>
    `).join('');

    stateDetail.classList.remove('hidden');
    stateDetail.scrollIntoView({ behavior: 'smooth' });
}

// Close state detail
document.getElementById('close-detail').addEventListener('click', () => {
    document.getElementById('state-detail').classList.add('hidden');
});

// Initialize table
function initializeTable() {
    populateFilters();
    renderTable();
    setupTableControls();
}

// Populate filter dropdowns
function populateFilters() {
    const stateFilter = document.getElementById('state-filter');
    const states = [...new Set(legislationData.map(item => item['State/Federal']))]
        .sort()
        .filter(s => s !== 'Federal');

    states.unshift('Federal');

    states.forEach(state => {
        const option = document.createElement('option');
        option.value = state;
        option.textContent = stateNames[state] || state;
        stateFilter.appendChild(option);
    });
}

// Render table
function renderTable(filteredData = legislationData) {
    const tbody = document.getElementById('table-body');

    tbody.innerHTML = filteredData.map(item => `
        <tr>
            <td><a href="${item.Link}" target="_blank">${item.Legislation}</a></td>
            <td>${stateNames[item['State/Federal']] || item['State/Federal']}</td>
            <td>${item.Date ? formatDate(item.Date) : '-'}</td>
            <td>${item.Proposed}</td>
            <td>${item.Passed}</td>
            <td>${item['Denied/Vetoed']}</td>
            <td>${item['Status Notes']}</td>
        </tr>
    `).join('');
}

// Setup table controls
function setupTableControls() {
    const stateFilter = document.getElementById('state-filter');
    const statusFilter = document.getElementById('status-filter');
    const searchInput = document.getElementById('search-input');

    const applyFilters = () => {
        let filtered = [...legislationData];

        // State filter
        if (stateFilter.value) {
            filtered = filtered.filter(item => item['State/Federal'] === stateFilter.value);
        }

        // Status filter
        if (statusFilter.value) {
            if (statusFilter.value === 'passed') {
                filtered = filtered.filter(item => item.Passed && item.Passed.toLowerCase().includes('yes'));
            } else if (statusFilter.value === 'pending') {
                filtered = filtered.filter(item => item.Passed && item.Passed.toLowerCase().includes('pending'));
            } else if (statusFilter.value === 'denied') {
                // Show anything that's not passed or pending (includes vetoed, defeated, or failed)
                filtered = filtered.filter(item => {
                    const passed = (item.Passed || '').toLowerCase();
                    const deniedVetoed = (item['Denied/Vetoed'] || '').toLowerCase();
                    return passed === 'no' || (deniedVetoed !== 'no' && deniedVetoed !== '');
                });
            }
        }

        // Search filter
        if (searchInput.value) {
            const searchTerm = searchInput.value.toLowerCase();
            filtered = filtered.filter(item =>
                item.Legislation.toLowerCase().includes(searchTerm) ||
                item['Status Notes'].toLowerCase().includes(searchTerm)
            );
        }

        renderTable(filtered);
    };

    stateFilter.addEventListener('change', applyFilters);
    statusFilter.addEventListener('change', applyFilters);
    searchInput.addEventListener('input', applyFilters);

    // Sorting
    const headers = document.querySelectorAll('th[data-sort]');
    headers.forEach(header => {
        header.addEventListener('click', () => {
            const column = header.dataset.sort;
            sortTable(column);
        });
    });
}

// Sort table
function sortTable(column) {
    const columnMap = {
        'legislation': 'Legislation',
        'state': 'State/Federal',
        'date': 'Date',
        'proposed': 'Proposed',
        'passed': 'Passed',
        'denied': 'Denied/Vetoed',
        'status': 'Status Notes'
    };

    const actualColumn = columnMap[column];

    if (currentSort.column === column) {
        currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
    } else {
        currentSort.column = column;
        currentSort.direction = 'asc';
    }

    legislationData.sort((a, b) => {
        let aVal = a[actualColumn] || '';
        let bVal = b[actualColumn] || '';

        if (column === 'date') {
            aVal = aVal || '9999-12-31';
            bVal = bVal || '9999-12-31';
        }

        if (aVal < bVal) return currentSort.direction === 'asc' ? -1 : 1;
        if (aVal > bVal) return currentSort.direction === 'asc' ? 1 : -1;
        return 0;
    });

    // Update UI
    document.querySelectorAll('th').forEach(th => {
        th.classList.remove('sorted', 'asc', 'desc');
    });

    const header = document.querySelector(`th[data-sort="${column}"]`);
    header.classList.add('sorted', currentSort.direction);

    renderTable();
}

// Format date
function formatDate(dateStr) {
    if (!dateStr) return '';
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
}
