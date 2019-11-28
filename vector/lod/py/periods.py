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
file_in = dir_path + "\\" + "atlantgis_periods.csv"
file_out = dir_path + "\\" + "periods.ttl"

# read csv file
data = pd.read_csv(
    file_in, # relative python path to subdirectory
    encoding='utf-8',
    sep='\t', # deliminiter
    quotechar="'",  # single quote allowed as quote character
    dtype={"period_counter": int, "period_before": int, "period_after": int}, # parse as an integer
    usecols=['period_counter', 'period_code', 'period_desc', 'period_before', 'period_after'], # only load the  columns specified
    skiprows=0, # skip X rows of the file
    na_values=['.', '??'] # take any '.' or '??' values as NA
)

# create triples from dataframe
outStr = ""
i = 0
lines = []
for index, row in data.iterrows():
    lines.append("period:" + str(row['period_counter']) + " " + "rdf:type" + " atlantgis:Period .")
    lines.append("period:" + str(row['period_counter']) + " " + "atlantgis:code" + " " + "'" + row['period_code'] + "'@en" + ".")
    lines.append("period:" + str(row['period_counter']) + " " + "atlantgis:description" + " " + "'" + row['period_desc'] + "'@en" + ".")
    if row['period_before'] != 0:
        lines.append("period:" + str(row['period_counter']) + " " + "atlantgis:period_before" + " period:" + str(row['period_before']) + " .")
    if row['period_after'] != 0:
        lines.append("period:" + str(row['period_counter']) + " " + "atlantgis:period_after" + " period:" + str(row['period_after']) + " .")
    lines.append("")

# write output file
file = codecs.open(file_out, "w", "utf-8")
prefixes = []
prefixes.append("PREFIX atlantgis: <http://atlantgis.squirrel.link/ontology#>")
prefixes.append("PREFIX period: <http://atlantgis.squirrel.link/period#>")
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
