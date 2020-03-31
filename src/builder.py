from rdflib import Graph, Literal, Namespace, URIRef, BNode
from rdflib.namespace import RDF, RDFS, XSD, DCTERMS, SKOS
from utils import BASE_URI, QB, SDMX_DIMENSION, SDMX_MEASURE, SDMX_ATTRIBUTE, DPC_NS


class DPCGraphBuilder():
    def __init__(self, dataset_chunk, dataset_label):
        self.g = Graph()
        self.bind()
        self.dataset = URIRef(BASE_URI + dataset_chunk)
        self.g.add((self.dataset, RDF.type, QB.Dataset))
        self.g.add((self.dataset, DCTERMS.title, Literal(dataset_label, lang='IT')))
        self.g.add((self.dataset, RDFS.label, Literal(dataset_label, lang='IT')))
        self.g.add((self.dataset, RDFS.comment, Literal(dataset_label, lang='IT')))
        self.dataStructureDefinition = URIRef(BASE_URI + dataset_chunk + "/dsd")
        self.g.add((self.dataset, QB.structure, self.dataStructureDefinition))
        self.dataStructureDefinition = URIRef(BASE_URI + dataset_chunk + "/dsd")
        self.g.add((self.dataset, QB.structure, self.dataStructureDefinition))
        self.g.add((self.dataStructureDefinition, RDF.type, QB.DataStructureDefinition))
        self.g.add((self.dataStructureDefinition, RDFS.comment,Literal('Specifica dei componenti (dimensioni, misure, attributi)', lang='IT')))


    def bind(self):
        self.g.bind("qb", QB)
        self.g.bind("sdmx-dimension", SDMX_DIMENSION)
        self.g.bind("sdmx-measure", SDMX_MEASURE)
        self.g.bind("sdmx-attribute", SDMX_ATTRIBUTE)
        self.g.bind("dct", DCTERMS)
        self.g.bind("skos", SKOS)
        self.g.bind("dpc", DPC_NS)


    def add_dimensions(self):
        # Dimensioni
        # Data
        dataCS = BNode()
        self.g.add((dataCS, RDF.type, QB.ComponentSpecification))
        self.g.add((dataCS, QB.dimension, SDMX_DIMENSION.refTime))
        self.g.add((self.dataStructureDefinition, QB.component, dataCS))

        # Stato
        statoCS = BNode()
        self.g.add((statoCS, RDF.type, QB.ComponentSpecification))
        self.g.add((statoCS, QB.dimension, SDMX_DIMENSION.refArea))
        self.g.add((self.dataStructureDefinition, QB.component, statoCS))


    def add_attributes(self):
        attributeCS = BNode()
        self.g.add((attributeCS, RDF.type, QB.ComponentSpecification))
        self.g.add((attributeCS, QB.attribute, SDMX_ATTRIBUTE.unitMeasure))
        self.g.add((self.dataStructureDefinition, QB.component, attributeCS))

    def add_measures(self):
        # Misura
        # Ricoverati con Sintomi
        measureHWS = DPC_NS.hospitalizedWithSymptoms
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureHWS))
        self.g.add((measureHWS, RDF.type, QB.MeasureProperty))
        self.g.add((measureHWS, RDF.type, RDF.Property))
        self.g.add((measureHWS, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureHWS, DCTERMS.description, Literal("Ricoverati con sintomi", lang="IT")))
        self.g.add((measureHWS, RDFS.label, Literal("Ricoverati con sintomi", lang="IT")))
        self.g.add((measureHWS, SKOS.notation, Literal("Ricoverati con sintomi", lang="IT")))
        self.g.add((measureHWS, DCTERMS.description, Literal("hospitalized with symptoms", lang="EN")))
        self.g.add((measureHWS, RDFS.label, Literal("Hospitalized with symptoms", lang="EN")))
        self.g.add((measureHWS, SKOS.notation, Literal("Hospitalized with symptoms", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

        # Misura
        # Terapia intensiva
        measureIC = DPC_NS.intensiveCare
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureIC))
        self.g.add((measureIC, RDF.type, QB.MeasureProperty))
        self.g.add((measureIC, RDF.type, RDF.Property))
        self.g.add((measureIC, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureIC, DCTERMS.description, Literal("Terapia intensiva", lang="IT")))
        self.g.add((measureIC, RDFS.label, Literal("Terapia intensiva", lang="IT")))
        self.g.add((measureIC, SKOS.notation, Literal("Terapia intensiva", lang="IT")))
        self.g.add((measureIC, DCTERMS.description, Literal("Intensive care", lang="EN")))
        self.g.add((measureIC, RDFS.label, Literal("Intensive care", lang="EN")))
        self.g.add((measureIC, SKOS.notation, Literal("Intensive care", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

        # Misura
        # Totale ospedalizzati
        measureTH = DPC_NS.totalHospitalized
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureTH))
        self.g.add((measureTH, RDF.type, QB.MeasureProperty))
        self.g.add((measureTH, RDF.type, RDF.Property))
        self.g.add((measureTH, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureTH, DCTERMS.description, Literal("Totale ospedalizzati", lang="IT")))
        self.g.add((measureTH, RDFS.label, Literal("Totale ospedalizzati", lang="IT")))
        self.g.add((measureTH, SKOS.notation, Literal("Totale ospedalizzati", lang="IT")))
        self.g.add((measureTH, DCTERMS.description, Literal("Total hospitalized", lang="EN")))
        self.g.add((measureTH, RDFS.label, Literal("Total hospitalized", lang="EN")))
        self.g.add((measureTH, SKOS.notation, Literal("Total hospitalized", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureTH))

        # Misura
        # Isolamento domiciliare
        measureHI = DPC_NS.homeIsolation
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureHI))
        self.g.add((measureHI, RDF.type, QB.MeasureProperty))
        self.g.add((measureHI, RDF.type, RDF.Property))
        self.g.add((measureHI, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureHI, DCTERMS.description, Literal("Isolamento domiciliare", lang="IT")))
        self.g.add((measureHI, RDFS.label, Literal("Isolamento domiciliare", lang="IT")))
        self.g.add((measureHI, SKOS.notation, Literal("Isolamento domiciliare", lang="IT")))
        self.g.add((measureHI, DCTERMS.description, Literal("Home isolation", lang="EN")))
        self.g.add((measureHI, RDFS.label, Literal("Home isolation", lang="EN")))
        self.g.add((measureHI, SKOS.notation, Literal("Home isolation", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

        # Misura
        # Totale  positivi
        measureTCP = DPC_NS.totalPositive
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureTCP))
        self.g.add((measureTCP, RDF.type, QB.MeasureProperty))
        self.g.add((measureTCP, RDF.type, RDF.Property))
        self.g.add((measureTCP, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureTCP, DCTERMS.description, Literal("Totale positivi", lang="IT")))
        self.g.add((measureTCP, RDFS.label, Literal("Totale positivi", lang="IT")))
        self.g.add((measureTCP, SKOS.notation, Literal("Totale positivi", lang="IT")))
        self.g.add((measureTCP, DCTERMS.description, Literal("Total positive", lang="EN")))
        self.g.add((measureTCP, RDFS.label, Literal("Total positive", lang="EN")))
        self.g.add((measureTCP, SKOS.notation, Literal("Total positive", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))


        # Misura
        # Variazione totale  positivi
        measureTCP = DPC_NS.totalPositiveVariation
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureTCP))
        self.g.add((measureTCP, RDF.type, QB.MeasureProperty))
        self.g.add((measureTCP, RDF.type, RDF.Property))
        self.g.add((measureTCP, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureTCP, DCTERMS.description, Literal("Variazione totale positivi", lang="IT")))
        self.g.add((measureTCP, RDFS.label, Literal("Variazione totale positivi", lang="IT")))
        self.g.add((measureTCP, SKOS.notation, Literal("Variazione totale positivi", lang="IT")))
        self.g.add((measureTCP, DCTERMS.description, Literal("Total positive variation", lang="EN")))
        self.g.add((measureTCP, RDFS.label, Literal("Total positive variation", lang="EN")))
        self.g.add((measureTCP, SKOS.notation, Literal("Total positive variation", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))


        # Misura
        # Nuovi positivi
        measureNCP = DPC_NS.newPositive
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureNCP))
        self.g.add((measureNCP, RDF.type, QB.MeasureProperty))
        self.g.add((measureNCP, RDF.type, RDF.Property))
        self.g.add((measureNCP, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureNCP, DCTERMS.description, Literal("Nuovi positivi", lang="IT")))
        self.g.add((measureNCP, RDFS.label, Literal("Nuovi positivi", lang="IT")))
        self.g.add((measureNCP, SKOS.notation, Literal("Nuovi positivi", lang="IT")))
        self.g.add((measureNCP, DCTERMS.description, Literal("New positive", lang="EN")))
        self.g.add((measureNCP, RDFS.label, Literal("New positive", lang="EN")))
        self.g.add((measureNCP, SKOS.notation, Literal("New positive", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

        # Misura
        # Dimessi guariti
        measureH = DPC_NS.healed
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureH))
        self.g.add((measureH, RDF.type, QB.MeasureProperty))
        self.g.add((measureH, RDF.type, RDF.Property))
        self.g.add((measureH, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureH, DCTERMS.description, Literal("Dimessi guariti", lang="IT")))
        self.g.add((measureH, RDFS.label, Literal("Dimessi guariti", lang="IT")))
        self.g.add((measureH, SKOS.notation, Literal("Dimessi guariti", lang="IT")))
        self.g.add((measureH, DCTERMS.description, Literal("Healed", lang="EN")))
        self.g.add((measureH, RDFS.label, Literal("Healed", lang="EN")))
        self.g.add((measureH, SKOS.notation, Literal("Healed", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

        # Misura
        # Deceduti
        measureD = DPC_NS.deads
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureD))
        self.g.add((measureD, RDF.type, QB.MeasureProperty))
        self.g.add((measureD, RDF.type, RDF.Property))
        self.g.add((measureD, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureD, DCTERMS.description, Literal("Deceduti", lang="IT")))
        self.g.add((measureD, RDFS.label, Literal("Deceduti", lang="IT")))
        self.g.add((measureD, SKOS.notation, Literal("Deceduti", lang="IT")))
        self.g.add((measureD, DCTERMS.description, Literal("Deads", lang="EN")))
        self.g.add((measureD, RDFS.label, Literal("Deads", lang="EN")))
        self.g.add((measureD, SKOS.notation, Literal("Deads", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))


        # Misura
        # Tamponi
        measureS = DPC_NS.SWABS
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureS))
        self.g.add((measureS, RDF.type, QB.MeasureProperty))
        self.g.add((measureS, RDF.type, RDF.Property))
        self.g.add((measureS, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureS, DCTERMS.description, Literal("Tamponi", lang="IT")))
        self.g.add((measureS, RDFS.label, Literal("Tamponi", lang="IT")))
        self.g.add((measureS, SKOS.notation, Literal("Tamponi", lang="IT")))
        self.g.add((measureS, DCTERMS.description, Literal("Swabs", lang="EN")))
        self.g.add((measureS, RDFS.label, Literal("Swabs", lang="EN")))
        self.g.add((measureS, SKOS.notation, Literal("Swabs", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

    def add_total_cases_measure(self):
        # Misura
        # Totale casi
        measureTC = DPC_NS.totalCases
        measureComponentSpecification = BNode()
        self.g.add((measureComponentSpecification, RDF.type, QB.ComponentSpecification))
        self.g.add((measureComponentSpecification, QB.measure, measureTC))
        self.g.add((measureTC, RDF.type, QB.MeasureProperty))
        self.g.add((measureTC, RDF.type, RDF.Property))
        self.g.add((measureTC, RDFS.subPropertyOf, SDMX_MEASURE.obsValue))
        self.g.add((measureTC, DCTERMS.description, Literal("Totale casi", lang="IT")))
        self.g.add((measureTC, RDFS.label, Literal("Totale casi", lang="IT")))
        self.g.add((measureTC, SKOS.notation, Literal("Totale casi", lang="IT")))
        self.g.add((measureTC, DCTERMS.description, Literal("Total cases", lang="EN")))
        self.g.add((measureTC, RDFS.label, Literal("Total cases", lang="EN")))
        self.g.add((measureTC, SKOS.notation, Literal("Total cases", lang="EN")))
        self.g.add((measureComponentSpecification, RDFS.range, XSD.integer))
        self.g.add((self.dataStructureDefinition, QB.component, measureComponentSpecification))

    def add_type_measures(self):
        dataCS = BNode()
        self.g.add((dataCS, RDF.type, QB.ComponentSpecification))
        self.g.add((dataCS, QB.dimension, QB.measureType))
        self.g.add((self.dataStructureDefinition, QB.component, dataCS))

    def add_observation(self, uri_row):
        self.add_triple((uri_row, RDF.type, QB.Observation))
        self.add_triple((uri_row, QB.dataset, self.dataset))


    def add_triple(self, triple):
        self.g.add(triple)

    def export(self, format='turtle'):
        return self.g.serialize(format=format)

    def save(self, filename, format = 'turtle'):
        self.g.serialize(destination=filename, format=format)