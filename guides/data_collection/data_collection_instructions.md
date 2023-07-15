# How to Get Zoning by the Tax Lot Data

In order for this project to work, I had to come up with a way to systematically and quickly import data on <b>all</b> of NYC's numerous tax lots that make up the fabric of its street system.

Thankfully, David Chen (<a href="https://github.com/TheEgghead27">Github</a>, <a href="https://www.linkedin.com/in/david-lin-chen/">LinkedIn</a>) was able to come up with a way to do this in relatively quick time. Without his initial contribution to the journey, the rest of it would not be possible.

Without further ado...

## Step 1: ZoLall the Way to the Bank 
Go to the NYC ZoLa (Zoning and Land Use) Website, upon which you will be greeted with a wonderful hodge podge of bright colors and other doohickeys. Don't worry about that for now. Zoom into any building, and open the F12 menu.

![Landing Inspect Page](zolasc1.png)

Then hit <b>Network</b>. <b>ONLY AFTER THAT</b>, proceed to click on any building. <i>(a random one on Madison Street in Bed-Stuy will do for our example)</i>

![Inspect Network Page](zolasc2.png)

The Network tab should be as confusing as it looks. This shows that (if we did Network -> building selection in the right order) the page has responded to our request to get data on a particular tax lot. 

(I'll use tax lot and building interchangeably, but just know that while a single tax lot usually corresponds to a single building, that does not always have to be the case! One building may belong to more than one tax lot, and one tax lot may encompass more than one building.)

In the <b>Filter</b> section, type in the <b>BBL</b> code as it appears in
`TAX LOT | BBL 3018260025` on the top of the page just to the left of our F12 menu. 


![Network Filter](zolasc3.png)

A "BBL" is a shorthand of saying Borough, Block, Lot. This is the way tax lots are divided up and codified in the NYC Planning Department, with a 10 digit code serving as an amalgamation of 3 smaller codes.

The Borough code can be anywhere between 1-5 inclusive, with 1 being Manhattan, 2 being the Bronx, 3 being Brooklyn, 4 being Queens, and 5 being Staten Island. The BBL code adds a second filler digit after the borough digit.

The Block code can by any (to my knowledge) 4 digit number `0000-9999`, and any missing leading zeros in the original block number will be filled in in the BBL code.

The Lot code works the same as the Block number.

The resulting BBL code can be used to identify any tax lot in New York City, and will be a useful tool for us in the next few steps.

Click on the first link that appears, whose preview ends in `"address,bbl,..."`

![SQL Sample](zolasc4.png)

What we have selected is important, and will be the basis for our subsequent data collection.

The New York City government has graciously provided an API (Application Programming Interface) to their data through their <a href="https://labs.planning.nyc.gov/">Planning Labs</a> website. 

This link represents a web request to the API to retrieve all information about this tax lot using SQL code that has been made compatible with HTML using some syntax edits. 

In our next step, we will undo these edits to reconstruct the original SQL code, and modify it to retrieve data for <b>all</b> NYC tax lots from the API. (Sincerest of apologies to the servers running this API for the repeated frying I did to them making this map, I promise it was all worth it)