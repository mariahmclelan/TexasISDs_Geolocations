User
const URL = 'http://127.0.0.1:5000/texasSchoolsDB/demographics' 


// Fetch the JSON data and log it
d3.json(URL).then(function(data) {
    console.log(data);
}); 

// Initialize the dashboard by creating the init function
function init() {
    // Use D3 to select the dropdown menu
    let dropdownMenu = d3.select('#selDataset');

    // Using D3 to get access to sample data
    d3.json(URL).then((data) => {
        // Declaring a variable to store district names
        let districtNames = data.map(d => d.District_Name);
        console.log(districtNames);

        // Add districts to the dropdown menu
        districtNames.forEach(function(name) {
            // Append each name as an option to the dropdown menu
            dropdownMenu.append('option').text(name).property('value', name);
        });

        // Assign the first district to a variable
        let firstDistrict = districtNames[0];

        // Log the first district
        console.log(firstDistrict);

        // Build the visualizations: a demographic panel, a bar chart, a bubble chart, a radar chart, and a gauge chart
        BarChart(firstDistrict);
        BubbleChart(firstDistrict);
        RadarChart(firstDistrict);
        Metadata(firstDistrict);
    });
}

// Build the bar chart
function BarChart(district) {
    // Use D3 to access the sample data for populating the bar chart
    d3.json(URL).then((data) => {
        let districtData = data.find(d => d.District_Name === district);
        console.log(districtData);

        // Extract demographic data for the bar chart
        let demographicData = {
            'African American': parseFloat(districtData['%_African_American']),
            'American Indian': parseFloat(districtData['%_American_Indian']),
            'Asian': parseFloat(districtData['%_Asian']),
            'Hispanic': parseFloat(districtData['% Hispanic']),
            'Pacific Islander': parseFloat(districtData['%_Pacific_Islander']),
            'White': parseFloat(districtData['%_White']),
            'Two or more races': parseFloat(districtData['%_Two_or_More_Races'])
        };

        // Bar Chart's trace
        let barChartTrace = {
            x: Object.values(demographicData),
            y: Object.keys(demographicData),
            type: 'bar',
            orientation: 'h'
        };

        let layout = {
            title: { 
                text: `<b>Demographic Distribution in ${district}</b>`,
                font: {size: 16, color: 'black'}
            },
            paper_bgcolor: "lavender"
        };

        // Call Plotly to create the bar chart
        Plotly.newPlot('bar', [barChartTrace], layout);
    });
}

// Build the bubble chart
function BubbleChart(district) {
    // Use D3 to access the sample data and populate the bubble chart
    d3.json(URL).then((data) => {
        let districtData = data.find(d => d.District_Name === district);
        console.log(districtData);

        // Extract demographic data for the bubble chart
        let demographicData = {
            'African American': parseFloat(districtData['%_African_American']),
            'American Indian': parseFloat(districtData['%_American_Indian']),
            'Asian': parseFloat(districtData['%_Asian']),
            'Hispanic': parseFloat(districtData['% Hispanic']),
            'Pacific Islander': parseFloat(districtData['%_Pacific_Islander']),
            'White': parseFloat(districtData['%_White']),
            'Two or more races': parseFloat(districtData['%_Two_or_More_Races'])
        };

        // Bubble Chart's trace
        let bubbleChartTrace = {
            x: Object.values(demographicData),
            y: Object.keys(demographicData),
            mode: 'markers',
            marker: {
                size: Object.values(demographicData),
                color: Object.values(demographicData),
                colorscale: 'Earth'
            }
        };

        let layout = {
            title: { 
                text: `<b>Demographic Distribution in ${district}</b>`,
                font: {size: 16, color: 'black'}
            },
            hovermode: 'closest',
            paper_bgcolor: "lavender",
            xaxis: {title: 'Percentage'},
            yaxis: {title: 'Demographic Group'}
        };

        // Call Plotly to create the bubble chart
        Plotly.newPlot('bubble', [bubbleChartTrace], layout);
    });
}

// Build the radar chart
function RadarChart(district) {
    // Use D3 to access the sample data and populate the radar chart
    d3.json(URL).then((data) => {
        let districtData = data.find(d => d.District_Name === district);
        console.log(districtData);

        // Extract demographic data for the radar chart
        let demographicData = {
            'African American': parseFloat(districtData['%_African_American']),
            'American Indian': parseFloat(districtData['%_American_Indian']),
            'Asian': parseFloat(districtData['%_Asian']),
            'Hispanic': parseFloat(districtData['% Hispanic']),
            'Pacific Islander': parseFloat(districtData['%_Pacific_Islander']),
            'White': parseFloat(districtData['%_White']),
            'Two or more races': parseFloat(districtData['%_Two_or_More_Races'])
        };

        // Radar Chart's trace
        let radarChartTrace = {
            r: Object.values(demographicData),
            theta: Object.keys(demographicData),
            fill: 'toself'
        };

        let layout = {
            title: { 
                text: `<b>Demographic Distribution in ${district}</b>`,
                font: {size: 16, color: 'black'}
            },
            polar: {radialaxis: {visible: true, range: [0, 100]}}
        };

        // Call Plotly to create the radar chart
        Plotly.newPlot('radar', [radarChartTrace], layout);
    });
}

// Build the demographic panel
function Metadata(district) {
    // Using D3 to access the sample data and populate the demographic panel
    d3.json(URL).then((data) => {
        let demographicData = data.find(d => d.District_Name === district);
        console.log(demographicData);

        // Clear out metadata
        d3.select('#sample-metadata').html('');

        // Use Object.entries to add each key and value to the panel
        Object.entries(demographicData).forEach(([key, value]) => {
            console.log(key, value);
            // Select the demographic info HTML
            d3.select('#sample-metadata').append('h6').text(`${key}: ${value}`);
        });
    });
}

// Define the function when the dropdown detects a change
function optionChanged(results){
    console.log(results);
    BarChart(results);
    BubbleChart(results);
    Metadata(results);
    GaugeChart(results);
}


init();