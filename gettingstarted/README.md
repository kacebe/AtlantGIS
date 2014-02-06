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
    * Das Standardkoordinatensystem ist meist auf WGS 84 eingestellt (EPSG: 4326). Änderungen zum Koordinatenbezugssystems für neue Projekte können in den globalen Projekteinstellungen vorgenommen werden. Im nächsten Schritt seht ihr die einfachste Variante, das Koordinatensystem des Projektes zu wechseln.
* Über den Menüpunkt *Layer* jetzt erstmnal geophys_excavation.tif aus dem Verzeichnis *gettingstarted\geophys\* in das Projekt laden.
    * Bitte beachten: Der Layer hat eine UTM-Projektion (EPSG: 32628). Da es der erste geladene Layer in dem Projekt ist wird das Projektkoordinatensystem angepasst.
