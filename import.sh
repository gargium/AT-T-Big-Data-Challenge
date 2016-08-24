#!/bin/bash
begin='2010'
end='2014'
db='big_data'

sf='sanFrancisco'
sr='sanRamon'
sc='santaClara'

for year in `seq $begin $end`;
do
	for city in $sf $sr $sc;
	do
		mongoimport --db $db --collection y$year --file Data/$year/$city$year.geojson
	done
done
