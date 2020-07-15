# Scaffold Shuffle
Any NYC resident can tell you the construction sites they avoid on their commute to work. The scaffolding and barriers smell, feel unsafe, and are used as homeless shelters. When visiting a new destination, it's unavoidable you need to pass by a construction site.

The goal of this project is to generate the best walking route to avoid construction sites. The existing data published by the NYC Department of Buildings for active construction sites will be scraped for locations and type of construction. If the type of construction would include sidewalk scaffolding or barriers, it will be included in the areas to avoid.

The current status of this project is scaffold locations are plotted on a map with the users location. Left click a map marker will bring up the street view and show the scaffolding if the street view is relatively recent. The direction functionality has not been implemented yet. For this project to be publicly usable, the google maps api would need to be replaced with OpenStreetMap api.

## Installation
Install docker and docker-compose.

Pull this repo and add you're own google api key and socrata api key.

Launch with `docker-compose up`.

## Usage
The data pulled from DOB database is currently filtered by permit types, borough, and dates. These could be changed to include additional types of construction besides scaffolding or to include another borough.

## Changelog
### Unreleased
- add directions
- replace google maps api with openstreetmaps api

### 0.0.1 - 2020-07-15
- maps active constructions sites that likely require scaffolding
- shows users location
- shows street view when left click on map marker

## Credits
- [NYC DOB Data](https://data.cityofnewyork.us/Housing-Development/DOB-Permit-Issuance/ipu4-2q9a)

## License
- [MIT](https://en.wikipedia.org/wiki/MIT_License)

## Links
- [NYC Open Data](https://opendata.cityofnewyork.us/)
