from rdflib import Namespace, URIRef

QB = Namespace("http://purl.org/linked-data/cube#")
BIO = Namespace("http://purl.org/vocab/bio/0.1/")
SDMX_DIMENSION = Namespace("http://purl.org/linked-data/sdmx/2009/dimension#")
SDMX_MEASURE = Namespace("http://purl.org/linked-data/sdmx/2009/measure#")
SDMX_ATTRIBUTE = Namespace("http://purl.org/linked-data/sdmx/2009/attribute#")
DPC_NS = Namespace("http://www.protezionecivile.gov.it/ns/")
DPC_DATASET = Namespace("http://www.protezionecivile.gov.it/dataset/covid19/")
DPC_NS = Namespace("http://www.protezionecivile.gov.it/ns/")
URI_ONTOPIA_ITALY = URIRef('https://w3id.org/italia/controlled-vocabulary/territorial-classifications/countries/italy/ITA')
URI_ONTOPIA_REGION_CHUNK = "https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/"
URI_ONTOPIA_PROVINCE_CHUNK = "https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/"
BASE_URI = 'http://www.protezionecivile.gov.it/dataset/covid19/'

measures = {
    'ricoverati_con_sintomi': {
        'uri_chunk': 'hospitalized-with-symptoms',
        'label_ita': 'ricoverati con sintomi',
        'label_eng': 'hospitalized with symptoms',
        'property': DPC_NS.hospitalizedWithSymptoms
    },
    'terapia_intensiva': {
        'uri_chunk': 'intensive-care',
        'label_ita': 'terapia intensiva',
        'label_eng': 'intensive care',
        'property': DPC_NS.intensiveCare
    },
    'totale_ospedalizzati': {
        'uri_chunk': 'total-hospitalized',
        'label_ita': 'totale ospedalizzati',
        'label_eng': 'total hospitalized',
        'property': DPC_NS.totalHospitalized
    },
    'isolamento_domiciliare': {
        'uri_chunk': 'home-isolation',
        'label_ita': 'isolamento domiciliare',
        'label_eng': 'home isolation',
        'property': DPC_NS.homeIsolation
    },
    'totale_positivi': {
        'uri_chunk': 'total-positive',
        'label_ita': 'totale positivi',
        'label_eng': 'total positive',
        'property': DPC_NS.totalPositive
    },
    'variazione_totale_positivi': {
        'uri_chunk': 'total-positive-variation',
        'label_ita': 'variazione totale positivi',
        'label_eng': 'Total positive variation',
        'property': DPC_NS.totalPositiveVariation
    },
    'nuovi_positivi': {
        'uri_chunk': 'new-positive',
        'label_ita': 'nuovi positivi',
        'label_eng': 'new positive',
        'property': DPC_NS.newPositive
    },
    'dimessi_guariti': {
        'uri_chunk': 'healed',
        'label_ita': 'dimessi guariti',
        'label_eng': 'healed',
        'property': DPC_NS.healed
    },
    'deceduti': {
        'uri_chunk': 'deads',
        'label_ita': 'deceduti',
        'label_eng': 'deads',
        'property': DPC_NS.deads
    },
    'totale_casi': {
        'uri_chunk': 'total-cases',
        'label_ita': 'totale casi',
        'label_eng': 'totale cases',
        'property': DPC_NS.totalCases
    },
    'tamponi': {
        'uri_chunk': 'swabs',
        'label_ita': 'tamponi',
        'label_eng': 'swabs',
        'property': DPC_NS.swabs
    }
}