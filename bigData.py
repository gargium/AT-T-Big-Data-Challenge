from pymongo import MongoClient

class bayArea:
	income = "B19013_001E"
	price = "B25077_001E"
	client = MongoClient()
	db = client.big_data
	sr = db.sanRamon.find({})
	sf = db.sanFrancisco.find({})
	sc = db.santaClara.find({})

	county = ["SF", "SR", "SC"]
	database = [sf, sr, sc]

	tracts = {
		"SF": {},
		"SR": {},
		"SC": {}
	}

	bsi = {
		"SF": {},
		"SR": {},
		"SC": {}
	}

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

	def __init__(self):
		for j in range(len(self.database)):
			db = self.database[j];
			for i in range(db.count()):
				for tract in db[i]["features"]:
					id = tract["properties"]["tract"]
					name = tract["properties"]["name"]
					self.bayArea[self.county[j]][str(i+2010)]["income"][id] = tract["properties"].get(self.income, "No Income Data Available")
					self.bayArea[self.county[j]][str(i+2010)]["price"][id] = tract["properties"].get(self.price, "No Price Data Available")
					self.tracts[self.county[j]][id] = name

	def get_bay_area(self):
		return self.bayArea

	def get_income(self, county, year, tract):
		return self.bayArea[county][year]["income"][tract]

	def get_price(self, county, year, tract):
		return self.bayArea[county][year]["price"][tract]

	def get_tracts(self, county):
		return self.tracts[county]

	def get_tract_name(self, county, id):
		return self.tracts[county][id]

	def count_tracts(self):
		for county in self.tracts:
			print county, len(self.tracts[county].keys())

	def set_bsi(self, county, tract, bsi):
		self.bsi[county][tract] = bsi

	def get_bsi(self, county, tract):
		return self.bsi[county][tract]
