#!/bin/bash
begin='2010'
end='2014'
db='big_data'

sf='sanFrancisco'
sr='sanRamon'
sc='santaClara'

for city in $sf $sr $sc;
do
	for year in `seq $begin $end`;
	do
		mongoimport --db $db --collection $city --file Data/$city/$city$year.geojson
	done
done
