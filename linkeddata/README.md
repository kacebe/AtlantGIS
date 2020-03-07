# AtlantGIS as Linked Open Data

## Files

* `/rdf` - the final RDF files.
* `/ontology` - the AntlantGIS ontology as OWL file and HTML representation.
* `/pyscripts` - python scripts for transforming csv tables into RDF.

## Ontology

See the AtlantGIS ontology at http://atlantgis.squirrel.link/ontology/ .

## SPARQL endpoint

AtlantGIS as LOD can be queried via a mainzed SPARQL endpoint:

```
http://sandbox.mainzed.org/atlantgis/
```

Send the following query to get all AtlantGIS geometries:

```sql
PREFIX atlantgis: <http://atlantgis.squirrel.link/ontology#>
PREFIX geosparql: <http://www.opengis.net/ont/geosparql#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?item ?wkt_geom WHERE {
  ?item geosparql:hasGeometry ?geom_obj .
  ?geom_obj geosparql:asWKT ?wkt_geom .
}
```

## SPARQLing Unicorn QGIS Plugin

The AtlantGIS triplestore is part of the `SPARQLing Unicorn QGIS Plugin` (>v0.8) which helps to integrate Linked Data and triplestores into QGIS.

* Install plugin: https://plugins.qgis.org/plugins/sparqlunicorn/
* Install the required dependencies: https://github.com/sparqlunicorn/unicornQGISdepInstaller
* More Info at: http://sparqlunicorn.link

## Credits

* Florian Thiery, Research Squirrel Engineers
* Timo Homburg, Research Squirrel Engineers

## License

CC BY-SA 4.0 - Research Squirrel Engineers 2020

This work is licensed under the Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/deed.de.
