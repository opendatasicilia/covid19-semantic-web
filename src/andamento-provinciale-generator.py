from rdflib import Literal, URIRef
from rdflib.namespace import  RDFS, XSD
from datetime import datetime
import csv
from builder import DPCGraphBuilder
from utils import BASE_URI, QB, DPC_NS, SDMX_DIMENSION, URI_ONTOPIA_PROVINCE_CHUNK, measures

dataset_chunk = 'provincial-trend'
dataset_title = 'CoVid-19 - Andamento provinciale'

builder = DPCGraphBuilder(dataset_chunk, dataset_title)
builder.add_dimensions()
builder.add_attributes()
builder.add_total_cases_measure()


with open('../input/dpc-covid19-ita-province.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row['data']
        date_uri_chunk = date.replace('-', '')[0:8]

        date_obj = datetime.strptime(date_uri_chunk, '%Y%m%d')
        date_label = date_obj.strftime("%d/%m/%Y")

        uri_row = URIRef(f'{BASE_URI}{dataset_chunk}/observations/{date_uri_chunk}/regions/{row["codice_regione"]}/provinces/{row["codice_provincia"]}')

        builder.add_observation(uri_row)

        builder.add_triple((uri_row, SDMX_DIMENSION.refTime, Literal(date_uri_chunk, datatype=XSD.date)))
        builder.add_triple((uri_row, SDMX_DIMENSION.refArea, URIRef(f'{URI_ONTOPIA_PROVINCE_CHUNK}{row["codice_provincia"]}')))

        builder.add_triple((uri_row, DPC_NS.totalCases, Literal(row['totale_casi'], datatype=XSD.int)))
        builder.add_triple((uri_row, RDFS.label, Literal(f'Regione {row["denominazione_regione"]}, provincia {row["denominazione_provincia"]}, totale casi di giorno {date_label}: {row["totale_casi"]}', datatype=XSD.string)))

    builder.save('../output/dpc-covid19-ita-province.ttl')
