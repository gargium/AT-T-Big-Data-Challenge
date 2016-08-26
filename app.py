from flask import Flask, render_template, json
from bigData import bayArea

app = Flask(__name__)
bayArea = bayArea()

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/chart")
def chart():
    countyToTractMap = {}
    countyToTractMap["SR"] = bayArea.get_tracts("SR")
    countyToTractMap["SF"] = bayArea.get_tracts("SF")
    countyToTractMap["SC"] = bayArea.get_tracts("SC")

    return render_template('chart.html', bayArea=json.dumps(bayArea.get_bay_area()), countyTractMap=json.dumps(countyToTractMap))

@app.route("/map")
def map():
    return render_template('map.html', urlSF='static/Data/sanFrancisco/sanFrancisco2010.geojson',
        urlSR='static/Data/sanRamon/sanRamon2010.geojson', urlSC='static/Data/santaClara/santaClara2010.geojson')

@app.route("/about/")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)
