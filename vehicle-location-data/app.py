from flask import Flask, jsonify, render_template
from simulator import Simulator
import folium
from folium.plugins import MarkerCluster
import json
from math import sin, cos, sqrt, atan2, radians

app = Flask(__name__, static_url_path='')

# City Boundaries
center_location = (52.56, 13.40)
RADIUS = 4500

def calculateRadius():
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(52.52791908000258)
    lon1 = radians(13.34014892578125)
    lat2 = radians(52.562995039558004)
    lon2 = radians(13.506317138671875)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1000
    return(distance)

@app.route('/render-simulation-data')
def get_simulation_result():
    number_of_requests = 5
    bounding_box = (13.34014892578125, 52.52791908000258, 13.506317138671875, 52.562995039558004)
    data = Simulator(bounding_box).simulate(number_of_requests)
    radius = calculateRadius()

    map_loc = "templates/visual_map.html"
    plot_map = folium.Map(location=center_location, zoom_start=11)
    folium.Circle(center_location, radius=radius).add_to(plot_map)
    marker_cluster = MarkerCluster().add_to(plot_map)

    # Mark the location dropoff and pickup points
    most_popular_dropoff_points = json.loads(data["most_popular_dropoff_points"])["features"]
    most_popular_pickup_points = json.loads(data["most_popular_pickup_points"])["features"]
    for points in most_popular_dropoff_points:
        properties = points["properties"]
        nodes = points["geometry"]["coordinates"]
        folium.Marker(location=nodes[::-1], tooltip=str(properties)).add_to(marker_cluster)

    for points in most_popular_pickup_points:
        properties = points["properties"]
        nodes = points["geometry"]["coordinates"]
        folium.Marker(location=nodes[::-1], tooltip=str(properties)).add_to(marker_cluster)
    plot_map.save(map_loc)
    return render_template('visual_map.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
