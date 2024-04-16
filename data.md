---
title:			Der AtlantGIS Datensatz
description:	Informationen rund um den AtlantGIS-Datensatz
date:           19.11.2021
author:			Kai-Christian Bruhn
affiliation:	Hochschule Mainz
contact:		kai-christian.bruhn@hs-mainz.de
license:		cc by 4.0
tags:			GIS, QGIS, Spatial Humanities, AtlantGIS, Digital Humanities
---

AtlantGIS
===

---

Link zu diesem Dokument: https://hackmd.io/@KaCeBe/atlantgis-dataset

---

Was ist AtlantGIS?

> Faked GIS-Datasets, simulating an island in the Atlantic for educational purposes in using GIS in archaeology. All AtlantGIS data are published under a CC-BY-SA 4.0 license.
The idea is to create artificial data creatively referring to the story of Atlantis as told by Platon. We believe that simple datasets with a narrative are most qualified to impart knowledge and skills to students.
Whoever likes the idea is invited to contribute data using the repository on GitHub. We ask every contributor to link to documents that put the dataset in context of a special GIS-related task and make the tutorials/workshop documents available under an open licence.
DISCLAIMER: These data are not in any way based on any "identification" of Platon's concept of Atlantis in geographical sense. They should and cannot be used to argue in favour or against any scientific of unscientific hypotheses.

Quelle: https://github.com/kacebe/AtlantGIS

Download zip-Archiv: https://github.com/kacebe/AtlantGIS/archive/refs/heads/master.zip

AtlantGIS Ontologie und Linked Open Data: https://research-squirrel-engineers.github.io/AtlantGIS_LOD/

QGIS- und R-Tutorials auf Basis von AtlantGIS:
* http://i3mainz.github.io/qgis-caa2014/
* http://i3mainz.github.io/qgis-caa2014/slides/01_Grundlagen.htm
* https://github.com/ISAAKiel/R-Tutorial_CAA2016/
* https://github.com/eScienceCenter/R-Tutorial_20170707

Foliensatz eines Vortrags auf Grundlage einer Hausarbeit auf Grundlage des AtlantGIS-Datensatzes: 
> Thiery, Florian, & Taani, Rania. (2017, June 23). Avalanches on Atlantis - Real or Fake? The "true" story!. XXX. International Geodetic Student Meeting, Zagreb, Croatia. Zenodo. https://doi.org/10.5281/zenodo.817496

---

## Datenherkunft

Reale Geodaten stammen von der Insel [Sokotra](https://de.wikipedia.org/wiki/Sokotra) im Indischen Ozean und wurden in den Atlantik "verschoben".

Viele Layer, insbesondere thematische Vektordaten, beziehen sich inhaltlich auf die Schilderungen von Plato im [Kritias-Dialog](http://de.wikipedia.org/wiki/Kritias_%28Platon%29)

---

## Datenstruktur

Das zip-Archiv auf GitHub auf der eigenen Festplatte entpackt, hat folgende Ordnerstruktur:

![](https://i.imgur.com/W5IhQir.png)

---

### Getting Started

In diesem Verzeichnis sind einige sehr abstrahierte Daten zu einer archäologischen Ausgrabung im Südosten der Insel erfasst. Konkret ist ein Gebiet von zwei 10 x 10 m messenden Grabungsschnitten am archäologischen Fundort 122 (vgl.`vector/shp/archaeological_sites`). 

![](https://i.imgur.com/1VGn184.png)
Lage der Grabung aus dem Verzeichnis `Getting Started` auf AtlantGIS


Im einzelnen umfassen die Daten:

#### geophys
    
`geophys_excavation.tif`:

Frei erfundene Daten einer geophysikalischen Prospektion in dem 20 x 10 m großen Ausgrabungs-Gebiet.


![](https://i.imgur.com/oWX0nJL.png)


`gdalinfo -mm -stats .../AtlantGIS-master/gettingstarted/geophys/geophys_excavation.tif`
Ausgabe
```
Driver: GTiff/GeoTIFF 
Files: .../AtlantGIS-master/gettingstarted/geophys/geophys_excavation.tif 
.../AtlantGIS-master/gettingstarted/geophys/geophys_excavation.tif.aux.xml 
Size is 40, 20 
Coordinate System is: 
PROJCRS["WGS 84 / UTM zone 28N", 
BASEGEOGCRS["WGS 84", 
DATUM["World Geodetic System 1984", 
ELLIPSOID["WGS 84",6378137,298.257223563, 
LENGTHUNIT["metre",1]]], 
PRIMEM["Greenwich",0, 
ANGLEUNIT["degree",0.0174532925199433]], 
ID["EPSG",4326]], 
CONVERSION["UTM zone 28N", 
METHOD["Transverse Mercator", 
ID["EPSG",9807]], 
PARAMETER["Latitude of natural origin",0, 
ANGLEUNIT["degree",0.0174532925199433], 
ID["EPSG",8801]], 
PARAMETER["Longitude of natural origin",-15, 
ANGLEUNIT["degree",0.0174532925199433], 
ID["EPSG",8802]], 
PARAMETER["Scale factor at natural origin",0.9996, 
SCALEUNIT["unity",1], 
ID["EPSG",8805]], 
PARAMETER["False easting",500000, 
LENGTHUNIT["metre",1], 
ID["EPSG",8806]], 
PARAMETER["False northing",0, 
LENGTHUNIT["metre",1], 
ID["EPSG",8807]]], 
CS[Cartesian,2], 
AXIS["(E)",east, 
ORDER[1], 
LENGTHUNIT["metre",1]], 
AXIS["(N)",north, 
ORDER[2], 
LENGTHUNIT["metre",1]], 
USAGE[ 
SCOPE["Engineering survey, topographic mapping."], 
AREA["Between 18°W and 12°W, northern hemisphere between equator and 84°N, onshore and offshore. Gambia. Greenland. Guinea. Guinea-Bissau. Iceland. Ireland - offshore Porcupine Basin. Mauritania. Morocco. Senegal. Sierra Leone. Western Sahara."], 
BBOX[0,-18,84,-12]], 
ID["EPSG",32628]] 
Data axis to CRS axis mapping: 1,2 
Origin = (456800.000000000000000,3933110.000000000000000) 
Pixel Size = (0.500000000000000,-0.500000000000000) 
Metadata: 
AREA_OR_POINT=Area 
TIFFTAG_ARTIST=Kai-Christian Bruhn 
TIFFTAG_COPYRIGHT=cc by sa 4.0 
TIFFTAG_IMAGEDESCRIPTION=Fake image of geophysical prospection of excavation site on AtlantGIS 
TIFFTAG_RESOLUTIONUNIT=3 (pixels/cm) 
TIFFTAG_SOFTWARE=proprietary 
TIFFTAG_XRESOLUTION=50 
TIFFTAG_YRESOLUTION=50 
Image Structure Metadata: 
INTERLEAVE=BAND 
Corner Coordinates: 
Upper Left ( 456800.000, 3933110.000) ( 15d28'35.65"W, 35d32'26.46"N) 
Lower Left ( 456800.000, 3933100.000) ( 15d28'35.65"W, 35d32'26.14"N) 
Upper Right ( 456820.000, 3933110.000) ( 15d28'34.86"W, 35d32'26.47"N) 
Lower Right ( 456820.000, 3933100.000) ( 15d28'34.86"W, 35d32'26.14"N) 
Center ( 456810.000, 3933105.000) ( 15d28'35.26"W, 35d32'26.30"N) 
Band 1 Block=40x20 Type=Float32, ColorInterp=Gray 
Min=96.782 Max=96.950 Computed Min/Max=96.782,96.950 
Minimum=96.782, Maximum=96.950, Mean=96.880, StdDev=0.036 
NoData Value=-9999 
Metadata: 
STATISTICS_MAXIMUM=96.949974060059 
STATISTICS_MEAN=96.879702615738 
STATISTICS_MINIMUM=96.782386779785 
STATISTICS_STDDEV=0.036105345519655 
STATISTICS_VALID_PERCENT=100
```

---

`geophys_excavation.tif.aux.xml`:
Metadaten (PAMDataset) mit Histogramm und Werte-Statistik.

---

#### sqlite

SpatiaLite-Datenbank mit Befunden und Mauern:

![](https://i.imgur.com/11bO9R8.png)


Attributdaten Befunde (features):

| PK_UID | id | type | desc | f_year | f_no | f_id |
| ------ | -- | ---- | ---- | ------ | ---- | ---- |
| 1 | 1 | posthole |  | 8 | 11 | 08-11 |
| 2 | 2 | posthole |  | 8 | 12 | 08-12 |
| 3 | 3 | floor | same as 08-18 | 8 | 17 | 08-17 |
| 4 | 4 | floor | same as 08-17 | 8 | 18 | 08-18 |
| 5 | 5 | foundation trench |  | 8 | 32 | 08-32 |
| 6 | 6 | foundation trench |  | 9 | 12 | 09-12 |
| 7 | 8 | pit |  | 9 | 7 | 09-7 |
| 8 | 7 | pit |  | 9 | 26 | 09-02 |
| 9 | 33 | fill |  | 8 | 33 | 08-33 | 
| 10 | 34 | fill |  | 9 | 9 | 09-09 |
| 11 | 4 | fill |  | 8 | 34 | 08-34 |
| 12 | 6 | fill |  | 8 | 31 | 08-31 |
| 13 | 58 | fill |  | 9 | 10 | 09-10 |

---

Attributdaten Mauern (walls):

| PK_UID | id | w_no | type |
| ------ | -- | ---- | ---- |
| 1 | 1 | 257 | rubble |
| 2 | 2 | 253 | rubble |
| 3 | 3 | 265 | rubble |

---

#### vector

##### dxf

Polygone der eingemessenen Grabungsgrenzen im DXF-Format ohne Attribute

![](https://i.imgur.com/ejEK1kx.png)

---

##### shp

Kleinfunde (smallfinds) als Shapefile. Keine .prj- oder .cpg-Datei vorhanden.

![](https://i.imgur.com/i6grJIx.png)

Attributdaten Keinfunde (smallfinds):

| PK_UID | id | sf_year | sf_no | type | material | sf_id |
| ------ | -- | ------- | ----- | ---- | -------- | ----- |
| 1 | 1 | 8 | 45 | needle | bone | 08-45 |
| 2 | 2 | 8 | 46 | coin | bronze | 08-46 |
| 3 | 3 | 9 | 3 | coin  | bronze | 09-3 |
| 4 | 4 | 9 | 15 | scraper | flint | 09-15 |
| 5 | 5 | 9 | 16 | bowl | glass | 09-16 |
| 6 | 6 | 9 | 17 | scraper | bronze | 09-17 |
| 7 | 7 | 9 | 18 | fibula | bronze | 09-18 |
| 8 | 8 | 9 | 19 | bead | glass | 09-19 |

---

### LinkedData

AtlantGIS as Linked Open Data

**Files**

* `/rdf` - the final RDF files.
* `/ontology` - the AntlantGIS ontology as OWL file and HTML representation.
* `/pyscripts` - python scripts for transforming csv tables into RDF.

**Ontology**

See the AtlantGIS ontology at http://atlantgis.squirrel.link/ontology/ .

**SPARQL endpoint**

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

**SPARQLing Unicorn QGIS Plugin**

The AtlantGIS triplestore is part of the `SPARQLing Unicorn QGIS Plugin` (>v0.8) which helps to integrate Linked Data and triplestores into QGIS.

* Install plugin: https://plugins.qgis.org/plugins/sparqlunicorn/
* Install the required dependencies: https://github.com/sparqlunicorn/unicornQGISdepInstaller
* More Info at: http://sparqlunicorn.link

**Credits for LinkedData set**

* Florian Thiery, Research Squirrel Engineers
* Timo Homburg, Research Squirrel Engineers

---

### Project Datasets

Ordner für spezifische Projektdateien

#### Barrows

Dieses Verzeichnis enthält Daten aus einem fiktiven Surveyprojekt von 2017 auf AtlantGIS, das ein bestimmtes Gebiet in der nördlichen Küstenebene der Insel zum Ziel hatte. Eigentlich handelt es sich um dekontextualisierte reale Daten aus dem von der DFG geförderten Projekt [Late Neolithic/Early Bronze Age developments in the south-west Baltic area (2500-1500 BC): Why did the Bruszczewo-Leki Male type of power structures appear?](http://gepris.dfg.de/gepris/projekt/277223019)

---

`barrow_dem.tif`:
![](https://i.imgur.com/cuWO4R1.png)

---

`barrow_magnetic.tif`

![](https://i.imgur.com/azT8d9Z.png)

---

`barrow_ortho.tif`

![](https://i.imgur.com/5RODQZF.png)

---

`barrow_magnetic_raw_data.csv`
CSV-Datei mit Messwerten für Interpolation
| id | magnetic_flux_in_nT | probe | x | y |

vgl. die [Informationen zum QGIS- und R-Workshop mit diesen Daten auf Github](https://github.com/kacebe/AtlantGIS/blob/e88a130c973b9368b06da790d5315df4b7586970/project_datasets/barrow/readme.md).

---

### Raster

Zur Zeit liegen als Rasterdaten nur ein Geländemodell der Insel vor.

#### dem

`atlantgis_dgm.tif`
Digitales Geländemodell der Insel. Abgeleitet aus:
> NASA Shuttle Radar Topography Mission (SRTM)(2013). Shuttle Radar Topography Mission (SRTM) Global. Distributed by OpenTopography. https://doi.org/10.5069/G9445JDF
> 
![](https://i.imgur.com/2OjX364.png)

Die Daten liegen als 
* GeoTIFF in epsg 32628 (WGS84/UTM 28N) vor.
* Daneben enthält das Verzeichnis die gleichen Daten in epsg 4326 (WGS 84) als
    * GeoTIFF und in 
    * XYZ-Format.

---

### Screenshots

Einzelne Graphiken für die Nutzung in Skripten und Präsentationen.

### Tables

Wertetabellen mit Daten für die Anreicherung von Geodatensätzen:

#### Periods

`atlantgis_periods.csv`

In den *periods* werden 5 Phasen der zeitlichen Entwicklung von AtlantGIS unterschieden. Mit den `integer`-Werten in `_counter`, `_before` und `_after` können Ausdrücke nach dem [Allen-Kalkül](https://de.wikipedia.org/wiki/Allen-Kalk%C3%BCl) formuliert werden:

| id | period_counter | period_code | period_desc | period_before | period_after |
| -- | -------------- | ----------- | ----------- | ------- | -------- |
| 1 | 5 | I | Period from genesis to Leukippe and Euenor | NULL | 10 |
| 2 | 10 | II | Period of Kleito and Poseidon as well as of their direct descendants | 5 | 25 |
| 3 | 13 | IIa | Period of Kleito and Poseidon | 5 | 17 |
| 4 | 17 | IIb | Period of Kleito's and Poseidon's descandants | 13 | 25 |
| 5 | 25 | III | Period before doom | 10 | NULL |

---

#### Finds

`Finds.csv`, `Finds.md` und `Finds_VesselTypes.csv`

Das Schema der `Finds.csv` ist in der `Finds.md` dokumentiert:

| Spalte      | Beschreibung                             |
| ----------- | ---------------------------------------- |
| site        | Fundstelle aus `vector/sites.shp`        |
| feature     | Befund                                   |
| object      | Individuum                               |
| class       | Fundgattung (K: Keramik)                 |
| sherd       | Art der Scherbe (G: Gefäß, R: Rand, W: Wand, B: Boden) |
| qty         | Anzahl                                   |
| wt          | Gewicht (g)                              |
| size        | Größenklasse (nach Clist 2004/05: 30: \<30x30mm, 70: \<70x70mm, 120: \<120x120mm, 200: \<200x200mm, 500: \>200x200mm) |
| wall        | Wandungsdicke (mm)                       |
| muendungsD  | Mündungsdruchmesser (cm)                 |
| muendungsH  | Höhe des Mündungsdruchmessers (cm)       |
| minD        | Minimaler Durchmesser (cm)               |
| minD_H      | Höhe des minimalen Durchmessers (cm)     |
| maxD        | Maximaler Durchmesser (cm)               |
| maxD_H      | Höhe des maximalen Durchmessers (cm)     |
| bodenD      | Bodendruchmesser (cm)                    |
| temperSize  | Größe nicht-plastischer Martikel (Magerung; nach 'Wentworth grain size classification', VF: Very fine 0.0625-0.125mm, F: Fine 0.125-0.25mm, M: Medium 0.25-0.5mm, C: Coarse 0.5-1mm, VC: Very Coarse 1-2mm) |
| vesselShape | Gefäßform (siehe `tables/Finds_VesselTypes.csv`) |

---

### Templates

`resources.qml` und `landtype.qml`

QML ist ein XML-Format zum Speichern von Layer-Stilen.

Eine QML-Datei enthält alle Informationen, die QGIS für das Rendern von Feature-Geometrien verarbeiten kann, einschließlich Symboldefinitionen, Größen und Drehungen, Beschriftung, Deckkraft und Mischmodus und mehr. ([Quelle](https://docs.qgis.org/3.16/de/docs/user_manual/appendices/qgis_file_formats.html#qml-the-qgis-style-file-format))

Exemplarisch sind in diesem Verzeichnis qml-Dateien für die Datensätze `\vector\shp\landtype` und `\vector\shp\resources` abgelegt.

---

`relief_farben`

Exemplarische Definition eines Farbverlaufs für die Visualisierung des Geländemodell im Verzeichnis `\raster\dem\`

```
<ReliefColors>
  <ReliefColor MaxElevation="50" red="255" blue="180" green="244" MinElevation="-5"/>
  <ReliefColor MaxElevation="100" red="249" blue="151" green="222" MinElevation="50"/>
  <ReliefColor MaxElevation="250" red="232" blue="109" green="187" MinElevation="100"/>
  <ReliefColor MaxElevation="500" red="185" blue="86" green="149" MinElevation="250"/>
  <ReliefColor MaxElevation="750" red="148" blue="68" green="115" MinElevation="500"/>
  <ReliefColor MaxElevation="1000" red="131" blue="56" green="94" MinElevation="750"/>
  <ReliefColor MaxElevation="1200" red="94" blue="39" green="64" MinElevation="1000"/>
  <ReliefColor MaxElevation="1400" red="77" blue="30" green="49" MinElevation="1200"/>
  <ReliefColor MaxElevation="1500" red="61" blue="24" green="39" MinElevation="1400"/>
</ReliefColors>

```

---

### Vector

Dieses Verzeichnis enthält Daten zu

* Archäologischen Fundorten (*archaeological_sites*)
* Küstenlinien (*kuestenlinie*)
* Landschaftstypen (*landtype*)
* Rohstoffvorkommen (*resources*)
* Hauptstädten (*sites*)
* Flüssen (*streams*)
* Herrschaftsgebieten (*voronoi*)

in den Unterverzeichnissen liegen dieselben Daten teilweise in Auszügen in unterschiedlichen Formaten (spatialite, geojson, geopackage) vor.

---

#### archaeological_sites

123 zufällig auf der Insel verteilte archäologische Fundplätze mit Zuweisung einer Zeitstufe (vgl. `\tables\atlantgis_periods.csv`)

Hinweis: ID_AR_SITE: 120 ist doppelt vergeben!
![](https://i.imgur.com/7jLST4a.png)

`Geometrietyp: MultiPoint`

![](https://i.imgur.com/DxZuEVU.png)
![](https://i.imgur.com/H6N9jSi.png)

---

#### kuestenlinie

Küstenlinie der Insel, abgeleitet aus dem SRTM-Geländemodell im Verzeichnis `\raster\dem\`

2 Polygone (Insel vor Küste im NW), keine Attributwerte.

![](https://i.imgur.com/Wg5ZX3r.png)



---

#### landtype

Als `landtype` wurde eine Klassifizierung nach "Habit Types" aus folgender Publikation übernommen.
> Porter, RF & AS Suleiman. 2013. *The populations and distribution of the breeding birds of the Socotra archipelago*, Yemen: 1. Sandgrouse to Buntings. Sandgrouse 35: 43-81.

* [Link zur Website (archive.org)](https://web.archive.org/web/20210127010203/https://cmep.org.uk/botanists-help-socotra-bird-studies/)
* [Link zur Kartenvorlage (archive.org)](https://web.archive.org/web/20211124113946/https://cmep.org.uk/wp-content/uploads/2013/07/Socotra-island.jpg)

Kartenvorlage wurde georeferenziert und die Poygone vektorisiert.

`Geometrietyp: MultiPolygon`

![](https://i.imgur.com/i6nelbr.png)
![](https://i.imgur.com/BITvCDw.png)

---

#### resources

Frei erfundene Rohstoffvorkommen als Polygone. Die Bezeichnungen richten sich nach den Angaben im Kritias-Dialog des Platon.

`Geometrietyp: MultiPolygon`

![](https://i.imgur.com/g4kQ6EC.png)
![](https://i.imgur.com/VnprjDb.png)

---

#### sites

10 "Hauptstädte" der Söhne von Kleito und Poseidon, gegründet in Periode IIb.

![](https://i.imgur.com/BNdb7yc.png)

---

#### streams

Fließgewässer auf AtlantGIS, abgeleitet aus SRTM-Geländemodell im Verzeichnis `\raster\dem\`.

Attribute:

`PK_UID`: unique identifier
`cat`: entspricht *PK_UID*
`value`: nicht rekonstruierbare Werte
`label`: keine Werte vergeben 
`discharge`: Abflussmenge
`distance`: keine Werte vergeben

`Geometrietyp: MultiLineString`

![](https://i.imgur.com/SZKxL52.png)


----

#### voronoi

Als Voronoi-Polygone aus `sites` abgeleitete "Herrschaftsgebiete" der einzelnen Söhne von Kleito und Poseidon.

Werte im Feld `cat` entsprechen den Werte aus `id` in `sites`.

![](https://i.imgur.com/WnuOiK0.png)


