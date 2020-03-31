from rdflib import Literal, URIRef
from rdflib.namespace import  RDFS, XSD
from datetime import datetime
import csv
from builder import DPCGraphBuilder
from utils import BASE_URI, QB, SDMX_DIMENSION, URI_ONTOPIA_REGION_CHUNK, measures

dataset_chunk = 'regional-trend'
dataset_title = 'CoVid-19 - Andamento Regionale'

builder = DPCGraphBuilder(dataset_chunk, dataset_title)
builder.add_dimensions()
builder.add_attributes()
builder.add_measures()
builder.add_total_cases_measure()


with open('../input/dpc-covid19-ita-regioni.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row['data']
        date_uri_chunk = date.replace('-', '')[0:8]

        date_obj = datetime.strptime(date_uri_chunk, '%Y%m%d')
        date_label = date_obj.strftime("%d/%m/%Y")
        uri_row = URIRef(f'{BASE_URI}{dataset_chunk}/observations/{date_uri_chunk}/regions/{row["codice_regione"]}')

        builder.add_observation(uri_row)

        builder.add_triple((uri_row, SDMX_DIMENSION.refTime, Literal(date_uri_chunk, datatype=XSD.date)))
        builder.add_triple((uri_row, SDMX_DIMENSION.refArea, URIRef(f'{URI_ONTOPIA_REGION_CHUNK}{row["codice_regione"]}')))


        for measure, value in measures.items():
            builder.add_triple((uri_row, value["property"], Literal(int(row[measure]), datatype=XSD.int)))
            builder.add_triple((uri_row, RDFS.label, Literal(f'Andamento COVID-19 della regione {row["denominazione_regione"]}', datatype=XSD.string)))

    builder.save('../output/dpc-covid19-ita-regioni.ttl')
