# How to Get Zoning by the Tax Lot Data

In order for this project to work, I had to come up with a way to systematically and quickly import data on <b>all</b> of NYC's numerous tax lots that make up the fabric of its street system.

Thankfully, David Chen (<a href="https://github.com/TheEgghead27">Github</a>, <a href="https://www.linkedin.com/in/david-lin-chen/">LinkedIn</a>) was able to come up with a way to do this in relatively quick time. Without this contribution of his to the journey, the rest of it would not be possible.

Without further ado...

## Step 1: ZoLall the Way to the Bank 
Go to the NYC ZoLa (Zoning and Land Use) Website, upon which you will be greeted with a wonderful hodge podge of bright colors and other doohickeys. Don't worry about that for now. Zoom into any building, and open the F12 menu.

![Landing Inspect Page](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/zolasc1.PNG)

Then hit <b>Network</b>. <b>ONLY AFTER THAT</b>, proceed to click on any building. <i>(a random one on Madison Street in Bed-Stuy will do for our example)</i>

![Inspect Network Page](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/zolasc2.PNG)

The Network tab should be as confusing as it looks. This shows that (if we did Network -> building selection in the right order) the page has responded to our request to get data on a particular tax lot. 

(I'll use tax lot and building interchangeably, but just know that while a single tax lot usually corresponds to a single building, that does not always have to be the case! One building may belong to more than one tax lot, and one tax lot may encompass more than one building.)

In the <b>Filter</b> section, type in the <b>BBL</b> code as it appears in
`TAX LOT | BBL 3018260025` on the top of the page just to the left of our F12 menu. 


![Network Filter](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/zolasc3.PNG)

A "BBL" is a shorthand of saying Borough, Block, Lot. This is the way tax lots are divided up and codified in the NYC Planning Department, with a 10 digit code serving as an amalgamation of 3 smaller codes.

The Borough code can be anywhere between 1-5 inclusive, with 1 being Manhattan, 2 being the Bronx, 3 being Brooklyn, 4 being Queens, and 5 being Staten Island.

The Block code can by any (to my knowledge) 5 digit number `00000-99999`, and any missing leading zeros in the original block number will be filled in in the BBL code.

The Lot code works the same as the Block number, but with a 4 digit number.

The resulting BBL code can be used to identify any tax lot in New York City, and will be a useful tool for us in the next few steps.

Click on the first link that appears, whose preview ends in `"address,bbl,..."`

![SQL Sample](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/zolasc4.PNG)

What we have selected is important, and will be the basis for our subsequent data collection.

The New York City government has graciously provided an API (Application Programming Interface) to their data through their <a href="https://labs.planning.nyc.gov/">Planning Labs</a> website. 

This link represents a web request to the API to retrieve all information about this tax lot using SQL code that has been made compatible with URL using some syntax edits. 

In our next step, we will undo these edits to reconstruct the original SQL code, and modify it to retrieve data for <b>all</b> NYC tax lots from the API. (Sincerest of apologies to the servers running this API for the repeated frying I did to them making this map, I promise it was all worth it)

## Step 2: We Aren't Getting Any Sleep

I did this step using <a href="https://insomnia.rest/download">Insomnia</a>, but I'm sure any old API development program will work.

Create a new request, head over to <b>Query</b>, and paste the link in the URL tab at the top.

![SQL Sample](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/insomniasc1.PNG)

Next, hit Import from URL and watch the sparks (SQL-URL deconstruction) fly!

![SQL Sample](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/insomniasc2.PNG)

We have a LOT of information that we're pulling from the API (some of it VERY incriminating, like the building owner), so let's not have all of that there!

What we need for now is just `address,bbl,bldgarea,block,borocode,cd,lot,lotarea,lotdepth,lotfront,numbldgs,numfloors,unitsres,unitstotal`, and everything after and including the "id" comment.

Next, change the `WHERE bbl=3018260025` to `WHERE bbl BETWEEN 1000000000 AND 1999999999` to encompass all possible Manhattan BBLs. (we will get to the other boroughs soon)

![SQL Sample](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/insomniasc3.PNG)

These modifications will allow us to only get the data we may need, and only scan for reasonably possible BBLs, because believe it or not, abusing API resources isn't cute or quirky, it's just mean. :(

While we will not primarily get our final data from insomnia, it helps to send a request anyways to see what the data looks like to make sure it's right.

It should take a few seconds to render the list, and make sure you display it on screen regardless of the warnings to see it in-program. 

![SQL Sample](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/insomniasc4.PNG)

We have a lot of characteristics on this address: <b>2 Wall Street</b>. 
As a commercial building, it has 0 residential units, but we know it has 21 floors, a gross floor area of 173,159 square feet, and a lot area of 8,614 square feet. 

(The floor-to-area ratio, otherwise known as FAR, taken by diving total floor area by lot area, is above 20, making this certainly a dense tower. Fitting for a Financial District building.)

This, and all other Manhattan tax lots, should be visible in this preview, but let's now move on to writing a script to help us write the data for all boroughs into files.

## Step 3: Lead the Serpents to the Palace

Using Python, we can make a short script to automate this process for us and procure our citywide data in seconds.

Take the `URL Preview` from Insomnia, and copy it. We'll need it a bit later.

Here's a copy of the code used to import the data (found in `import.py`):

```
import http.client

conn = http.client.HTTPSConnection("planninglabs.carto.com")

for i in range(5):
    print(f"Getting file #{i+1}!")
    payload = ""
    conn.request("GET", f"/api/v2/sql?q=SELECT%20address,bbl,bldgarea,block,borocode,cd,lot,lotarea,lotdepth,lotfront,numbldgs,numfloors,unitsres,unitstotal,%20%20%20%20%2F*%20id%3A3018260025%20*%2F%20%20%20%20st_x(st_centroid(the_geom))%20as%20lon,%20st_y(st_centroid(the_geom))%20as%20lat,%20%20%20%20the_geom,%20bbl%20AS%20id%20FROM%20dcp_mappluto%20WHERE%20bbl%20BETWEEN%20{i+1}000000000%20AND%20{i+1}099999999&format=geojson", payload)
    res = conn.getresponse()
    data = res.read()

    with open(f"{i+1}-data.json", 'w') as f:
        f.write(data.decode("utf-8"))
```

We will use http.client to interact with the Web from Python, create a connection to the PlanningLabs site, request 5 payloads, each of which being each of the boroughs in the city. This is where the URL will go. Cut off everything before /api, since that is the domain and we have already specified it in the `HTTPSConnection` variable. Place it in between the `"GET"` and `payload` parameters of the request function. 

We will also use fprint to be able to change out the Borough code at will using the variable we're using to loop through the Boroughs with, and change files accordingly when we write the data to our JSON file output at the end.

Save and run the program, and run it with `python3 [filename].py`

## Step 4: Cleanup on Aisle J(SON)

Our last step is to make our files a little more readable, with this one simple trick! (Doctors hate it...)

`for i in {1..5}; do cat $i-data.json | python3 -m json.tool > $i-data-clean.json; done`

The clean data should look like what we saw in Insomnia. 

## Here's a bonus!

A representation of some of the lot blocks in Manhattan using the neat <a href="https://geojson.io/">GeoJSON</a>!

![GeoJSON](https://github.com/doke05c/NYCDensityMapper/blob/main/guides/data_collection/geojson1.PNG)

176 Bleecker has 4 residential units, and a great Indian restaurant! (That's the 5th unit in the building)
