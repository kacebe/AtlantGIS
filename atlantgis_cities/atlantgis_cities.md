# AtlantGIS Cities

## The Cities

The files in this subfolder contain cities that can be used as part of the AtlantGIS data set. The cities were generated with the [Medieval Fantasy City Generator](https://watabou.itch.io/medieval-fantasy-city-generator) by [watabou](https://itch.io/profile/watabou). The cities were then placed on the location of the capitals on the AtlantGIS map. Topological Errors were fixed. Walls, towers and gates were added. Roads were added to connect the cities.

This data set was created as part of a seminar paper. Its goal was to work with geo-spatial data in a context of (digital) humanities. Instead of using existing data, the AtlantGIS cities were created as an opportunity to add more detail to the AtlantGIS map. This work was produced in the seminar "Erfassung von raumbezogenen Daten in interdisziplinärem Kontext" as part of the digital humanities degree course "Digitale Methodik in den Geistes- und Kulturwissenschaften" in Mainz".

### City transformation

To turn a Medieval Fantasy City in an AtlantGIS City several steps are necessary:
- import the json file from the generator in QGIS
- delete the 'river', 'fields' and 'earth' layers from the json
- move the remaining layers to the desired city location
- split the polygon layers 'buildings', 'greens' and 'squares' in multipolygons (via plugin 'split feature parts') to fix topology
- buffer those layers with 0m to fix topology
- turn the 'walls' polygon layer into a linestring, buffer this linestring with 4m to get the walls, extract the vertex points and buffer them with 7m to get the towers, merge and disolve those layers
- merge the new walls with the original 'walls' layer to get the new city borders
- buffer the 'roads' linestring, 3m
- difference between roads and walls to get the gates
- mark the buildings in the suburbs outside the gates, buffer with 5m, dissolve, convex hull to get the area of the suburbs
- merge streets, wall area and suburb area to get the full city area

The result should now look like one of the AtlantGIS cities.

## Usage Example

The city maps can be used to make a space syntax analysis. For this purpose the city borders, walls and buildings were merged into one file. This file was converted to .dxf to allow the analysis with [depthMapX](https://www.spacesyntax.online/software-and-manuals/depthmap/). With this tool it is possible to show how connected a certain place in the city is to the rest of it. The influence of open spaces in the city, of big streets, or suburbs in front of the gates on the movement of its citizens can be shown and analyzed this way.
In a second attempt the cities were turned into street maps by taking the sceleton of the city maps, doing a bit of cleaning and connecting the city street maps with the intercity roads to perform a space syntax analysis on the whole AtlantGIS city system.
In the 'example' folder are a few illustrations of the spacial syntax analysis.
