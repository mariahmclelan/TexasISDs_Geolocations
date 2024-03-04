from flask import Flask, jsonify, abort, render_template, json
from flask_pymongo import PyMongo
from bson import ObjectId
import folium
from folium.plugins import MarkerCluster
from branca.colormap import linear
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os 

app = Flask(__name__, static_url_path='/custom_static')
app.config["MONGO_URI"] = "mongodb://localhost:27017/texasSchoolsDB"
mongo = PyMongo(app)

def get_marker_size(revenue):
    if revenue < 5000000:
        return 4
    elif 5000000 <= revenue < 10000000:
        return 8
    elif 10000000 <= revenue < 50000000:
        return 12
    elif 50000000 <= revenue < 100000000:
        return 16
    elif 100000000 <= revenue < 500000000:
        return 20
    else:
        return 24

# Define marker color based on student count
def get_marker_color(student_count):
    if student_count >= 2275:
        return 'red'
    elif 1315 <= student_count <= 2274:
        return 'purple'
    elif 545 <= student_count <= 1314:
        return 'blue'
    elif 254 <= student_count <= 544:
        return 'yellow'
    elif 105 <= student_count <= 253:
        return 'orange'
    else:
        return 'green'
    


@app.route("/")
def home_page():
    info = (
        f"Available Routes:<br/>"
        f"/texasSchoolsDB/school_info<br/>"
        f"/texasSchoolsDB/current_districts_geojson<br/>"
        f"/texasSchoolsDB/scores_finances_coordinates<br/>"
        f"/texasSchoolsDB/coordinates<br/>"
        f"/texasSchoolsDB/schools_2022_to_2023_geojson<br/>"
        f"/map"
        f"/heatmap"
        
    )
    return render_template('home.html', info=info)


@app.route("/texasSchoolsDB/school_info")
def school_info():
    docs = mongo.db.school_info.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        data.append(doc)
    return jsonify(data)

@app.route("/texasSchoolsDB/current_districts_geojson")
def current_districts_geojson():
    docs = mongo.db.current_districts_geojson.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        data.append(doc)
    return jsonify(data)

@app.route("/texasSchoolsDB/scores_finances_coordinates")
def scores_finances_coordinates():
    docs = mongo.db.scores_finances_coordinates.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        data.append(doc)
    return jsonify(data)

@app.route("/texasSchoolsDB/coordinates")
def coordinates():
    docs = mongo.db.coordinates.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string
        data.append(doc)
    return jsonify(data)

@app.route("/texasSchoolsDB/demographics")
def demographics():
    docs = mongo.db.demographics.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)

@app.route("/map")
def map():
    # Retrieve GeoJSON data for district boundaries from MongoDB
    boundaries_cursor = mongo.db.current_districts_geojson.find({})
    districts_geojson = [
        {
            'type': 'Feature',
            'geometry': {
                'type': boundary['geometry']['type'],
                'coordinates': boundary['geometry']['coordinates']
            },
            'properties': {
                'name': boundary['properties']['NAME20']  # Use NAME20 for district name
            }
        }
        for boundary in boundaries_cursor
    ]

    # Create a Folium map centered around Texas
    m = folium.Map(location=[31.0, -100.0], zoom_start=6)  # Centered in Texas, adjust zoom as needed

    # Create a feature group for district boundaries
    district_group = folium.FeatureGroup(name='District Boundaries', control=True)

    # Add district boundaries to the map
    for district_geojson in districts_geojson:
        district_name = district_geojson['properties']['name']
        folium.GeoJson(
            district_geojson,
            style_function=lambda feature: {
                'color': 'black',
                'weight': 2,
                'fillOpacity': 0,
            },
            tooltip=district_name  # Add tooltip with district name
        ).add_to(district_group)

    # Add district boundaries feature group to the map
    district_group.add_to(m)

    # Retrieve GeoJSON data for markers from MongoDB
    coordinates = mongo.db.coordinates

    # Create a feature group for financial data markers
    marker_group = folium.FeatureGroup(name='Financial Data', control=True)

    # Fetch data from MongoDB and create markers
    for document in coordinates.find({}):
        latitude = float(document.get('Latitude'))
        longitude = float(document.get('Longitude'))
        revenue = float(document.get('Total_Operating_Revenue'))
        student_count = float(document.get('Student_Count'))
        district_name = document.get('District_Name')

        # Create popup text
        popup_text = f"ISD Name: {district_name} <br>Revenue: ${revenue:,}<br>Student Count: {student_count:,}"
        size = get_marker_size(revenue)
        color = get_marker_color(student_count)
        marker = folium.CircleMarker(location=[latitude, longitude],
                                      radius=size,
                                      color=color,
                                      fill=True,
                                      fill_color=color,
                                      fill_opacity=0.5,
                                      popup=popup_text,
                                      clickable=True)

        # Add marker to financial data feature group
        marker.add_to(marker_group)

    # Add financial data feature group to the map
    marker_group.add_to(m)

    # Add layer control to the map
    folium.LayerControl().add_to(m)

    # Save the map as HTML in templates folder
    m.save('templates/two_layers.html')

    return render_template('two_layers.html') 


@app.route("/heatmap")
def heat_map():
    # Retrieve SAT scores data from MongoDB
    scores = mongo.db.scores_finances_coordinates.find({}, {"SAT_Total": 1, "Latitude": 1, "Longitude": 1})
    
    # Retrieve data from MongoDB
    heat_data = []
    for document in scores:
        latitude = float(document.get('Latitude'))
        longitude = float(document.get('Longitude'))
        weight = float(document.get('SAT_Total'))  # Use SAT_Total as weight
        heat_data.append([latitude, longitude, weight])

    # Create a map centered around Texas
    map_sat_scores = folium.Map(location=[31.9686, -99.9018], zoom_start=6)

    # Add heatmap layer with legend
    heat_layer = folium.plugins.HeatMap(heat_data, gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'orange', 1: 'red'})
    heat_layer.add_to(map_sat_scores)

    # Add layer control for SAT Scores
    folium.LayerControl().add_to(map_sat_scores)

    # Convert the map to HTML
    map_html = map_sat_scores._repr_html_()

    # Pass the map HTML to the template
    return render_template('heat_map.html', map_html=map_html)

if __name__ == "__main__":
    app.run(debug=True)