from rdflib import Literal, URIRef
from rdflib.namespace import  RDFS, XSD
from datetime import datetime
import csv
from builder import DPCGraphBuilder
from utils import BASE_URI, QB, SDMX_DIMENSION, URI_ONTOPIA_ITALY, measures

dataset_chunk = 'national-trend'
dataset_title = 'CoVid-19 - Andamento Nazionale'

builder = DPCGraphBuilder(dataset_chunk, dataset_title)
builder.add_dimensions()
builder.add_attributes()
builder.add_measures()
builder.add_total_cases_measure()


with open('../input/dpc-covid19-ita-andamento-nazionale.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date = row['data']
        date_uri_chunk = date.replace('-', '')[0:8]
        date_obj = datetime.strptime(date_uri_chunk, '%Y%m%d')
        date_label = date_obj.strftime("%d/%m/%Y")
        uri_row = URIRef(f'{BASE_URI}{dataset_chunk}/observations/{date_uri_chunk}')

        builder.add_observation(uri_row)

        builder.add_triple((uri_row, SDMX_DIMENSION.refTime, Literal(date_uri_chunk, datatype=XSD.date)))
        builder.add_triple((uri_row, SDMX_DIMENSION.refArea, URI_ONTOPIA_ITALY))

        for measure, value in measures.items():
            builder.add_triple((uri_row, value["property"], Literal(row[measure], datatype=XSD.int)))
            builder.add_triple((uri_row, RDFS.label, Literal(f'Andamento nazionale di giorno {date_label}', datatype=XSD.string)))

    # save to filesystem
    builder.save('../output/dpc-covid19-ita-andamento-nazionale.ttl')
