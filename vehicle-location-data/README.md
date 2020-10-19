# Visualize Mobility Data #

https://vehicle-simulator.herokuapp.com/

Problem Statement:
------------------------------------------------------------------------------------
door2door is analysing and visualising mobility data to find the optimal solution to improve public transportation in cities and rural areas, and working on finding the most efficient solutions to stakeholder's problems. One of the ways the team evaluates a potential Ridepooling service is by simulating said service. The mission is to integrate it in a solution that enables users to trigger a simulation and see its results visualized in some way accessible through a webpage.


Approach:
------------------------------------------------------------------------------------

* Analysis of Simulator module
* Creating an API/wrapper around the Simulator module
* Get the results by triggering the API
* Transformation and mapping the data
* Render the map by plotting the location coordinates for each mobility data
* Visualize the cluster on a map on click of a button


Tech Stack:
------------------------------------------------------------------------------------

1. Python 3.8
2. Flask
3. Heroku


Overview of "d2d-vehicle-simulator" Workflow:
------------------------------------------------------------------------------------

1. Create Flask API (GET)
    * An API/wrapper around the simulator module
    * Calculates the radius based on bounding box coordinates
    * Plots the location coordinates for each simulator data within the boundaries of Berlin
    * Renders an webpage for visualizing results on a map
    
2. Create webpage for visualization
    * A simple webpage to visualize simulation results on map by click of a button
    
    
Project Structure:
--------------------------------------------------------------------------------------

1. app.py -- _An API/wrapper function for the Simulator module_
2. simulator.py -- _Provides a class Simulator that returns some mock simulation results_
3. templates/index.html -- _An html page for the visualizing simulation results on a map_
4. templates/visual_map.html -- _A rendered html page after plotting location coordinates on a map_
5. berlin_stops.geojson -- _A geojson file which contains dropoff and pickup points data_
6. Procfile -- _A file which is used to run a web app deployed on Heroku_
7. requirements.txt -- _Dependency libraries for the project_
8. runtime.txt -- _A file which contains runtime version on which the app is running_


Pre requisites:
---------------------------------------------------------------------------------------

* Python 3.7 or Python 3.8
* Heroku


Libraries Used:
---------------------------------------------------------------------------------------

1. _Folium_ -- A python package for visualizing maps that makes it easy to visualize data that's been manipulated in Python on an interactive leaflet map. It enables both the binding of data to a map for choropleth visualizations as well as passing rich vector/raster/HTML visualizations as markers on the map.

2. _Flask_ -- A lightweight WSGI web application framework to build a web application

3. _GeoPandas_ -- A python library to work with geospatial data that extends the datatypes used by pandas to allow spatial operations on geometric types.

4. _Shapely_ -- A Python package for manipulation and analysis of planar geometric objects



Solution:
---------------------------------------------------------------------------------------

Visualize the simulation results on a map (in any browser) by clicking the below web URL.

URL --> https://vehicle-simulator.herokuapp.com/

PS: DEMO screenshots available in /demo_screenshots/README.md
