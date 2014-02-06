#QGIS 2.0 Tutorial
#5. Workshop der AG CAA
##Tübingen
##Getting Started
###Einführende Übung zum Umgang mit der neuen QGIS-Benutzeroberfläche für fortgeschrittene GIS-Nutzer

In der Ankündigung des [Tutorials](http://ag-caa.de/workshop2014/tutorials/) heißt es:
> Der Workshop wendet sich an Interessenten, die bereits mit GIS in der Archäologie arbeiten. Er führt nicht in die Grundlagen von GIS ein. Um das notwendige Grundlagenwissen unter den Teilnehmenden sicher zu stellen, wird im Januar ein e-Learning-Modul mit Screencasts freigeschaltet, in dem die wichtigsten Funktionen von QGIS vorgeführt werden. Nutzerinnen und Nutzer anderer GIS-Programme soll damit die Möglichkeit gegeben werden, Grundfunktionen im Vorfeld des Workshops kennen zu lernen.

Dieses kurze Tutorial ist nun genau dieses "e-Learning-Modul". Es setzt ein Grundverständnis von GIS voraus und soll einen Einstieg in die allgemein üblichen Funktionen einer Desktop-Anwendung geben. Nutzt die im folgenden beschriebenen Schritte, um Euch mit der Oberfläche vertraut zu machen, dann fällt der Einstieg am Samstag Nachmittag leichter.

####QGIS 2.0 installieren
Eine aktuelle Beschreibung für die Installation von QGIS ist im [AWF-Wiki](http://wiki.awf.forst.uni-goettingen.de/wiki/index.php/QGIS_installation) der Uni-Göttingen zu finden.

Unter Microsoft-Betriebssystemen empfehlen wir unbedingt die Installation mit dem osgeo4w-Installer, wie im Wiki beschrieben. Bitte installiert gleichzeitig SAGA und GRASS GIS, damit wir die Funktionen nutzen können.

Sollen ältere QGIS-Versionen auf dem Rechner installiert sein, empfiehlt es sich, diese vorher zu deinstallieren. Dabei unbedingt darauf achten, dass zusätzlich der (versteckte) Ordner *.qgis* im Benutzerprofil unter Windows (*C:\Users\\{username}\\.qgis\...*) von Hand gelöscht wird.

In diesem .qgis-Ordner sollten normalerweise keine eigenen Daten liegen. Er dient nur der lokalen Konfiguration des Programms. Falls Ihr den Ordner bentutzt haben solltet, um eigene Daten zu speichern, diese bitte vorher sichern.

Nach der Installation kann es losgehen

####Daten herunterladen
Für diese kleine Rundtour nutzen wir Daten aus dem [AtlantGIS-Datensatz](http://kacebe.github.io/AtlantGIS/ "gesamter aktueller AtlantGIS-Datenbestand auf GitHub"). Der für den Workshop in Tübingen benötigte Datenauszug kann als [zip-Archiv](https://github.com/kacebe/AtlantGIS/archive/tuebingen2014.zip "Daten für den Workshop in Tübingen") heruntergeladen werden.

Nach dem Herunterladen das [zip-Archiv](https://github.com/kacebe/AtlantGIS/archive/tuebingen2014.zip "Daten für den Workshop in Tübingen") bitte an einem genehmen Ort auf der Festplatte entpacken. Für einige Anwendungen ist es wichtig, dass der Pfad zu den Dateien keine **Punkte (.)** oder **Leerzeichen** enthält. Ein Verzeichnisname wie etwa "*...\user\mein ordner für gis.tübingen\daten*" verursacht nur unnötigen Ärger.

####Neues Projekt anlegen
* Nach dem Start von QIS wird automatisch ein neues Projekt angelegt.
    * Das Standardkoordinatensystem ist meist auf WGS 84 voreingestellt (EPSG: 4326). Änderungen zum Koordinatenbezugssystems (KBS in QGIS) für neue Projekte können in den globalen Projekteinstellungen vorgenommen werden. Im nächsten Schritt seht ihr die einfachste Variante, das KBS des Projektes zu wechseln.
	* Umfangreiche Erläuterungen zur neuen QGIS-Oberfläche sind in der [Dokumentation] (http://qgis.org/de/docs/user_manual/introduction/qgis_gui.html "QGIS - User Manual: QGIS GUI") nachzulesen. Die folgenden Abschnitte und der Screencast "Projekteinstellungen" geben aber auch einen guten Überblick.
	
[![Screencast 1](http://b.vimeocdn.com/ts/462/315/462315048_295.jpg)](http://vimeo.com/85140013) 

####Daten in Projekt laden
* Über den Menüpunkt *Layer* jetzt erst einmal *geophys_excavation.tif* aus dem Verzeichnis *gettingstarted\geophys\* in das Projekt laden.
    * Bitte beachten: Der Layer hat eine UTM-Projektion (EPSG: 32628). Da es der erste geladene Layer in dem Projekt ist, wird das Projektkoordinatensystem auf dieses KBS geändert. Ganz unten rechts in der Statuszeile wird das aktuell eingestellte KBS angezeigt. Ein Klick auf das Symbol ![Symbol KBS-Status](http://qgis.org/de/_images/mIconProjectionDisabled.png "Symbol") daneben öffnet den Dialog für Anpassungen/Änderungen.
	* Für die Steuerung der Darstellung der geladenen Rasterdaten empfiehlt es sich, über das Menü *Ansicht* unter *Werkzeugkästen* einen Haken vor *Raster* zu setzen. Auf der Programmoberfläche erscheint eine Symbolleiste, die entsprechende Optionen bietet.
* In dem Datenverzeichnis *gettingstarted\* sind weitere Geodaten vorhanden.
	* im Verzeichnis *gettingstarted\sqlite\* liegt eine [SpatiaLite-Datenbank](https://www.gaia-gis.it/fossil/libspatialite/index) mit Vektordaten zu Mauer- und Befundumrissen einer (selbstverständlich frei erfundenen) archäologischen Grabung
		* Um Daten aus einer Datenbank in QGIS zu nutzen, muss zunächst eine Verbindung zu dem Datenbanksystem aufgebaut werden.
		* Unter *Menü - Layer* finden sich alle derzeit in QGIS verfügbaren Datenbanksysteme verzeichnet. Wählt *SpatiaLite Layer hinzufügen*. In dem Dialog muss über *Neu* zunächst die Datenbank adressiert werden. Wählt die *...\gettingstarted\sqlite\atlantgis_excavation.sqlite* Datei und anschließend *Verbinden*. Alle geometriehaltenden Tabellen werden angezeigt und können alle (mit gleichzeitig gedrückt gehaltener CTRL-Taste)  mit der Maus ausgewählt werden. Mit der Befehlfläche "Hinzufügen" unten im Dialog werden die Layer in das Projekt geladen.
	* im Verzeichnis *gettingstarted\vector\dxf\* liegt eine .dxf-Datei mit den Begrenzungen zweier Grabungsschnitte
		* dxf-Dateien können über *Layer - Vektorlayer hinzufügen* eingespielt werden. Achtet darauf, dass in dem Dialog "Öffnen eines OGR-Vektorlayers" ganz unten rechts das Format der zu öffnenden Datei gewählt werden kann.
		* da dxf-Dateien nicht wissen, in welchem KBS die Geometrien gespeichert sind, werden die Inhale nach dem Laden nicht angezeigt. Mit einem Klick der rechten Maustaste auf den dxf-Layer und dem Wählen der Option *KBS für Layer setzen...* kann das nachgeholt werden (hier: WGS 84 / UTM zone 28N; EPSG: 32628 wählen und bestätigen)
		* sollte einem das dxf-Format im GIS nicht geheuer sein, kann der Datensatz in eine Reihe Geodatenformate umgewandelt werden. Dafür wieder mit der rechten Mautaste auf den dxf-Layer klicken und über *Speichern als...* die gewünschten Einstellungen vornehmen.
	* im Verzeichnis *gettingstarted\vector\shp\* ein Shapefile mit Punktgeometrien zu Kleinfunden aus der Grabung
		* Das Vorgehen entspricht dem Einspielen von dxf-Daten. Über *Layer - Vektorlayer hinzufügen* den Datensatz auswählen und bestätigen.
	* abschließend das Projekt speichern *Menü - Projekt - Speichern*
		* dabei bitte die Einstellungen zu relativen und absoluten Pfaden beachten (s. oben verlinkten Screencast)

####Arbeiten mit den Projektdaten

In einer Reihe von [Screencasts](https://vimeo.com/channels/qgisworkshops) haben wir die meisten grundlegenden Funktionen interaktiv aufbereitet.

Zusätzliche Hilfe bietet die umfangreiche [Dokumentation des QGIS-Projekts](http://qgis.org/de/docs/user_manual/index.html).

Als Zielstellung für die Anpassung der Layereinstellungen kann folgendes Ergebnis dienen:

![AtlantGIS Ausgrabungsbefunde mit Ergebnissen der Geophysik](https://github.com/kacebe/AtlantGIS/raw/tuebingen2014/screenshots/atlantgis_trenches.png "AtlantGIS Ausgrabungsbefunde mit Ergebnissen der Geophysik")




