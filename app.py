from flask import Flask, jsonify, abort, render_template
from flask_pymongo import PyMongo
from bson import ObjectId
import folium

app = Flask(__name__)
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
    return (
        f"Available Routes:<br/>"
        f"/texasSchoolsDB/scores_finances<br/>"
        f"/texasSchoolsDB/school_info<br/>"
        f"/mongomaps"
        # f"/texasSchoolsDB/current_districts_geojson"
    )

@app.route('/mongomaps')
def mongomaps():
    # Access MongoDB collection
    coordinates = mongo.db.coordinates

    # Create a Folium map
    map = folium.Map(location=[29.7604, -95.3698], zoom_start=6)

    # Create a feature group for the markers
    marker_group = folium.FeatureGroup(name='Markers')

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

        # Add marker to feature group
        marker.add_to(marker_group)

    # Add feature group to the map
    marker_group.add_to(map)

    # Add layer control to the map
    folium.LayerControl().add_to(map)

    # Convert the map to HTML
    map_html = map.get_root().render()

    # Render the HTML template with the map
    return render_template('map_with_markers_revenue_size_and_student_count_color_updated.html', map=map_html)

@app.route("/texasSchoolsDB/scores_finances")
def scores_finances():
    docs = mongo.db.scores_finances.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)

@app.route("/texasSchoolsDB/school_info")
def school_info():
    docs = mongo.db.school_info.find({})
    data = []
    for doc in docs:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)

# @app.route("/texasSchoolsDB/current_districts_geojson")
# def current_districts_geojson():
#     docs = mongo.db.current_districts_geojson.find({})
#     data = []
#     for doc in docs:
#         doc['_id'] = str(doc['_id'])
#         data.append(doc)
#     return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
