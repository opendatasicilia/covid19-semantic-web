## COVID-19 Semantic Web - DPC RDF Data Cube Vocabulary Project

Il progetto intende modellare i dataset del monitoraggio sanitario COVID-19 in Italia, 
pubblicati dalla Protezione Civile quotidianamente, disponibili  sul
repository ufficiale [GitHub](https://github.com/pcm-dpc/COVID-19), attraverso il modello
[RDF Data Cube Vocabulary](https://www.w3.org/TR/vocab-data-cube/).

Una sintesi del modello è rappresentata nella seguente figura:

![RDF Data Cube Vocabulary](https://www.w3.org/TR/vocab-data-cube/images/qb-fig1.png)

I dataset della protezione civile sono nella seguente forma:

* Andamento nazionale ([dpc-covid19-ita-andamento-nazionale.csv](https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv))
```
data,stato,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,note_it,note_en
2020-02-24T18:00:00,ITA,101,26,127,94,221,0,221,1,7,229,4324,,
```

* Andamento regionale ([dpc-covid19-ita-regioni.csv](https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv))
```
data,stato,codice_regione,denominazione_regione,lat,long,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_positivi,variazione_totale_positivi,nuovi_positivi,dimessi_guariti,deceduti,totale_casi,tamponi,note_it,note_en
2020-02-24T18:00:00,ITA,03,Lombardia,45.46679409,9.190347404,76,19,95,71,166,0,166,0,6,172,1463,,
```

* Andamento provinciale ([dpc-covid19-ita-province.csv](https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv))
```
data,stato,codice_regione,denominazione_regione,codice_provincia,denominazione_provincia,sigla_provincia,lat,long,totale_casi,note_it,note_en
2020-03-30T17:00:00,ITA,03,Lombardia,016,Bergamo,BG,45.69441368,9.668424528,8664,,
```

## Metodologia

Applicare il modello semantico **RDF Data Cube Vocabulary** ad un dataset significa definire per ciascuna osservazione i seguenti concetti:

* **Dimensioni**
* **Misure**
* **Attributi** 

E' possibile applicare diverse strategie sia per l'architettura delle URI sia per l'organizzazione delle osservazioni all'interno del dataset.
Per maggiori dettagli implementativi si consiglia di consultare la raccomandazione W3C sopra citata.

Per motivi di semplicità e facilità delle interrogazioni l'approccio scelto è `row-oriented` e `multiple measures` (vedi raccomandazione).


### Andamento Nazionale
[Download dati](https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv)


* **URI**: Ciascuna riga viene identificata da una apposita `URI` secondo il seguente schema:

`http://www.protezionecivile.gov.it/dataset/covid19/national-trend/observations/20200330`
#### Dimensioni
Nome   | Property
------------ | -------------
Data | http://purl.org/linked-data/sdmx/2009/dimension#refTime
Area geografica | http://purl.org/linked-data/sdmx/2009/dimension#refArea

#### Misurazioni
Nome   | Property
------------ | -------------
Ricoverati con sintomi | http://www.protezionecivile.gov.it/ns/hospitalizedWithSymptoms
Terapia intensiva| http://www.protezionecivile.gov.it/ns/intensiveCare
Totale ospedalizzati| http://www.protezionecivile.gov.it/ns/totalHospitalized
Isolamento domiciliare | http://www.protezionecivile.gov.it/ns/homeIsolation
Totale positivi | http://www.protezionecivile.gov.it/ns/totalPositive
Variazione totale positivi | http://www.protezionecivile.gov.it/ns/totalPositiveVariation
Nuovi positivi| http://www.protezionecivile.gov.it/ns/newPositive
Dimessi guariti | http://www.protezionecivile.gov.it/ns/healed
Deceduti | http://www.protezionecivile.gov.it/ns/deads
Tamponi | http://www.protezionecivile.gov.it/ns/swabs
Totale casi | http://www.protezionecivile.gov.it/ns/totalCases

L'istanza relativa alla dimensione dell'area geografica è stata presa dal progetto [Ontopia](https://github.com/italia/daf-ontologie-vocabolari-controllati), nella 
fattispecie dal vocabolario controllato della [classificazione territoriale](https://github.com/italia/daf-ontologie-vocabolari-controllati/tree/master/VocabolariControllati/territorial-classifications):

`<https://w3id.org/italia/controlled-vocabulary/territorial-classifications/countries/italy/ITA>`


### Andamento Regionale
[Download dati](https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv)


* **URI**: Ciascuna riga viene identificata da una apposita `URI` secondo il seguente schema:

`http://www.protezionecivile.gov.it/dataset/covid19/regional-trend/observations/20200224/regions/01`

#### Dimensioni

Nome   | Property
------------ | -------------
Data | http://purl.org/linked-data/sdmx/2009/dimension#refTime
Area geografica | http://purl.org/linked-data/sdmx/2009/dimension#refArea

#### Misurazioni
Nome   | Property
------------ | -------------
Ricoverati con sintomi | http://www.protezionecivile.gov.it/ns/hospitalizedWithSymptoms
Terapia intensiva| http://www.protezionecivile.gov.it/ns/intensiveCare
Totale ospedalizzati| http://www.protezionecivile.gov.it/ns/totalHospitalized
Isolamento domiciliare | http://www.protezionecivile.gov.it/ns/homeIsolation
Totale positivi | http://www.protezionecivile.gov.it/ns/totalPositive
Variazione totale positivi | http://www.protezionecivile.gov.it/ns/totalPositiveVariation
Nuovi positivi| http://www.protezionecivile.gov.it/ns/newPositive
Dimessi guariti | http://www.protezionecivile.gov.it/ns/healed
Deceduti | http://www.protezionecivile.gov.it/ns/deads
Tamponi | http://www.protezionecivile.gov.it/ns/swabs
Totale casi | http://www.protezionecivile.gov.it/ns/totalCases

L'istanza relativa alla dimensione dell'area geografica (regioni) è stata presa dal progetto [Ontopia](https://github.com/italia/daf-ontologie-vocabolari-controllati), nella 
fattispecie dal vocabolario controllato della [classificazione territoriale](https://github.com/italia/daf-ontologie-vocabolari-controllati/tree/master/VocabolariControllati/territorial-classifications):

`<https://w3id.org/italia/controlled-vocabulary/territorial-classifications/regions/02>`


### Andamento Provinciale
[Download dati](https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv)

* **URI**: Ciascuna riga viene identificata da una apposita `URI` secondo il seguente schema:

`http://www.protezionecivile.gov.it/dataset/covid19/provincial-trend/observations/20200224/regions/01/provinces/001`

#### Dimensioni

Nome   | Property
------------ | -------------
Data | http://purl.org/linked-data/sdmx/2009/dimension#refTime
Area geografica | http://purl.org/linked-data/sdmx/2009/dimension#refArea

#### Misurazioni

Nome   | Property
------------ | -------------
Totale casi | http://www.protezionecivile.gov.it/ns/totalCases

L'istanza relativa alla dimensione dell'area geografica (province) è stata presa dal progetto [Ontopia](https://github.com/italia/daf-ontologie-vocabolari-controllati), nella 
fattispecie dal vocabolario controllato della [classificazione territoriale](https://github.com/italia/daf-ontologie-vocabolari-controllati/tree/master/VocabolariControllati/territorial-classifications):

`<https://w3id.org/italia/controlled-vocabulary/territorial-classifications/provinces/001>`

## Esecuzione

Scaricare il progetto, entrare nell'apposita directory ed eseguire da shell:

```./run.sh```

Lo script creerà l'ambiente necessario (se non già presente), effettuerà il download dei dataset di interesse del progetto e 
avvierà la generazione di triple RDF in formato `turtle` disponibili al fine del processo all'interno della directory ```output```.


```bash
#!/bin/bash

folder="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

set -x

# Creazione ambiene
mkdir -p "$folder"/input
mkdir -p "$folder"/output
rm -r "$folder"/input/*.*
rm -r "$folder"/output/*.*

# Download file CSV dal repository github del Dipartimento Protezione Civile (https://github.com/pcm-dpc/COVID-19)
curl -sL "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv" > "$folder"/input/dpc-covid19-ita-andamento-nazionale.csv
curl -sL "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv" > "$folder"/input/dpc-covid19-ita-regioni.csv
curl -sL "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-province/dpc-covid19-ita-province.csv" > "$folder"/input/dpc-covid19-ita-province.csv

# Generazione triple RDF
cd src
for i in "$folder"/src/*generator.py; do
  python $i
done

```

## SPARQL Endpoint
I dati generati sono disponibili al seguente [SPARQL Endpoint](http://45.62.242.205:8890/sparql), aggiornato quotidianamente. 

### Query

* **Quali sono i dataset presenti nello store?**

[Demo](http://45.62.242.205:8890/sparql?default-graph-uri=&query=PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+%0D%0APREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+%0D%0APREFIX+dpc%3A+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fns%2F%3E%0D%0Aprefix+l0%3A+%3Chttps%3A%2F%2Fw3id.org%2Fitalia%2Fonto%2Fl0%2F%3E+%0D%0ASELECT+%3Fdataset+%3Flabel%0D%0AWHERE+%7B%0D%0A%3Fdataset+a+qb%3ADataset%3B%0D%0A+++++++++rdfs%3Alabel+%3Flabel.%0D%0A%7D&format=text%2Fhtml&timeout=0&debug=on)

```sparql
PREFIX qb: <http://purl.org/linked-data/cube#> 
PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> 
PREFIX dpc: <http://www.protezionecivile.gov.it/ns/>
prefix l0: <https://w3id.org/italia/onto/l0/> 
SELECT ?dataset ?label
WHERE {
?dataset a qb:Dataset;
         rdfs:label ?label.
}

```

* **Quali sono i dati sanitari totali italiani del 25 marzo 2020?** 

[Demo](http://45.62.242.205:8890/sparql?default-graph-uri=&query=PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+%0D%0APREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+%0D%0APREFIX+dpc%3A+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fns%2F%3E%0D%0Aprefix+l0%3A+%3Chttps%3A%2F%2Fw3id.org%2Fitalia%2Fonto%2Fl0%2F%3E+%0D%0A%0D%0Aselect+%3Farea+%3Fdate+%3FhospitalizedWithSymptoms+%3FintensiveCare+%0D%0A%3FtotalHospitalized+%3FhomeIsolation+%3FtotalPositive+%0D%0A%3FnewPositive+%3FtotalPositiveVariation+%3Fhealed+%3Fdeads+%3FtotalCases+%3Fswabs%0D%0AWHERE%0D%0A%7B%0D%0A++++%3Fobs+a+qb%3AObservation%3B%0D%0A+++++++++qb%3Adataset+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fdataset%2Fcovid19%2Fnational-trend%3E%3B%0D%0A+++++++++sdmx-dimension%3ArefTime+%3Fdate%3B%0D%0A+++++++++sdmx-dimension%3ArefArea+%3Farea%3B%0D%0A+++++++++dpc%3AhospitalizedWithSymptoms+%3FhospitalizedWithSymptoms+%3B%0D%0A+++++++++dpc%3AintensiveCare+%3FintensiveCare+%3B%0D%0A+++++++++dpc%3AtotalHospitalized+%3FtotalHospitalized+%3B%0D%0A+++++++++dpc%3AhomeIsolation+%3FhomeIsolation+%3B%0D%0A+++++++++dpc%3AtotalPositive+%3FtotalPositive+%3B%0D%0A+++++++++dpc%3AnewPositive+%3FnewPositive+%3B%0D%0A+++++++++dpc%3AtotalPositiveVariation+%3FtotalPositiveVariation+%3B%0D%0A+++++++++dpc%3Ahealed+%3Fhealed+%3B%0D%0A+++++++++dpc%3Adeads+%3Fdeads+%3B%0D%0A+++++++++dpc%3AtotalCases+%3FtotalCases+%3B%0D%0A+++++++++dpc%3Aswabs+%3Fswabs+.%0D%0A+++++++++FILTER%28%3Fdate+%3D+%222020-03-25%22%5E%5Exsd%3Adate%29.%0D%0A%7D&format=text%2Fhtml&timeout=0&debug=on)
```sparql
PREFIX qb: <http://purl.org/linked-data/cube#> 
PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> 
PREFIX dpc: <http://www.protezionecivile.gov.it/ns/>
prefix l0: <https://w3id.org/italia/onto/l0/> 

select ?area ?date ?hospitalizedWithSymptoms ?intensiveCare 
?totalHospitalized ?homeIsolation ?totalPositive 
?newPositive ?totalPositiveVariation ?healed ?deads ?totalCases ?swabs
WHERE
{
    ?obs a qb:Observation;
         qb:dataset <http://www.protezionecivile.gov.it/dataset/covid19/national-trend>;
         sdmx-dimension:refTime ?date;
         sdmx-dimension:refArea ?area;
         dpc:hospitalizedWithSymptoms ?hospitalizedWithSymptoms ;
         dpc:intensiveCare ?intensiveCare ;
         dpc:totalHospitalized ?totalHospitalized ;
         dpc:homeIsolation ?homeIsolation ;
         dpc:totalPositive ?totalPositive ;
         dpc:newPositive ?newPositive ;
         dpc:totalPositiveVariation ?totalPositiveVariation ;
         dpc:healed ?healed ;
         dpc:deads ?deads ;
         dpc:totalCases ?totalCases ;
         dpc:swabs ?swabs .
         FILTER(?date = "2020-03-25"^^xsd:date).
}
```

* **Quali sono i dati sanitari della regione Lombardia del 25 marzo 2020?**
 
 *Per motivi di performance sono stati caricati nello store anche i vocabolari controllati di  [Ontopia](https://github.com/italia/daf-ontologie-vocabolari-controllati).*

[Demo](http://45.62.242.205:8890/sparql?default-graph-uri=&query=PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+%0D%0APREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+%0D%0APREFIX+dpc%3A+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fns%2F%3E%0D%0Aprefix+l0%3A+%3Chttps%3A%2F%2Fw3id.org%2Fitalia%2Fonto%2Fl0%2F%3E+%0D%0A%0D%0Aselect+%3Fobs+%3FareaName+%3Fdate+%3FintensiveCare+%0D%0A+++++++%3FtotalHospitalized+%3FtotalPositive+%3FhomeIsolation+%0D%0A+++++++%3FnewPositive+%3FtotalPositiveVariation+%0D%0A+++++++%3Fhealed+%3Fdeads+%3FtotalCases+%3Fswabs%0D%0AWHERE%0D%0A%7B%0D%0A++++%3Fobs+a+qb%3AObservation%3B%0D%0A+++++++++qb%3Adataset+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fdataset%2Fcovid19%2Fregional-trend%3E%3B%0D%0A+++++++++sdmx-dimension%3ArefTime+%3Fdate%3B%0D%0A+++++++++sdmx-dimension%3ArefArea+%3Farea%3B%0D%0A+++++++++dpc%3AtotalHospitalized+%3FtotalHospitalized+%3B%0D%0A+++++++++dpc%3AintensiveCare+%3FintensiveCare+%3B%0D%0A+++++++++dpc%3AhomeIsolation+%3FhomeIsolation+%3B%0D%0A+++++++++dpc%3AtotalPositive+%3FtotalPositive+%3B%0D%0A+++++++++dpc%3AnewPositive+%3FnewPositive+%3B%0D%0A+++++++++dpc%3AtotalCases+%3FtotalCases+%3B%0D%0A+++++++++dpc%3AtotalPositiveVariation+%3FtotalPositiveVariation+%3B%0D%0A+++++++++dpc%3Adeads+%3Fdeads+%3B%0D%0A+++++++++dpc%3Ahealed+%3Fhealed+%3B%0D%0A+++++++++dpc%3Aswabs+%3Fswabs+.%0D%0A+++++++++%3Farea+l0%3Aname+%3FareaName.%0D%0A+++++++++FILTER+regex%28%3FareaName%2C%22%5ELombardia%22%2C%22i%22%29.%0D%0A+++++++++FILTER%28%3Fdate+%3D+%222020-03-25%22%5E%5Exsd%3Adate%29.%0D%0A%7D&format=text%2Fhtml&timeout=0&debug=on)

```sparql
PREFIX qb: <http://purl.org/linked-data/cube#> 
PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> 
PREFIX dpc: <http://www.protezionecivile.gov.it/ns/>
prefix l0: <https://w3id.org/italia/onto/l0/> 

select ?obs ?areaName ?date ?intensiveCare 
       ?totalHospitalized ?totalPositive ?homeIsolation 
       ?newPositive ?totalPositiveVariation 
       ?healed ?deads ?totalCases ?swabs
WHERE
{
    ?obs a qb:Observation;
         qb:dataset <http://www.protezionecivile.gov.it/dataset/covid19/regional-trend>;
         sdmx-dimension:refTime ?date;
         sdmx-dimension:refArea ?area;
         dpc:totalHospitalized ?totalHospitalized ;
         dpc:intensiveCare ?intensiveCare ;
         dpc:homeIsolation ?homeIsolation ;
         dpc:totalPositive ?totalPositive ;
         dpc:newPositive ?newPositive ;
         dpc:totalCases ?totalCases ;
         dpc:totalPositiveVariation ?totalPositiveVariation ;
         dpc:deads ?deads ;
         dpc:healed ?healed ;
         dpc:swabs ?swabs .
         ?area l0:name ?areaName.
         FILTER regex(?areaName,"^Lombardia","i").
         FILTER(?date = "2020-03-25"^^xsd:date).
}
```

* **Quali sono i casi totali della provincia di Lodi?**
 
 *Per motivi di performance sono stati caricati nello store anche i vocabolari controllati di  [Ontopia](https://github.com/italia/daf-ontologie-vocabolari-controllati).*

[Demo](http://45.62.242.205:8890/sparql?default-graph-uri=&query=PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+%0D%0APREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+%0D%0APREFIX+dpc%3A+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fns%2F%3E%0D%0Aprefix+l0%3A+%3Chttps%3A%2F%2Fw3id.org%2Fitalia%2Fonto%2Fl0%2F%3E+%0D%0A%0D%0Aselect+%3FareaName+%3Fdate+%3FtotalCases+%0D%0AWHERE%0D%0A%7B%0D%0A++++%3Fobs+a+qb%3AObservation%3B%0D%0A+++++++++qb%3Adataset+%3Chttp%3A%2F%2Fwww.protezionecivile.gov.it%2Fdataset%2Fcovid19%2Fprovincial-trend%3E%3B%0D%0A+++++++++sdmx-dimension%3ArefTime+%3Fdate%3B%0D%0A+++++++++sdmx-dimension%3ArefArea+%3Farea%3B%0D%0A+++++++++dpc%3AtotalCases+%3FtotalCases+.%0D%0A+++++++++%3Farea+l0%3Aname+%3FareaName.%0D%0A+++++++++FILTER+regex%28%3FareaName%2C%22%5ELodi%22%2C%22i%22%29.%0D%0A%7D%0D%0AORDER+BY+DESC%28%3Fdate%29&format=text%2Fhtml&timeout=0&debug=on)

```sparql
PREFIX qb: <http://purl.org/linked-data/cube#> 
PREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> 
PREFIX dpc: <http://www.protezionecivile.gov.it/ns/>
prefix l0: <https://w3id.org/italia/onto/l0/> 

select ?areaName ?date ?totalCases 
WHERE
{
    ?obs a qb:Observation;
         qb:dataset <http://www.protezionecivile.gov.it/dataset/covid19/provincial-trend>;
         sdmx-dimension:refTime ?date;
         sdmx-dimension:refArea ?area;
         dpc:totalCases ?totalCases .
         ?area l0:name ?areaName.
         FILTER regex(?areaName,"^Lodi","i").
}
ORDER BY DESC(?date)
```


## Ulteriori sviluppi

* Arricchire i dati RDF collegandoli con dataset esterni
