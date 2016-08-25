from pymongo import MongoClient

client = MongoClient()
db = client.big_data
sr = db.sanRamon.find({})
sf = db.sanFrancisco.find({})
sc = db.santaClara.find({})

income = "B19013_001E"
price = "B25077_001E"

bayArea = {
	"SF": {
		"2010": {
			"income": {},
			"price": {}
		},
		"2011": {
			"income": {},
			"price": {}
		},
		"2012": {
			"income": {},
			"price": {}
		},
		"2013": {
			"income": {},
			"price": {}
		},
		"2014": {
			"income": {},
			"price": {}
		}
	},
	"SR": {
		"2010": {
			"income": {},
			"price": {}
		},
		"2011": {
			"income": {},
			"price": {}
		},
		"2012": {
			"income": {},
			"price": {}
		},
		"2013": {
			"income": {},
			"price": {}
		},
		"2014": {
			"income": {},
			"price": {}
		}
	},
	"SC": {
		"2010": {
			"income": {},
			"price": {}
		},
		"2011": {
			"income": {},
			"price": {}
		},
		"2012": {
			"income": {},
			"price": {}
		},
		"2013": {
			"income": {},
			"price": {}
		},
		"2014": {
			"income": {},
			"price": {}
		}
	}
}

for i in range(sr.count()):
	for tract in sr[i]["features"]:
		name = tract["properties"]["tract"]
		bayArea["SR"][str(i+2010)]["income"][name] = tract["properties"].get(income, "No Income Data Available")
		bayArea["SR"][str(i+2010)]["price"][name] = tract["properties"].get(price, "No Price Data Avaialbe")

for i in range(sf.count()):
	for tract in sr[i]["features"]:
		name = tract["properties"]["tract"]
		bayArea["SF"][str(i+2010)]["income"][name] = tract["properties"].get(income, "No Income Data Available")
		bayArea["SF"][str(i+2010)]["price"][name] = tract["properties"].get(price, "No Price Data Avaialbe")

for i in range(sc.count()):
	for tract in sr[i]["features"]:
		name = tract["properties"]["tract"]
		bayArea["SC"][str(i+2010)]["income"][name] = tract["properties"].get(income, "No Income Data Available")
		bayArea["SC"][str(i+2010)]["price"][name] = tract["properties"].get(price, "No Price Data Avaialbe")

# count how many tracts in each
# for county in bayArea:
# 	for year in bayArea[county]:
# 		for factor in bayArea[county][year]:
# 			print county, year, factor, len(bayArea[county][year][factor].keys())

