from flask import Flask, render_template, json
from bigData import bayArea
from algorithm import algorithm

app = Flask(__name__)
bayArea = bayArea()
algorithm = algorithm()


@app.route("/")
def index():
	return render_template('index.html')

@app.route("/chart")
def chart():
    countyToTractMap = {}
    countyToTractMap["SR"] = bayArea.get_tracts("SR")
    countyToTractMap["SF"] = bayArea.get_tracts("SF")
    countyToTractMap["SC"] = bayArea.get_tracts("SC")
    SFBSIs = algorithm.BSI("SF")
    SCBSIs = algorithm.BSI("SC")
    SRBSIs = algorithm.BSI("SR")

    return render_template('chart.html', bayArea=json.dumps(bayArea.get_bay_area()), countyTractMap=json.dumps(countyToTractMap), sfBSIs = json.dumps(SFBSIs), scBSIs = json.dumps(SCBSIs), srBSIs = json.dumps(SRBSIs))

@app.route("/map")
def map():
    SFBSIs = algorithm.BSI("SF")
    SCBSIs = algorithm.BSI("SC")
    SRBSIs = algorithm.BSI("SR")

    return render_template('map.html', urlSF='static/Data/sanFrancisco/sanFrancisco2010.geojson',
                           urlSR='static/Data/sanRamon/sanRamon2010.geojson',
                           urlSC='static/Data/santaClara/santaClara2010.geojson',
                           sfBSIs = json.dumps(SFBSIs),
                           scBSIs = json.dumps(SCBSIs),
                           srBSIs = json.dumps(SRBSIs))

@app.route("/about/")
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)
