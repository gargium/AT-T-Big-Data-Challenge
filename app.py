from flask import Flask, render_template, Markup, json
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/chart/")
def chart1():
    income = "B19013_001E"
    price = "B25077_001E"
    censusTract = "NAME"
    incomeList = []
    priceList = []
    censusTractList = []

    with open('Data/2010/sanFrancisco2010.geojson') as sf2010:
        sf2010Data = json.load(sf2010)

    for a in range(len(sf2010Data["features"])):
        if income in sf2010Data["features"][a]["properties"]:
            print sf2010Data["features"][a]["properties"][income]
            incomeList.append(sf2010Data["features"][a]["properties"][income])

    for b in range(len(sf2010Data["features"])):
        if price in sf2010Data["features"][b]["properties"]:
            print sf2010Data["features"][b]["properties"][price]
            priceList.append(sf2010Data["features"][b]["properties"][price])

    for c in range(len(sf2010Data["features"])):
        if censusTract in sf2010Data["features"][c]["properties"]:
            print sf2010Data["features"][c]["properties"][censusTract]
            censusTractList.append(sf2010Data["features"][c]["properties"][censusTract])

    incomeValues = incomeList
    priceValues = priceList
    censusTractValues = censusTractList
    # labels = ["January","February","March","April","May","June","July","August"]
    # values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=priceValues, labels=censusTractValues)

@app.route("/map")
def map():
    return render_template('map.html', urlSF='static/Data/sanFrancisco/sanFrancisco2010.geojson',
                           urlSR='static/Data/sanRamon/sanRamon2010.geojson', urlSC='static/Data/santaClara/santaClara2010.geojson')

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
	app.run(debug=True)
