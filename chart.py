from flask import Flask, render_template, Markup, json

income = "B19013_001E"
price = "B25077_001E"

with open('Data/2010/sanFrancisco2010.geojson') as sf2010:
    sf2010Data = json.load(sf2010)

    print sf2010Data["features"]

for a in range(len(sf2010Data["features"])):
    if income in sf2010Data["features"][a]["properties"]:
        print sf2010Data["features"][a]["properties"][income];


# labels = ["January","February","March","April","May","June","July","August"]
# values = [10,9,8,7,6,4,7,8]
# return render_template('chart.html', values=values, labels=labels)