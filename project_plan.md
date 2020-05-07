<!---
Reference:
https://www.openproject.org/
https://www.projectmanagementdocs.com/
--->

# Scaffold Shuffle
## Scope
Any NYer can tell you the construction sites they avoid on their commute to work. The scaffolding and barriers smell, feel unsafe, and are used as homeless shelters. When visiting a new destination, it's unavoidable you need to pass by a construction site. 

The goal of this project is to generate the best walking route to avoid construction sites. The existing data published by the [NYC Department of Buildings for active construction sites][1] will be scraped for locations and type of construction. If the type of construction would include sidewalk scaffolding or barriers, it will be included in the areas to avoid. The locations can be plotted on a map for easy visuablization and directions can be provided after the user enters two locations.

The second goal is to use this project as part of my protfolio which will require additional documentation on the planning, design, and execution of the project. The additional documentation will also need to be provided with website hosting.

This project uses existing data provided by NYC OpenData which is currently updated daily. It does not include programming a maps api or directions api.

## Schedule
The high level milestone schedule is:
- date - WBS & planning complete. Start programming.
- data - Pull data from DOB daily.
- date - Parse relavent data and store.
- date - Plot locations on a map.
- date - Plot walking directions.
- date - Cloud host for public access.

## Budget
The budget for the project is $0. It is to be funded through the FYxx My Empty Wallet Foundation. The NYC OpenData access if free. The maps api access will need to be limited to within the free range if using google. My existing home server is capable of hosting during dev. Cloud hosting might fit within the free bracket for limited usage and ads might pay for higher usage.

## WBS
The Work Breakdown Structure presented here represents all the work required to complete this project.

#### Outline View
<!--- follow the 8-80 rule for breaking out each task --->
	1. Setup Docker
		1.1 
	2. Data Pull from Source
		2.1 Existing data has API.
		2.2 Review API docs.
	3. Parse Data and Save
		3.1 
	4. Plot Locations on Map
		4.1 
	5. Plot Directions
		5.1 
	6. Setup Cloud Host
		6.1 


## Contacts
Project team directory for all communications is:
|Name	|Title	|Email	|Other	|
|---|---|---|---|
|Jon Murphy	|Project Owner	|me@jonmurphy.info	|git: jonmurphy1618	|


## Quality
The quality standards that will be followed:
- [Python PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Docker Guide](https://docs.docker.com/get-started/)

The quality metrics the project will need to meet:
- Daily data updating.
- Minimum maintence requirements. No manual data pull, docker building, or data parse.


## Risks
All risks, their causes, and the impacts.
- Additional data sets from NYC OpenData could be included but they're less actively updated or poorly formatted. [Active projects under construction][2], [street closure due to construction][3], [Sidewalk weekly construction schedule][4].
- Similar project that plotted walking and bike accidents along path called [SAFERout][5].


[1]: https://data.cityofnewyork.us/Housing-Development/DOB-Permit-Issuance/ipu4-2q9a
[2]: https://data.cityofnewyork.us/Housing-Development/Active-Projects-Under-Construction/8586-3zfm
[3]: https://data.cityofnewyork.us/Transportation/Street-Closures-due-to-construction-activities-by-/i6b5-j7bu
[4]: https://data.cityofnewyork.us/Transportation/Sidewalk-Weekly-Construction-Schedule/r528-jcks
[5]: https://github.com/zekebergida/saferout_nyc

