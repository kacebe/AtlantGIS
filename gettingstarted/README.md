#QGIS 2.0 Tutorial
#Workshop der AG CAA
##Tübingen
##Getting Started
###Einführende Übung zum Umgang mit der neuen QGIS-Benutzeroberfläche für fortgeschrittene GIS-Nutzer

####Daten herunterladen
Für diese kleine Rundtour nutzen wir Daten aus dem [AtlantGIS-Datensatz](http://kacebe.github.io/AtlantGIS/ "gesamter aktueller AtlantGIS-Datenbestand auf GitHub"). Der für den Workshop in Täbingen benötigte Datenauszug kann als [zip-Archiv](https://github.com/kacebe/AtlantGIS/archive/tuebingen2014.zip "Daten für den Workshop in Tübingen") heruntergeladen werden.

Nach dem Herunterladen das zip-Archiv bitte an einem genehmen Ort auf der Festplatte entpacken. Für einige Anwendungen ist es wichtig, dass der Pfad zu den Dateien keine Punkte (.) oder Leerzeichen enthält. Ein Verzeichnisname wie etwa "...\user\mein ordner für gis.tübingen\daten" verursacht nur unnötigen Ärger.

####Neues Projekt anlegen
* Nach dem Start von QIS wird automatisch ein neues Projekt angelegt.
    * Das Standardkoordinatensystem ist meist auf WGS 84 voreingestellt (EPSG: 4326). Änderungen zum Koordinatenbezugssystems (KBS in QGIS) für neue Projekte können in den globalen Projekteinstellungen vorgenommen werden. Im nächsten Schritt seht ihr die einfachste Variante, das KBS des Projektes zu wechseln.
	* Umfangreiche Erläuterungen zur neuen QGIS-Oberfläche sind in der [Dokumentation] (http://qgis.org/de/docs/user_manual/introduction/qgis_gui.html "QGIS - User Manual: QGIS GUI") nachzulesen. Die folgenden Abschnitte geben aber auch einen guten Überblick.

Screencast "Projekteinstellungen"
	
	![Screencast 1: Projekteinstellungen](http://vimeo.com/85140013 "Projekteinstellungen")

####Daten in Projekt laden
* Über den Menüpunkt *Layer* jetzt erst einmal *geophys_excavation.tif* aus dem Verzeichnis *gettingstarted\geophys\* in das Projekt laden.
    * Bitte beachten: Der Layer hat eine UTM-Projektion (EPSG: 32628). Da es der erste geladene Layer in dem Projekt ist, wird das Projektkoordinatensystem auf dieses KBS geändert. Ganz unten rechts in der Statuszeile wird das aktuell eingestellte KBS angezeigt. Ein Klick auf das Symbol ![Symbol KBS-Status](http://qgis.org/de/_images/mIconProjectionDisabled.png "Symbol") daneben öffnet den Dialog für Anpassungen/Änderungen.
	* Für die Steuerung der Darstellung der geladenen Rasterdaten empfiehlt es sich, über das Menü *Ansicht* unter *Werkzeugkästen* einen Haken vor *Raster* zu setzen. Auf der Programmoberfläche erscheint eine Symbolleiste, die entsprechende Optionen bietet.
	
	
