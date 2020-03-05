__author__ = "Florian Thiery"
__copyright__ = "MIT Licence 2019, Research Squirrel Engineers, Florian Thiery"
__credits__ = ["Florian Thiery", "Research Squirrel Engineers"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Florian Thiery"
__email__ = "rse@fthiery.de"
__status__ = "draft"

# import dependencies
import uuid
import pandas as pd
import os
import codecs
import datetime

# set paths
dir_path = os.path.dirname(os.path.realpath(__file__))
file_in = dir_path + "\\" + "Finds.csv"
file_out = dir_path + "\\" + "finds.ttl"

# read csv file
data = pd.read_csv(
    file_in, # relative python path to subdirectory
    encoding='utf-8',
    sep=',', # deliminiter
    quotechar="'",  # single quote allowed as quote character
    dtype={"muendungsD": float, "muendungsH": float, "minD": float, "minD_H": float, "maxD": float, "maxD_H": float, "bodenD": float, "size": int, "wall": int, "temperSize": object}, # parse as an integer
    #usecols=['site', 'feature', 'objectF', 'classF', 'sherd', 'vesselShape'], # only load the  columns specified
    skiprows=0, # skip X rows of the file
    na_values=['.', '??'] # take any '.' or '??' values as NA
)

# create triples from dataframe
outStr = ""
i = 0
lines = []
for index, row in data.iterrows():
    lines.append("find:" + str(i) + " " + "rdf:type" + " atlantgis:Find .")
    lines.append("find:" + str(i) + " " + "atlantgis:site" + " site:" + row['site'] + " .")
    lines.append("find:" + str(i) + " " + "atlantgis:vesselShape" + " vesseltype:" + str(row['vesselShape']) + " .")
    lines.append("find:" + str(i) + " " + "atlantgis:feature" + " " + "'" + row['feature'] + "'@en" + ".")
    lines.append("find:" + str(i) + " " + "atlantgis:object" + " " + "'" + str(row['objectF']) + "'" + ".")
    lines.append("find:" + str(i) + " " + "atlantgis:class" + " " + "'" + str(row['classF']) + "'" + ".")
    lines.append("find:" + str(i) + " " + "atlantgis:sherd" + " " + "'" + str(row['sherd']) + "'" + ".")
    lines.append("find:" + str(i) + " " + "atlantgis:quantity" + " " + "'" + str(row['qty']) + "'" + ".")
    lines.append("find:" + str(i) + " " + "atlantgis:weight" + " " + "'" + str(row['wt']) + "'" + ".")
    lines.append("find:" + str(i) + " " + "atlantgis:temperSize" + " " + "'" + str(row['temperSize']) + "'" + ".")
    if row['size'] != -1:
        lines.append("find:" + str(i) + " " + "atlantgis:size" + " " + "'" + str(row['size']) + "'" + ".")
    if row['wall'] != -1:
        lines.append("find:" + str(i) + " " + "atlantgis:wall" + " " + "'" + str(row['wall']) + "'" + ".")
    if row['muendungsD'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:muendungsD" + " " + "'" + str(row['muendungsD']) + "'" + ".")
    if row['muendungsH'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:muendungsH" + " " + "'" + str(row['muendungsH']) + "'" + ".")
    if row['minD'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:minD" + " " + "'" + str(row['minD']) + "'" + ".")
    if row['minD_H'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:minD_H" + " " + "'" + str(row['minD_H']) + "'" + ".")
    if row['maxD'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:maxD" + " " + "'" + str(row['maxD']) + "'" + ".")
    if row['maxD_H'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:maxD_H" + " " + "'" + str(row['maxD_H']) + "'" + ".")
    if row['bodenD'] != -1.0:
        lines.append("find:" + str(i) + " " + "atlantgis:bodenD" + " " + "'" + str(row['bodenD']) + "'" + ".")
    lines.append("")
    i += 1

# write output file
file = codecs.open(file_out, "w", "utf-8")
prefixes = []
prefixes.append("PREFIX atlantgis: <http://atlantgis.squirrel.link/ontology#>")
prefixes.append("PREFIX site: <http://atlantgis.squirrel.link/site#>")
prefixes.append("PREFIX find: <http://atlantgis.squirrel.link/find#>")
prefixes.append("PREFIX vesseltype: <http://atlantgis.squirrel.link/vesseltype#>")
prefixes.append("PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>")
prefixes.append("PREFIX owl: <http://www.w3.org/2002/07/owl#>")
prefixes.append("PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>")
prefixes.append("PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>")
prefixes.append("")
file.write("# create triples from" + "\r\n")
file.write("# " + file_in + "\r\n")
file.write("# on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\r\n")
file.write("# by python script" + "\r\n\r\n")
for prefix in prefixes:
    file.write(prefix)
    file.write("\r\n")
for line in lines:
    file.write(line)
    file.write("\r\n")
file.close()
